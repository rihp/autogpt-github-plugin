import requests
from typing import Dict, Union

class GitHubRepo:
    def __init__(self, owner: str, repo: str):
        self.url = f"https://api.github.com/repos/{owner}/{repo}"

    def get_repo_info(self) -> Dict[str, Union[int, str]]:
        response = requests.get(self.url)
        response.raise_for_status()  # If the response was unsuccessful, raise an exception

        data = response.json()
        return {
            "name": data["name"],
            "stars": data["stargazers_count"],
            "forks": data["forks_count"],
            "issues": data["open_issues_count"]
        }

def autogpt_github_status():
    return GitHubRepo("significant-gravitas", "Auto-GPT").get_repo_info()