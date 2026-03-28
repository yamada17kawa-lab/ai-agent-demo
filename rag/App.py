import streamlit as st

st.title("上传文件")

file = st.file_uploader(
    "上传文件",
    type=["txt"],
    accept_multiple_files=False,
)

if file is not None:
    fname = file.name
    ftype = file.type
    fsize = file.size / 1024

    st.subheader(fname)
    st.write(f"类型: {ftype}, 大小: {fsize: .2f} KB")

    naiyou = file.getvalue().decode("utf-8")
    st.write("内容: " + naiyou)
