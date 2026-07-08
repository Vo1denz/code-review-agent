import os
import requests
from dotenv import load_dotenv

load_dotenv()


class CommentPoster:

    def __init__(self):
        self.token = os.getenv("GITHUB_TOKEN")

        self.headers = {
            "Authorization": f"Bearer {self.token}",
            "Accept": "application/vnd.github+json"
        }

    def post_comment(
        self,
        owner: str,
        repo: str,
        pr_number: int,
        markdown: str
    ):

        url = f"https://api.github.com/repos/{owner}/{repo}/issues/{pr_number}/comments"

        response = requests.post(
            url,
            headers=self.headers,
            json={
                "body": markdown
            }
        )

        if response.status_code != 201:
            raise Exception("Failed to post comment")

        return response.json()