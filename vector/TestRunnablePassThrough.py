from langchain_core.documents import Document
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_ollama import OllamaEmbeddings, ChatOllama
from typing import List

chat = ChatOllama(model="qwen3:8b")

embedding = OllamaEmbeddings(model="qwen3-embedding:4b")

store  = InMemoryVectorStore(embedding=embedding)

store.add_texts(["减肥就是要少吃多练",
                 "在减脂期间吃东西很重要，清淡少油控制卡路里摄入并运动起来",
                 "跑步是很好的运动哦"])

retriever = store.as_retriever(serach_arg={"k": 2})

chatprompt = ChatPromptTemplate.from_messages([
    ("system", "你是一名世界上最好的健身专家，请以我提供的信息进行回答问题，参考信息是：{context}"),
    ("human", "用户提问：{question}")
])

strparser = StrOutputParser()

def format_func(docs: List[Document]):
    if not docs:
        return "无参考信息"
    else:
        prefer_context = "["

        for result in docs:
            prefer_context = prefer_context + result.page_content

        prefer_context = prefer_context + "]"
        return prefer_context

chain = {"question": RunnablePassthrough(), "context": retriever | format_func} | chatprompt | chat | strparser

for res in chain.stream("怎么减肥？"):
    if res is not None and res != "":
        print(res, end="", flush=True)