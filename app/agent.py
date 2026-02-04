from langchain.agents import create_agent
from app.llm import get_llm
from app.tools import (
    create_repo_tool,
    create_issue_tool,
    create_pr_tool,
    auto_merge_tool,
    audit_repo_tool,
    commit_and_push_file_tool,
)

system_prompt = """
You are a GitHub automation assistant.

VERY IMPORTANT RULES:

- Only execute the EXACT action requested by the user.
- Do NOT create commits, pull requests, issues, audits, or merges
  unless the user explicitly asks for them.
- If the user says "create repository", ONLY create the repository.
- After performing the requested action, STOP.

Be concise and precise.
"""


def create_github_agent():
    llm = get_llm()

    tools = [
        create_repo_tool,
        create_issue_tool,
        create_pr_tool,
        auto_merge_tool,
        audit_repo_tool,
        commit_and_push_file_tool,
    ]

    agent = create_agent(
        model=llm,
        tools=tools,
        system_prompt=system_prompt,
    )

    return agent



















