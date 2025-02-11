#!/bin/bash

# Check if Git is initialized
if [ ! -d ".git" ]; then
    echo "Initializing a new Git repository..."
    git init
fi

# Add all project files to the staging area
echo "Adding all project files to staging..."
git add .

# Prompt the user for a commit message
echo "Enter a commit message: "
read commit_message

# Check if a commit message is provided
if [ -z "$commit_message" ]; then
    echo "No commit message provided. Using default message: 'Initial commit'"
    commit_message="Initial commit"
fi

# Commit the files
echo "Committing files with message: '$commit_message'..."
git commit -m "$commit_message"

# Optional: Check for a remote repository
echo "Do you want to push these changes to a remote repository? (y/n)"
read push_response

if [ "$push_response" == "y" ]; then
    echo "Enter the remote repository URL: "
    read remote_url
    git remote add origin "$remote_url"
    git branch -M main
    git push -u origin main
else
    echo "Skipping push to remote repository."
fi

echo "All files have been committed successfully!"

