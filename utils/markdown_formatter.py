from models.schemas import Category, PRReview


class MarkdownFormatter:

    def format(self, review: PRReview) -> str:
        security = []
        quality = []
        tests = []
      
        for item in review.items:
            if item.category == Category.SECURITY:
                security.append(item)

            elif item.category == Category.CODE_QUALITY:
                 quality.append(item)

            else:
                tests.append(item)
        
        markdown = "# GitHub PR Review\n\n"

        if security:
             markdown += "## Security\n\n"
             for item in security:
                markdown += f"""
                - **Issue:** {item.issue}
                - **Severity:** {item.severity.value}
                - **File:** {item.file_name}:{item.line_number}
                - **Recommendation:** {item.recommendation}

                """
        if quality:
            markdown += "## Code Quality\n\n"
            for item in quality:
                markdown += f"""
            - **Issue:** {item.issue}
            - **Severity:** {item.severity.value}
            - **File:** {item.file_name}:{item.line_number}
            - **Recommendation:** {item.recommendation}

            """
        if tests:
             markdown += "## Test Coverage\n\n"  
            for item in tests:
                markdown += f"""
            - **Issue:** {item.issue}
            - **Severity:** {item.severity.value}
            - **File:** {item.file_name}:{item.line_number}
            - **Recommendation:** {item.recommendation}

            """
                
        return markdown