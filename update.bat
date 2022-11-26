@echo off

git pull

git add *
git status
set /p msg=Enter commit message:

git commit -am "%msg%"
git push
