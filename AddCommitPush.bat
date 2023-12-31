
#!/bin/bash
# by: RAFAL
# Date: 25NOV23
# Function: Perform a commit
# Script: AddCommitPush.bat

@echo off
cls
git status

echo **************************************************
echo Performing an add for all files in this directory
git add .
git status

echo **************************************************
set /p CommitMessage="Enter the commit message: "
git commit -m "%CommitMessage%"
git status

echo **************************************************
echo Pushing to GITHUB repository
git push -u origin master
echo **************************************************

echo Done!
