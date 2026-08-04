import os
import requests
from dotenv import load_dotenv

load_dotenv()


class CommentPoster:

    def __init__(self):
        self.token = os.getenv("GITHUB_TOKEN")

        if not self.token:
            raise ValueError("GITHUB_TOKEN is not set. Add it to your .env before posting comments.")

        self.headers = {
            "Authorization": f"Bearer {self.token}",
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28"
        }

    def _print_error(self, response):
        print(response.status_code)
        print(response.text)

        accepted_permissions = response.headers.get("X-Accepted-GitHub-Permissions")

        if accepted_permissions:
            print(f"X-Accepted-GitHub-Permissions: {accepted_permissions}")

    def post_comment(
        self,
        owner: str,
        repo: str,
        pr_number: int,
        markdown: str
    ):

        issue_comment_url = f"https://api.github.com/repos/{owner}/{repo}/issues/{pr_number}/comments"

        response = requests.post(
            issue_comment_url,
            headers=self.headers,
            json={
                "body": markdown
            },
            timeout=30
        )

        if response.status_code == 201:
            return response.json()

        if response.status_code != 403:
            self._print_error(response)
            raise Exception("Failed to post comment")

        review_url = f"https://api.github.com/repos/{owner}/{repo}/pulls/{pr_number}/reviews"

        review_response = requests.post(
            review_url,
            headers=self.headers,
            json={
                "body": markdown,
                "event": "COMMENT"
            },
            timeout=30
        )

        if review_response.status_code in (200, 201):
            return review_response.json()

        print("Issue comment endpoint failed:")
        self._print_error(response)
        print("Pull request review endpoint failed:")
        self._print_error(review_response)
        raise Exception("Failed to post comment")
