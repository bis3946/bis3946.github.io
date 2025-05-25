#!/bin/bash

# Usage: ./git-auto.sh "Your commit message"
# If no commit message provided, uses a default with date/time.

MSG="$1"
if [ -z "$MSG" ]; then
  MSG="Auto-update: $(date '+%Y-%m-%d %H:%M:%S')"
fi

git add .
git commit -m "$MSG"
git push origin main

echo "✅ Code committed and pushed to GitHub!"
