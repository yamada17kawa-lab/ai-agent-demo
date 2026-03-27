from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader(
    file_path='../求职简历.pdf',
)

page = 0
documents = loader.load()
for doc in documents:
    page += 1
    print(doc)
    print(f"============={page}==========")