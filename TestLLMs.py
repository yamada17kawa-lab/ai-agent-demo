
from langchain_ollama import OllamaLLM

model = OllamaLLM(model="qwen3:8b")

res = model.stream("说个笑话")


for r in res:
    print(r, end=" ", flush=True)