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
    model="text-davinci-003",
    prompt=prompt,
    temperature=0.7,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
  )
  output = (response.get("choices")[0].get("text"))
  return output
keyword = input("Enter Your Keyword ")
prompt = f"write 6 topics about {keyword}"
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
for key, value in qna.items():
  qn = wph2(key)
  answer = wpp(value)
  temp_content = qn+answer
  content += temp_content

title = f"Common topics about {keyword}"
data = {
  "title": title.title(),
  "content": content,
  "slug":keyword.replace(" ", "-"),
  "categories":'172'
}
api_url = 'https://bestjobinuae.com/wp-json/wp/v2/posts'
r = requests.post(api_url, data = data, headers = wp_headers)
print(r.json())

