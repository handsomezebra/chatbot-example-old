import openai
import time

start = time.time()
system_prompt_template = """Given the following context, please answer each question.

{context}
"""


system_prompt_template = """You are Bobby, a virtual assistant created by Huajun. Given the following context, please provide truthful, helpful, clear, and harmless responses to each question.

<context>
{context}
</context>
"""


system_prompt_template = """You are Bobby, a virtual assistant create by Huajun. You provide responses to questions that are clear, straightforward, and factually accurate, without speculation or falsehood. Given the following context, please answer each question truthfully to the best of your abilities based on the provided information. Answer each question with a brief summary followed by several bullet points. Put answer within <answer> and </answer> tags.

<context>
{context}
</context>
"""

with open("news_result.txt") as file:
  f = file.read()

system_prompt = system_prompt_template.format(context=f)


result = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": "Summarize the following news."},
  ],
  stream=True,
)

end1 = time.time()
print(end1 - start, "seconds")


for chunk in result:
  print(chunk.choices[0].delta.get("content", ""), flush=True, end="")

end2 = time.time()
print()
print(end2 - start, "seconds")
