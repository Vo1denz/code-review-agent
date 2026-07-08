import os
from dotenv import load_dotenv

from langchain_groq import ChatGroq

from models.schemas import PRReview


load_dotenv()

class SecurityAgent:

    def __init__(self):

        self.model = ChatGroq(
            model="llama-3.3-70b-versatile",
            api_key=os.getenv("GROQ_API_KEY"),
            temperature=0  #less random and more deterministic 
        )

        self.structured_model = self.model.with_structured_output(PRReview)

    def review(self, parsed_files):

        all_items = []
            
        for file in parsed_files:

            prompt = f"""
            You are a Senior Security Code Reviewer.

            Review ONLY the added lines of code.

            Use the removed lines only for context.

            Detect:
            - Hardcoded secrets
            - SQL Injection
            - Command Injection
            - Path Traversal
            - Insecure Deserialization
            - Weak Authentication
            - Weak Cryptography
            - Any other security vulnerabilities

            Return ONLY valid structured output.

            File:
            {file["file_path"]}

            Added Lines:
            {file["added_lines"]}

            Removed Lines:
            {file["removed_lines"]}
            """

            review = self.structured_model.invoke(prompt)

            all_items.extend(review.items)

        summary = f"Found {len(all_items)} security issue(s)."

        return PRReview(
            items=all_items,
            total_files=len(parsed_files),
            total_issues=len(all_items),
            summary=summary,
            file_summaries=[]
        )
