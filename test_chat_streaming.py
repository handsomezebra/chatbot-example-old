import openai
import time

start = time.time()
result = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {
      "role": "system", 
      "content": "You are a helpful assistant."
    },
    {
      "role": "user", 
      "content": "Create a blog article about large language model."
    },
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
