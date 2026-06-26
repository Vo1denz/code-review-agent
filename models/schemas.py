from enum import Enum
from pydantic import BaseModel
from typing import List

class Severity(str, Enum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"
    CRITICAL = "CRITICAL"


class Category(str, Enum):
    SECURITY = "SECURITY"
    CODE_QUALITY = "CODE_QUALITY"
    TEST_COVERAGE = "TEST_COVERAGE"


class ReviewItem(BaseModel):
        issue: str
        recommendation: str
        file_name: str
        line_number: int
        severity : Severity
        category : Category

class FileSummary(BaseModel):
        file_path : str
        total_issues : int
        high_severity : int
        medium_severity : int
        low_severity : int


class PRReview(BaseModel):
     items : list[ReviewItem]
     total_files : int
     total_issues : int
     summary : str
     file_summaries : list[FileSummary]