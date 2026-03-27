from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

loader = TextLoader(
    file_path=f'..\\ttt.txt',
    encoding='utf-8',
)

# for doc in loader.load():
#     print(doc.page_content)
#
# print(len(loader.load()))

splitter = RecursiveCharacterTextSplitter(
    chunk_size=10,
    chunk_overlap=3,
    separators=["\r\n", "\n", " ", ".", "。", "，", "?", "!", "？", ""],
    length_function=len
)

split_doc = splitter.split_documents(loader.load())
for doc in split_doc:
    print(doc)