import argparse

from utils.pr_url_parser import PRUrlParser
from tools.github_fetcher import GitHubFetcher
from tools.diff_parser import DiffParser

from agents.orchestrator import Orchestrator

from utils.markdown_formatter import MarkdownFormatter
from tools.comment_poster import CommentPoster


def main():

    parser = argparse.ArgumentParser(
        description="GitHub PR Review Agent"
    )

    parser.add_argument(
        "--pr",
        required=True,
        help="GitHub Pull Request URL"
    )

    args = parser.parse_args()

    # -----------------------------
    # Parse PR URL
    # -----------------------------
    url_parser = PRUrlParser()

    owner, repo, pr_number = url_parser.parse(args.pr)

    # -----------------------------
    # Fetch PR
    # -----------------------------
    github = GitHubFetcher()

    pr_data = github.fetch_pr(
        owner,
        repo,
        pr_number
    )

    # -----------------------------
    # Parse Diff
    # -----------------------------
    diff_parser = DiffParser()

    parsed_files = diff_parser.parse(
        pr_data["diff"]
    )

    # -----------------------------
    # Review PR
    # -----------------------------
    orchestrator = Orchestrator()

    review = orchestrator.review(
        parsed_files
    )

    # -----------------------------
    # Format Markdown
    # -----------------------------
    formatter = MarkdownFormatter()

    markdown = formatter.format(review)

    # -----------------------------
    # Post Comment
    # -----------------------------
    poster = CommentPoster()

    poster.post_comment(
        owner,
        repo,
        pr_number,
        markdown
    )

    print("✅ Review posted successfully.")


if __name__ == "__main__":
    main()