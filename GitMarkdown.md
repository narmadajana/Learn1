# GitHub Markdown 

## What is Git?
Git is the free and open source distributed version control system that's responsible for everything GitHub related that happens locally on your computer.
The Command Line Interface used in Git is called Git bash.
## What is GitHub?
GitHub is a web-based platform that allows developers to store, share, and collaborate on code.

## What GitHub is used for?
- Storing code: Developers can store their code in a repository on GitHub. 
- Sharing code: Developers can share their work with others. 
- Collaborating: Developers can work together on projects without worrying about their changes - impacting others' work. 
- Managing projects: Developers can manage projects, share progress, and collaborate on open-source projects. 
- Tracking changes: Developers can track and manage changes to their code over time. 
- Reviewing code: Developers can let others review their code and make suggestions to improve it. - Bug tracking: Developers can track bugs and request new software features. 
- Task management: Developers can manage tasks and use wikis for each project.

## SOME GIT COMMANDS
- git init	Initialize a local Git repository
-git clone ssh://git@github.com/[username]/[repository-name].git	Create a local copy of a remote repository

Basic Snapshotting
- git status	Check status
- git add [file-name.txt]	Add a file to the staging area
- git add -A	Add all new and changed files to the staging area
- git commit -m "[commit message]"	Commit changes
- git rm -r [file-name.txt]	Remove a file (or folder)
- git remote -v	View the remote repository of the currently working file or directory

Branching & Merging
- git branch	List branches (the asterisk denotes the current branch)
- git branch -a	List all branches (local and remote)
- git branch [branch name]	Create a new branch
- git branch -d [branch name]	Delete a branch
- git branch -m [old branch name] [new branch name]	Rename a local branch
- git push origin --delete [branch name]	Delete a remote branch
- git checkout -b [branch name]	Create a new branch and switch to it
- git checkout -b [branch name] origin/[branch name]	Clone a remote branch and switch to it
- git checkout [branch name]	Switch to a branch
- git checkout -	Switch to the branch last checked out
- git checkout -- [file-name.txt]	Discard changes to a file
- git merge [branch name]	Merge a branch into the active branch
- git merge [source branch] [target branch]	Merge a branch into a target branch
- git stash	Stash changes in a dirty working directory
- git stash clear	Remove all stashed entries
- git stash pop	Apply latest stash to working directory

Sharing & Updating Projects
- git push origin [branch name]	Push a branch to your remote repository
- git push -u origin [branch name]	Push changes to remote repository (and remember the branch)
- git push	Push changes to remote repository (remembered branch)
- git push origin --delete [branch name]	Delete a remote branch
- git pull	Update local repository to the newest commit
- git pull origin [branch name]	Pull changes from remote repository
- git remote add origin ssh://git@github.com/[username]/[repository-name].git	Add a remote repository
- git remote set-url origin ssh://git@github.com/[username]/[repository-name].git	Set a repository's origin branch to SSH

Inspection & Comparison
- git log	View changes
- git log --summary	View changes (detailed)
- git log --oneline	View changes (briefly)
- git diff [source branch] [target branch]	Preview changes before merging










