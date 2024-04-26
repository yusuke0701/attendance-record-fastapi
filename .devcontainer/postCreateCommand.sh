#!/bin/bash

sudo apt update && sudo apt upgrade -y

# neovim をインストール
# https://github.com/neovim/neovim/blob/master/INSTALL.md#linux
curl -LO https://github.com/neovim/neovim/releases/latest/download/nvim-linux64.tar.gz
sudo rm -rf /opt/nvim
sudo tar -C /opt -xzf nvim-linux64.tar.gz
rm nvim-linux64.tar.gz

# NvChad をインストール
# https://nvchad.com/docs/quickstart/install
mkdir ~/.config/nvim
git clone https://github.com/NvChad/NvChad ~/.config/nvim --depth 1
touch ~/.config/nvim/init.lua

# nvim-lspconfig をインストール
# https://github.com/neovim/nvim-lspconfig?tab=readme-ov-file#install
git clone https://github.com/neovim/nvim-lspconfig ~/.config/nvim/pack/nvim/start/nvim-lspconfig

# fish をインストール
# NOTE: postCreateCommand は devcontainer.json の "features" より先に呼ばれる。
# fish は "features" でインストールすることも可能だが、その場合は設定ファイルがまだないという状態になるので、ここでインストールする。
sudo apt install fish -y
mkdir -p ~/.config/fish
echo "set PATH /opt/nvim-linux64/bin $PATH" >> ~/.config/fish/config.fish

# npm をインストール
sudo apt install npm -y
sudo npm i -g n
sudo n lts
sudo apt purge nodejs npm -y

# pyright をインストール
sudo npm i -g pyright
echo "require'lspconfig'.pyright.setup{}" >> ~/.config/nvim/init.lua
