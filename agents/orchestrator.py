from langchain_core.runnables import RunnableParallel, RunnableLambda

from agents.security_agent import SecurityAgent
from agents.code_quality_agent import QualityAgent
from agents.test_coverage_agent import TestCoverageAgent

from models.schemas import PRReview


class Orchestrator:

    def __init__(self):

        self.security = SecurityAgent()
        self.quality = QualityAgent()
        self.tests = TestCoverageAgent()

        self.parallel = RunnableParallel(
            security=RunnableLambda(self.security.review),
            quality=RunnableLambda(self.quality.review),
            tests=RunnableLambda(self.tests.review),
        )

    def review(self, parsed_files):
        all_items = []
        results = self.parallel.invoke(parsed_files)
        all_items.extend(results["security"].items)
        all_items.extend(results["quality"].items)
        all_items.extend(results["tests"].items)
        summary = f"Found {len(all_items)} issue(s)."

        return PRReview(
            items=all_items,
            total_files=len(parsed_files),
            total_issues=len(all_items),
            summary=summary,
            file_summaries=[]
        )
            
        # easier approach for multiple lists
        # for review in results.values():
           # all_items.extend(review.items)

