from langchain.tools import tool
from app.github_tools import (
    create_repository,
    create_issue,
    create_pull_request,
    auto_merge_pr,
    audit_repository,
    commit_and_push_file,
)
"hello sir"

@tool
def create_repo_tool(
    name: str,
    description: str = "",
    private: bool = False,
) -> str:
    """Create a GitHub repository."""

    result = create_repository(
        name=name,
        description=description,
        private=private
    )

    return result



@tool
def create_issue_tool(repo: str, title: str, body: str) -> str:
    """Create a GitHub issue."""
    return str(create_issue(repo, title, body))


@tool
def create_pr_tool(
    repo: str,
    title: str,
    body: str,
    head: str,
    base: str = "main",
) -> str:
    """Create a pull request."""
    return str(create_pull_request(repo, title, body, head, base))


@tool
def auto_merge_tool(repo: str, pr_number: int, method: str = "squash") -> str:
    """Merge a pull request."""
    return str(auto_merge_pr(repo, pr_number, method))


@tool
def audit_repo_tool(repo: str) -> str:
    """Audit a GitHub repository."""
    return "\n".join(audit_repository(repo))


@tool
def commit_and_push_file_tool(
    repo: str,
    branch: str,
    file_path: str,
    commit_message: str,
) -> str:
    """Commit a LOCAL file to GitHub."""
    return str(
        commit_and_push_file(
            repo=repo,
            branch=branch,
            file_path=file_path,
            commit_message=commit_message,
        )
    )





