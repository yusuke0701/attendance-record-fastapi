import requests

import streamlit as st

st.title("TODOアプリ")

page = st.sidebar.radio(
    "ページ選択", ["タスク一覧", "タスク作成", "タスク更新", "タスク削除"]
)

if page == "タスク一覧":
    st.header("タスク一覧")
    tasks = requests.get("http://localhost:8000/tasks")
    st.write(tasks.json())

if page == "タスク作成":
    st.header("タスク作成")
    with st.form("タスク作成", clear_on_submit=True):
        title = st.text_input("タイトル")
        create_submitted = st.form_submit_button("タスク作成")

    if create_submitted:
        with st.spinner("タスクを作成中"):
            response = requests.post(
                "http://localhost:8000/tasks", json={"title": title}
            )
        page = "タスク一覧"

if page == "タスク更新":
    st.header("タスク更新")
    with st.form("タスク更新", clear_on_submit=True):
        task_id = st.text_input("タスクID")
        title = st.text_input("タイトル")
        update_submitted = st.form_submit_button("タスク更新")

    if update_submitted:
        with st.spinner("タスクを更新中"):
            response = requests.put(
                "http://localhost:8000/tasks/" + task_id, json={"title": title}
            )
        page = "タスク一覧"

if page == "タスク削除":
    st.header("タスク削除")
    with st.form("タスク削除", clear_on_submit=True):
        task_id = st.text_input("タスクID")
        delete_submitted = st.form_submit_button("タスク削除")

    if delete_submitted:
        with st.spinner("タスクを削除中"):
            response = requests.delete("http://localhost:8000/tasks/" + task_id)
        page = "タスク一覧"
