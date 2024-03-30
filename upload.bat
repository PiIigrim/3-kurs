@echo off
cd /d %~dp0
git add .
set /p commit_message="Введите текст коммита: "
git commit -m "%commit_message%"
git push origin master
pause