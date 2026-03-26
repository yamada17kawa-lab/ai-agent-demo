from openai import OpenAI

client = OpenAI(
    # 注意：本地运行必须带上 /v1
    base_url="http://localhost:11434/v1",
    api_key="yangxiaowang",  # Ollama 不需要 key，但 SDK 要求必须填一个非空字符串，随便填
)

completions = client.chat.completions.create(
    model="qwen3:8b",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "用python输出数字1-10"},
    ],
    stream=True,
)

# 因为你开启了 stream=True，需要遍历打印结果
for chunk in completions:
    # 使用 getattr 安全获取，如果没这个属性就返回 None
    # reasoning = getattr(chunk.choices[0].delta, "reasoning", None)
    content = chunk.choices[0].delta.content

    # if reasoning is not None:
    #     print(reasoning, end="", flush=True)
    if content is not None and content != "":
        print(content, end="", flush=True)
