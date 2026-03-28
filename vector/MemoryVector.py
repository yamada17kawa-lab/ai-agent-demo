from langchain_community.vectorstores import InMemoryVectorStore
from langchain_ollama import OllamaEmbeddings
from loader.TestTextLoader import TestLoader2

store = InMemoryVectorStore(embedding=OllamaEmbeddings(model="qwen3-embedding:4b"))

documents = TestLoader2.loading()
print(len(documents)+1)
store.add_documents(
    documents=documents,
    ids=["id"+str(i) for i in range(1, len(documents) + 1)],
)

store.delete(ids=["id1", "id2", "id3"])

result = store.similarity_search("雪が降り積もる", 3)
for item in result:
    print(item.page_content)