import openai
import asyncio

async def chat_func():
  result = await openai.ChatCompletion.acreate(
    model="gpt-3.5-turbo",
    messages=[
      {"role": "system", "content": "You are a helpful assistant."},
      {"role": "user", "content": "Create a blog article about large language model."},
    ],
    stream=True,
  )

  async for chunk in result:
    print(chunk.choices[0].delta.get("content", ""), flush=True, end="")

asyncio.run(chat_func())
