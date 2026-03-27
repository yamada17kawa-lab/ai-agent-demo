from langchain_community.document_loaders import CSVLoader

loader = CSVLoader(
    file_path=r'..\student.csv',
    csv_args={
        "delimiter": ",",
        "quotechar": '"',
        "fieldnames": ['name','age','gender','hobby']
    },
    encoding="utf-8"
)

for d in loader.lazy_load():
    print(d,flush=True)


