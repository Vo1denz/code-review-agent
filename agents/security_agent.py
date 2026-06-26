import os
from dotenv import load_dotenv

from langchain_groq import ChatGroq

from models.schemas import PRReview, ReviewItem
from models.schemas import Severity, Category


load_dotenv()

class SecurityAgent:

    def __init__(self):

        self.model = ChatGroq(
            model="llama-3.3-70b-versatile",
            api_key=os.getenv("GROQ_API_KEY"),
            temperature=0  #less random and more deterministic 
        )

        self.structured_model = self.model.with_structured_output(PRReview)