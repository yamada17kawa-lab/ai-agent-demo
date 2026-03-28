from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter


class TestLoader2:

    @staticmethod
    def loading():
        loader = TextLoader(
            file_path=r'..\ttt.txt',
            encoding='utf-8',
        )

        splitter = RecursiveCharacterTextSplitter(
            chunk_size=20,
            chunk_overlap=5,
            separators=["\r\n", "\n", " ", ".", "。", "，", "?", "!", "？", ""],
            length_function=len
        )

        # 加载并切割文档
        docs = loader.load()
        split_docs = splitter.split_documents(docs)

        return split_docs