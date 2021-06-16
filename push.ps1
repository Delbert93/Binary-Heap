git add .
git status
$commit_message = Read-Host -Prompt "Enter commit message"
$commit_message
git commit -m $commit_message
git push