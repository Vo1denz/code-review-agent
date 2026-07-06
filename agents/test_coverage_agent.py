import os
from dotenv import load_dotenv

from langchain_groq import ChatGroq

from models.schemas import PRReview


load_dotenv()


class TestCoverageAgent:

    def __init__(self):

        self.model = ChatGroq(
            model = "llama-3.3-70b-versatile",
            api_key = os.getenv("GROQ_API_KEY"),
            temperature=0
        )

        self.structured_model = self.model.with_structured_output(PRReview)
        
    def review(self, parsed_files):

        all_items = []

        for file in parsed_files:

            prompt = f"""
            You are a Senior Test Coverage Reviewer.

            Review ONLY the added lines of code.

            Use the removed lines only for context.

            Detect:
            -Missing unit tests
            -Missing edge case tests
            -Boundary condition coverage
            -Error and exception handling tests
            -Invalid input tests
            -Happy path vs failure path coverage
            -Missing integration tests (if applicable)
            -Untested new logic
            -Any other test coverage gaps

            
            Return ONLY valid structured output.

            File:
                {file["file_path"]}

                Added Lines:
                {file["added_lines"]}

                Removed Lines:
                {file["removed_lines"]}

            If the code is already well tested, return an empty PRReview.

            Every ReviewItem must have category = TEST_COVERAGE.
                """
            
            review = self.structured_model.invoke(prompt)

            all_items.extend(review.items)

        summary = f"Found {len(all_items)} test coverage issue(s)."

        return PRReview(
            items=all_items,
            total_files=len(parsed_files),
            total_issues=len(all_items),
            summary=summary,
            file_summaries=[]
            )

            