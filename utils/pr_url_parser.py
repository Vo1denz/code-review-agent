class PRUrlParser:

    def parse(self, url: str):
        parts = url.rstrip("/").split("/")

        if len(parts) < 7 or parts[2] != "github.com" or parts[5] != "pull":
            raise ValueError("Invalid GitHub PR URL")

        owner = parts[3]
        repo = parts[4]

        try:
            pr_number = int(parts[6])
        except ValueError:
            raise ValueError("Invalid GitHub PR number")

        return (
            owner,
            repo,
            pr_number
        )
