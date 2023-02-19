import openai
import base64
import requests

openai.api_key = "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"

def wph2(text):
  code = f"<!-- wp:heading --> <h2>{text}</h2><!-- /wp:heading -->"
  return code

def wpp(text):
  code = f"<!-- wp:paragraph --><p>{text}</p><!-- /wp:paragraph -->"
  return code

def oai_answer(prompt):
  response = openai.Completion.create(
    engine="davinci",
    prompt=prompt,
    max_tokens=100,
    temperature=0.7,
    top_p=0.9
  )
  output = (response.get("choices")[0].get("text"))
  return output
keyword = input("Enter Your Keyword ")
prompt = f"write 6 topic about {keyword}"
content = wpp(oai_answer(f"write short intro about {keyword}").strip("").strip("\n"))
questions = oai_answer(prompt)
# print(questions)
questions_list = questions.strip().split("\n")
end_line = "write a paragraph about it"
qna = {}
for q in questions_list:
  command = f"{q} {end_line}"
  # print(command)
  answer = oai_answer(command).strip("").strip("\n")
  qna[q] = answer

wp_user ='Ahmad'
wp_pass ='W444 GVr5 ghQA TFn1 ooSd ATBK'
wp_credential = f'{wp_user}:{wp_pass}'
wp_token = base64.b64encode(wp_credential.encode())
wp_headers = {'Authorization': f'Basic {wp_token.decode("utf-8")}'}

def media_upload(image):
  media_url = 'https://bestjobinuae.com/wp-json/wp/v2/media'
  files = {'file': open(image, 'rb')}
  res = requests.post(media_url, files = files, headers = wp_headers)

for key, value in qna.items():
  qn = wph2(key)
  answer = wpp(value)
  temp_content = qn+answer
  content += temp_content

title = f"common thinks about {keyword}"
data = {
  "title": title.title(),
  "content": content,
  "slug":keyword.replace(" ", "-"),
  "categories":'172'
}
api_url = 'https://bestjobinuae.com/wp-json/wp/v2/posts'
r = requests.post(api_url, data = data, headers = wp_headers)


