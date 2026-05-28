import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def generate_advice(summary):
    """
    Generate budgeting advice using Groq AI (FREE).
    """

    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful financial advisor for students."
                },
                {
                    "role": "user",
                    "content": f"""
Analyze this student spending data:

{summary}

Give:
- short summary
- 3 saving tips
- 1 warning
"""
                }
            ]
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"Error: {str(e)}"