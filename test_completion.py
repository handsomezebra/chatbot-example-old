import openai
import time

start = time.time()
result = openai.Completion.create(
  model="gpt-3.5-turbo-instruct",
  prompt="Write a blog article about Generative AI.",
  max_tokens=128,
  temperature=0
)
end = time.time()

print(result.choices[0].text)
print(end - start, "seconds")
