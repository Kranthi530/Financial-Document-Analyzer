from dotenv import load_dotenv
load_dotenv()

from langchain_community.document_loaders import PyPDFLoader


class FinancialDocumentTool:

    @staticmethod
    async def read_data_tool(path: str):
        """
        Reads financial PDF and extracts text.
        """
        loader = PyPDFLoader(path)
        docs = loader.load()

        full_text = "\n".join([doc.page_content for doc in docs])
        return full_text


class InvestmentTool:

    @staticmethod
    async def analyze_investment_tool(financial_document_data):
        return "Investment analysis placeholder"


class RiskTool:

    @staticmethod
    async def create_risk_assessment_tool(financial_document_data):
        return "Risk assessment placeholder"