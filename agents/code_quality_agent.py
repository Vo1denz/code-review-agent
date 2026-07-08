import os
from dotenv import load_dotenv

from langchain_groq import ChatGroq

from models.schemas import PRReview



load_dotenv()


class QualityAgent:

    def __init__(self):

        self.model = ChatGroq(
            model ="llama-3.3-70b-versatile",
            api_key = os.getenv("GROQ_API_KEY"),
            temperature = 0
        )

        self.structured_model = self.model.with_structured_output(PRReview)

    def review(self, parsed_files):

        all_items = []
        
        for file in parsed_files:

            prompt = f"""
            You are a Senior Code Quality Reviewer.

            Review ONLY the added lines of code.

            Use the removed lines only for context.

            Detect:
            - Code smells
            - Duplicate code
            - Unused variables, imports, and functions
            - Dead or unreachable code
            - Poor naming conventions
            - Long or overly complex functions
            - High cyclomatic complexity
            - Deeply nested logic
            - Violations of SOLID principles
            - Poor error handling
            - Missing input validation
            - Inefficient algorithms or data structures
            - Performance bottlenecks
            - Resource leaks (files, sockets, database connections)
            - Inconsistent coding style
            - Missing or inadequate documentation/docstrings
            - Poor modularization and code organization
            - Maintainability and readability issues
            - Any other code quality issues or best practice violations

            Return ONLY valid structured output.

               

            File:
            {file["file_path"]}

            Added Lines:
            {file["added_lines"]}

            Removed Lines:
            {file["removed_lines"]}

            Every ReviewItem must have category = CODE_QUALITY.
            """

            review = self.structured_model.invoke(prompt)

            all_items.extend(review.items)

        summary = f"Found {len(all_items)} quality issue(s)."

        return PRReview(
            items=all_items,
            total_files=len(parsed_files),
            total_issues=len(all_items),
            summary=summary,
            file_summaries=[]
        )
