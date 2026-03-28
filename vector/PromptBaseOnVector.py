from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_ollama import OllamaEmbeddings, ChatOllama


chat = ChatOllama(model="qwen3:8b")

embedding = OllamaEmbeddings(model="qwen3-embedding:4b")

store  = InMemoryVectorStore(embedding=embedding)

store.add_texts(["减肥就是要少吃多练",
                 "在减脂期间吃东西很重要，清淡少油控制卡路里摄入并运动起来",
                 "跑步是很好的运动哦"])

results = store.similarity_search("怎么减肥", 2)

prefer_context = "["

for result in results:
    prefer_context = prefer_context + result.page_content

prefer_context = prefer_context + "]"


chatprompt = ChatPromptTemplate.from_messages([
    ("system", "你是一名世界上最好的健身专家，请以我提供的信息进行回答问题，参考信息是：{context}"),
    ("human", "用户提问：{question}")
])



def print_prompt(prompt):
    print(prompt.to_string())
    print("="*20)
    return prompt

strparser = StrOutputParser()

chain = chatprompt | print_prompt | chat | strparser

res = chain.stream({"question": "怎么减肥", "context": prefer_context})
for result in res:
    if result is not None and result != "":
        print(result, end="", flush=True)

