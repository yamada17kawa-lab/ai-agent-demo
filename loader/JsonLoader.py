from langchain_community.document_loaders import JSONLoader

loader1 = JSONLoader(
    file_path='..\singer.json',
    jq_schema=".[].name",
)

for doc in loader1.load():
    print(doc.page_content)

print("==========================")

loader2 = JSONLoader(
    file_path='..\singer2.json',
    jq_schema=".age",
    json_lines=True,
    text_content=False, # 抽取的.age内容不是字符串
)

for doc in loader2.load():
    print(doc.page_content)