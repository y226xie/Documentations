## Some Basic Rules

1. Before you start to work on a feature of the application, please use `git checkout -b branchName` to create a branch (i.e. git checkout -b MOB-1)
2. Use `git push -u origin BranchName` to push your local branch into gitLab
3. After you finish your work, use `git status` to check what files you have modified.
4. Use `git add -A`  to add all files you would like to commit or use `git add filename` to add the specific files you want to commit
5. Use `git commit -m "BranchName commit message` to commit your changes, and the first letter of your commit message must be upper case, and do not add period for your commit message (i.e. git commit -m "MOB-1 Add the NavBar for the project")
5. Use `git push` to push your changes from local branch to remote branch in gitLab.
6. IMPORTANT: Before you merge, please rebase your branch with master!!
7. Use `git checkout master` and `git pull` to get whatever new changes from master
8. Then use `git checkout BranchName` (the branch you would like to merge master with). In this branch, use `git rebase -i master` to rebase your branch with master branch
9. Use `git push -f` to force push your branch to gitLab
10. Create a pull request in gitLab, please don't click `merge` button by yourself.
11. In the right top section, you will see something called `reviewer`, please select other team members rather than yourself. You are always required to ask other team member to view the changes with you together.

## Some Useful git command

1. `git stash` to save your local changes (consider it as `cut`)
2. `git stash pop` to let your changes show up (consider it as `paste`)
3. `git stash drop` would delete all your changes (consider it as select certain info then `delete` the info)

