# edgecentercloud-git-hooks

### 1. `commit-msg` hook

The commit-msg hook takes one parameter, which again is the path to a temporary file that contains the commit message
written by the developer. If this script exits non-zero, Git aborts the commit process.

This git hook, developed by the Cloud team, checks the commit message for compliance with the `Conventional Commits`
format _(see  https://www.conventionalcommits.org)_

#### How to implement it into your project?

In your project directory run this commands:

```shell
wget -q https://raw.githubusercontent.com/Edge-Center/edgecentercloud-git-hooks/main/hooks/commit_msg.py -O commit-msg
chmod +x commit-msg
mv commit-msg .git/hooks
```

**P.S:** You can insert this commands into your project `Makefile`. For example in the `init_git_hooks` section