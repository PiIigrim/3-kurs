#!/bin/bash

git add .
echo "Текст коммита: "
read commit_message
git commit -m "$commit_message"
git pull
git push origin main

read -p "Жмакни enter"