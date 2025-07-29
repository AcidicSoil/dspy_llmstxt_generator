#!/bin/bash

if [ -n "$1" ]; then
  COMMIT_MESSAGE="$1"
else
  read -p "Enter commit message: " COMMIT_MESSAGE
fi

git add .
git commit -m "$COMMIT_MESSAGE"
git push