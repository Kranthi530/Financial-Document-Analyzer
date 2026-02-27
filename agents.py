import os
from dotenv import load_dotenv
load_dotenv()

from crewai import Agent
from langchain_openai import ChatOpenAI

# Load API key
api_key = os.getenv("OPENAI_API_KEY")

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.2,
    api_key=api_key
)

financial_analyst = Agent(
    role="Financial Analyst",
    goal="Analyze financial documents and provide structured insights.",
    backstory="Experienced financial analyst with strong analytical skills.",
    llm=llm,
    verbose=True
)