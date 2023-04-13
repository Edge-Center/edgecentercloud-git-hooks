from hooks.commit_msg import is_conventional

import pytest


@pytest.mark.parametrize(
    "commit_message",
    [
        "feat(CLOUD-123): Add button to UI components",
        "fix(CLOUD-123): Corrected the return value type",
        "docs(CLOUD-123): add the testing process in `README.md`",
        "style(CLOUD-123): run black on the project files",
        "refactor(CLOUD-123): Simplify the `is_correct_image` function",
        "test(CLOUD-123): add tests for `is_correct_image` function",
        "chore(CLOUD-123): Add input scheme for `/statistics` endpoint",
        "build(CLOUD-123): make `Dockerfile` for a custom MariaDB image",
    ],
)
def test__valid_cloud_type(commit_message: str):
    assert is_conventional(commit_message=commit_message)


@pytest.mark.parametrize(
    "commit_message",
    [
        "fix(CLOUD-125): maintain separate unit, integration and e2e tests",
        "fix(CLOUD-346): Change `external_network_id` in `README.md`",
        "refactor(CLOUD-328): Remove all G-Core developments",
        "chore(CLOUD-328)!: Change the `StatisticsFilter` scheme for correct display in swagger",
        "test(CLOUD-328): Tests use only the test configuration from `src/tests/configs/`",
    ],
)
def test__minimal_valid_commit(commit_message: str):
    assert is_conventional(commit_message=commit_message)


@pytest.mark.parametrize(
    "commit_message",
    [
        (
            "feat(CLOUD-328): First projects drafts\n"
            "\n"
            "- Create project hierarchy\n"
            "- Add `sqlalchemy` models, session class and query service\n"
            "- Add configuration schema and its validation\n"
            "- Create the `GlobalDependency` class\n"
            "- Add `fastapi` schemas and routers\n"
            "- Create entry point for app\n"
            "- Prepare repository for development (git hooks, Makefile, poetry and etc)\n"
        ),
        (
            "refactor(CLOUD-223)!: sync ProjectSetup even if there are errors syncing network rbac rules\n"
            "\n"
            'if we don\'t sync a ProjectSetup, each call of "ensure_shared_networks_synchronized" will cause a try \n'
            "to sync failed rules.\n"
            "\n"
            "we don't need to sync it on each call, because when a user next time will change shared networks, \n"
            "the sync try will be performed anyway.\n"
        ),
        (
            "fix(CLOUD-125): Fix tests\n"
            "\n"
            "Rewrite `test_worker_probe` for not using AmqpTaskRunner connect, connections and resources release \n"
            "after ending test\n"
        ),
    ],
)
def test__detailed_valid_commit(commit_message: str):
    assert is_conventional(commit_message=commit_message)


@pytest.mark.parametrize(
    "commit_message",
    [
        "feature(CLOUD-123): Add button to UI components",
        "fixing(CLOUD-123): Corrected the return value type",
        "documentation(CLOUD-123): add the testing process in `README.md`",
        "styling(CLOUD-123): run black on the project files",
        "refactoring(CLOUD-123): Simplify the `is_correct_image` function",
        "testing(CLOUD-123): add tests for `is_correct_image` function",
        "building(CLOUD-123): make `Dockerfile` for a custom MariaDB image",
    ],
)
def test__invalid_cloud_type(commit_message: str):
    assert not is_conventional(commit_message=commit_message)


@pytest.mark.parametrize(
    "commit_message",
    [
        "CLOUD-125): maintain separate unit, integration and e2e tests",
        "(CLOUD-346): Change `external_network_id` in `README.md`",
        "(CLOUD-328): Remove all G-Core developments",
        "(CLOUD-328)!: Change the `StatisticsFilter` scheme for correct display in swagger",
        "(CLOUD-328): Tests use only the test configuration from `src/tests/configs/`",
    ],
)
def test__without_type(commit_message: str):
    assert not is_conventional(commit_message=commit_message)


@pytest.mark.parametrize(
    "commit_message",
    [
        "fix: maintain separate unit, integration and e2e tests",
        "fix: Change `external_network_id` in `README.md`",
        "refactor: Remove all G-Core developments",
        "chore!: Change the `StatisticsFilter` scheme for correct display in swagger",
        "test: Tests use only the test configuration from `src/tests/configs/`",
    ],
)
def test__without_task_tag(commit_message: str):
    assert not is_conventional(commit_message=commit_message)


@pytest.mark.parametrize(
    "commit_message",
    [
        "fix(CLOUD-125) maintain separate unit, integration and e2e tests",
        "fix(CLOUD-346) Change `external_network_id` in `README.md`",
        "refactor(CLOUD-328) Remove all G-Core developments",
        "chore(CLOUD-328) Change the `StatisticsFilter` scheme for correct display in swagger",
        "test(CLOUD-328) Tests use only the test configuration from `src/tests/configs/`",
    ],
)
def test__without_delimiter(commit_message: str):
    assert not is_conventional(commit_message=commit_message)


@pytest.mark.parametrize(
    "commit_message",
    [
        "fix(CLOUD-125):",
        "fix(CLOUD-346):",
        "refactor(CLOUD-328):",
        "chore(CLOUD-328)!:",
        "test(CLOUD-328):",
    ],
)
def test__without_description(commit_message: str):
    assert not is_conventional(commit_message=commit_message)


@pytest.mark.parametrize(
    "commit_message",
    [
        "fix: maintain separate unit, integration and e2e tests",
        "fix(CLOUD-346) Change `external_network_id` in `README.md`",
        "refactor(CLOUD): Remove all G-Core developments",
        "chore(CLOUD-328):! Change the `StatisticsFilter` scheme for correct display in swagger",
        "Tests use only the test configuration from `src/tests/configs/`",
        (
            "fix(CLOUD-125): Fix tests\n"
            "Rewrite `test_worker_probe` for not using AmqpTaskRunner connect, connections and resources release \n"
            "after ending test\n"
        ),
    ],
)
def test__invalid_commit(commit_message: str):
    assert not is_conventional(commit_message=commit_message)
