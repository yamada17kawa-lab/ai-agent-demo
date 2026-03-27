from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, PromptTemplate
from langchain_core.runnables import RunnableLambda
from langchain_ollama import ChatOllama

chat = ChatOllama(model="qwen3:8b")

parser = StrOutputParser()

chat_msg = [
    ("system", "你是一个ai assistant，严格执行用户提出的要求"),
    ("human", "我领居姓：{lastName}，生了个{gender}，帮我邻居给孩子起个名字，仅仅告诉我名字，不要额外信息")
]

chatPrompt = ChatPromptTemplate.from_messages(
    [
        ("system", "你是一个ai assistant，严格执行用户提出的要求"),
        ("human", "我领居姓：{lastName}，生了个{gender}，帮我邻居给孩子起个名字，仅仅告诉我名字，不要额外信息")
    ]
)

chat_func = RunnableLambda(lambda msg: chatPrompt.invoke(input=msg))




custom_func = RunnableLambda(lambda ai_msg: f"你为什么取名{ai_msg.content}呢？")

chain = chat_func | chat | custom_func | chat | parser

for res in chain.stream({"lastName": "杨", "gender": "男孩"}):
    if res is not None and res != "":
        print(res, end="", flush=True)

