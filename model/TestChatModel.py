
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_ollama import ChatOllama

chat = ChatOllama(model="qwen3:8b")

messages = [
    SystemMessage(content="你是一名诗人"),
    HumanMessage(content="写一首诗"),
    AIMessage(content="床前明月光，疑是地上霜"),
    HumanMessage(content="按照上面的格式，给我讲一个笑话")

]

res = chat.stream(messages)

for r in res:
    if r.content is not None and r.content != "":
        print(r.content, end="", flush=True)