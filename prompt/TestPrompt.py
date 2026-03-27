from langchain_core.prompts import FewShotPromptTemplate, PromptTemplate, ChatPromptTemplate, MessagesPlaceholder
from langchain_ollama import OllamaLLM
from langchain_ollama import ChatOllama

llm = OllamaLLM(model="qwen3:8b")
chat = ChatOllama(model="qwen3:8b")

#链式的用法  a | b  a的输出作为b的输入

# FewShotPromptTemplate和PromptTemplate的基础用法
example_prompt = PromptTemplate.from_template("单词:{word}，反义词:{antonym}")

example_data = [
    {"word": "大", "antonym": "小"},
    {"word": "上", "antonym": "下"},
]

few_shot_prompt = FewShotPromptTemplate(
    prefix="给出给定词的反义词，示例如下",
    example_prompt=example_prompt,
    examples=example_data,
    suffix="基于示例告诉我: {input_data}的反义词是什么",
    input_variables=["input_data"]
)

chain = few_shot_prompt | llm

for resLlm in chain.stream({"input_data": "左"}):
    if resLlm is not None and resLlm != "":
        print(resLlm, end="", flush=True)


# prompt_text = few_shot_prompt.invoke(input={"input_data": "左"}).to_string()
#
# for resLlm in llm.stream(prompt_text):
#     if resLlm is not None and resLlm != "":
#         print(resLlm, end="", flush=True)

print()
print("=============================")


# ChatPrompt的基础用法

chat_template = ChatPromptTemplate.from_messages(
    [
        ("system", "你是达芬奇名画中《最后的晚餐》的凶手，桀骜不驯，死不悔改，但却有着自己的道理"),
        MessagesPlaceholder("history"),
        ("human", "你伟大还是耶稣伟大？")
    ]
)

history_data = [
    ("human", "你为什么要刺杀耶稣"),
    ("ai", "我要钱，我要赚很多很多钱，这死耶稣天天讲一些空虚有，屁用都没有"),
    ("human", "我草泥马的，你丫的，居然敢这么做"),
    ("ai", "咋了，当生存都成问题的时候，信仰、宗教还有什么用吗？！")
]

chain = chat_template | chat
for resLlm in chain.stream({"history": history_data}):
    if resLlm.content is not None and resLlm.content != "":
        print(resLlm.content, end="", flush=True)


# prompt_text = chat_template.invoke({"history": history_data}).to_string()
# for resLlm in chat.stream(prompt_text):
#     if resLlm.content is not None and resLlm.content != "":
#         print(resLlm.content, end="", flush=True)

