import urllib

from langchain_ollama import OllamaEmbeddings
from langchain_postgres import PGVector
from loader.TestTextLoader import TestLoader2

embedding = OllamaEmbeddings(model="qwen3-embedding:4b")



connection = f"postgresql+psycopg://postgres:123456@localhost:5432/postgres"

COLLECTION_NAME = "my_ai_knowledge"


vector_store = PGVector.from_documents(
    embedding=embedding, # 向量模型
    connection=connection, # 连接的库
    collection_name=COLLECTION_NAME, # 自定义的知识库名
    documents=TestLoader2.loading(), # 存储的document
    use_jsonb=True,  # 开启使用元数据检索，检索更快
)

result = vector_store.similarity_search("记忆", 2)
print(result)

