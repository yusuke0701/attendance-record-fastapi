import requests

import streamlit as st

st.title("TODOアプリ")

st.header("ヘッダー")
st.subheader("サブヘッダー")

tasks = requests.get("http://localhost:8000/tasks")
st.write(tasks.json())

with st.form("タスク作成", clear_on_submit=True):
    title = st.text_input("タイトル")
    create_submitted = st.form_submit_button("タスク作成")

if create_submitted:
    with st.spinner("タスクを作成中"):
        response = requests.post("http://localhost:8000/tasks", json={"title": title})
    st.rerun()

with st.form("タスク更新", clear_on_submit=True):
    task_id = st.text_input("タスクID")
    title = st.text_input("タイトル")
    update_submitted = st.form_submit_button("タスク更新")

if update_submitted:
    with st.spinner("タスクを更新中"):
        response = requests.put(
            "http://localhost:8000/tasks/" + task_id, json={"title": title}
        )
    st.rerun()

with st.form("タスク削除", clear_on_submit=True):
    task_id = st.text_input("タスクID")
    delete_submitted = st.form_submit_button("タスク削除")

if delete_submitted:
    with st.spinner("タスクを削除中"):
        response = requests.delete("http://localhost:8000/tasks/" + task_id)
    st.rerun()
