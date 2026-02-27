from crewai import Task
from agents import financial_analyst
from tools import FinancialDocumentTool

analyze_task = Task(
    description=(
        "Analyze the uploaded financial document and provide:\n"
        "1. Executive Summary\n"
        "2. Revenue & Profit Analysis\n"
        "3. Cash Flow Analysis\n"
        "4. Debt & Liability Review\n"
        "5. Key Financial Ratios (if available)\n"
        "6. Risk Assessment\n"
        "7. Investment Recommendation (Neutral & Balanced)\n\n"
        "Base all insights strictly on document content."
    ),
    expected_output=(
        "Provide a structured financial analysis report in clean markdown format "
        "with clear headings and bullet points."
    ),
    agent=financial_analyst,
    tools=[FinancialDocumentTool.read_data_tool],
    async_execution=False,
)