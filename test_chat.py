import openai
import time

start = time.time()
result = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "How are you today?"},
  ],
)
end = time.time()

print(result.choices[0].message)
print(end - start)
