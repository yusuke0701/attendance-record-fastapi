# 勤怠管理アプリをFastAPI+Streamlitで作ってみる

## 環境構築メモ

1. devcontainer の導入
   1. 構成ファイル
      1. コンテナイメージ
         1. Python 3
      2. 追加する機能
         1. poetry
2. `poetry init` の実行
3. `poetry config virtualenvs.in-project true --local` の実行
4. README.md の追加
5. 拡張機能の追加
   1. `ms-python.python`
   2. `ms-python.black-formatter`
   3. `yzhang.markdown-all-in-one`
6. vscode の設定ファイルを用意
   1. `mkdir .vscode` の実行
   2. `touch .vscode/settings.json` の実行
   3. `editor.formatOnSave` を有効にする
7. `poetry add fastapi`
8. `poetry add uvicorn`
9. `poetry add streamlit`

## プロジェクトの初回セットアップ

`poetry install --no-root`

`python ./migrate_db.py`

## ローカルサーバーの立ち上げ

### サーバー

`.venv/bin/uvicorn main:app --reload`

### クライアント

streamlit run client/app.py

## ディレクトリ構成

├── client streamlit で作成しているクライアント
├── cruds DB操作
├── models DBの型定義
├── routers APIのルーティングを定義
├── schemas APIのリクエスト・レスポンスの型定義
└── tests テストコード