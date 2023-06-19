# EdgeCenter Cloud Git hooks

### 1. `commit-msg` hook

The commit-msg hook takes one parameter, which again is the path to a temporary file that contains the commit message
written by the developer. If this script exits non-zero, Git aborts the commit process.

This git hook, developed by the Cloud team, checks the commit message for compliance with the `Conventional Commits`
format _(see  https://www.conventionalcommits.org)_

#### How to implement it into your project?

Install `pre-commit` tools:

```shell
pip install pre-commit
```

Create (if it doesn't exist) a `.pre-commit-config.yaml` file in the root of the project:

```shell
touch .pre-commit-config.yaml
```

Add this content to the created file:

```shell
  - repo: https://github.com/Edge-Center/edgecentercloud-git-hooks
    rev: v0.0.6
    hooks:
      - id: edgecenter-cloud-conventional-commit
        name: EdgeCenter Cloud Conventional Commit
        entry: edgecenter-cloud-conventional-commit
        language: python
        always_run: true
        stages: [ commit-msg ]
```

Install hook using this command:

```shell
pre-commit install --install-hooks
```

Complete!