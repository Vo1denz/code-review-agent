import os
import requests
from dotenv import load_dotenv

load_dotenv()

class GitHubFetcher:
    def __init__(self):
        self.token = os.getenv("GITHUB_TOKEN")

        self.headers = {
            "Authorization": f"Bearer {self.token}",
            "Accept" : "application/vnd.github+json"
        }

    def fetch_pr(self, owner: str, repo: str, pr_number: int):
        url = f"https://api.github.com/repos/{owner}/{repo}/pulls/{pr_number}"

        response = requests.get(
            url,
            headers=self.headers
        )

        if response.status_code != 200:
            raise Exception("Failed to fetch PR")

        diff_headers = {
            **self.headers,
            "Accept": "application/vnd.github.v3.diff"
        }

        diff_response = requests.get(
            url,
            headers=diff_headers
        )

        if diff_response.status_code != 200:
            raise Exception("Failed to fetch PR diff")

        return {
            "metadata": response.json(),
            "diff": diff_response.text
        }
