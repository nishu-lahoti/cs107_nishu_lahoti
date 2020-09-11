#!/bin/bash

echo "Please choose a file to commit."
read FILE -r -p
git add $FILE
git status

echo -n "Do you wish to continue? (Y/N)"
read -r RESPONSE

if [ "$RESPONSE"="Y" ]; then
    echo -n "Please enter a commit message: "
    read -r COMM
    git commit -m "$COMM"
    git status

    echo -n "Do you wish to continue? (Y/N) "
    read -r  ANSWER
    if [ "$ANSWER"="Y" ]; then
        git push
    else
	exit 1
    fi
else
    exit 1
fi
