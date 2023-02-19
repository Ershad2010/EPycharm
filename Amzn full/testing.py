import openai

openai.api_key = "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"

prompt = "The future of technology is"

response = openai.Completion.create(
    engine="davinci",
    prompt=prompt,
    max_tokens=100,
    temperature=0.7,
    top_p=0.9
)

print(f"{prompt} {response.choices[0].text}.")