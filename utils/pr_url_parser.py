

class PRUrlParser:

    def parse(self, url: str):

         if len(parts) < 7 or parts[5] != "pull":
             raise ValueError("Invalid GitHub PR URL")   

        parts = url.split("/")
        owner = parts[3]
        repo = parts[4]
        pr_number = int(parts[6])


        return (
            owner,
            repo,
            pr_number
        )