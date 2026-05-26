from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("YOUR_OPENAI_API_KEY")
)


def generate_budget_advice(dataframe):
    """
    Generate AI budgeting advice.
    """

    if dataframe.empty:
        return "No spending data available yet."

    category_summary = dataframe.groupby("category")["amount"].sum().to_dict()

    prompt = f"""
    You are a financial advisor for students.

    Analyze this spending data:
    {category_summary}

    Give:
    - 3 saving tips
    - 2 spending warnings
    - 1 weekly budget suggestion

    Keep it simple and practical.
    """

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=prompt
    )

    return response.output_text