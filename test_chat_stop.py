import openai
import time

start = time.time()
result = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a helpful assistant. Please continue the chat flow."},
    {"role": "user", "name": "Tom", "content": "Hello!"},
    {"role": "assistant", "name": "Jerry", "content": "Hi!"},
    {"role": "user", "name": "Tom", "content": "Where to go for dinner?"},
    {"role": "assistant", "name": "Jerry", "content": "Chinese food!"},
    {"role": "user", "name": "Tom", "content": "How about tomorrow?"},
    {"role": "assistant", "name": "Jerry", "content": "Italy food."},
    {"role": "user", "name": "Tom", "content": "How about next Monday?"},
  ],
  temperature=1
)
end = time.time()

print(result.choices[0].message)
print(end - start)
