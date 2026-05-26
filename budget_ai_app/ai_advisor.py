from openai import OpenAI

client = OpenAI(
    api_key="YOUR_OPENAI_API_KEY"
)


def generate_budget_advice(dataframe):
    """
    Generate AI budgeting advice.
    """

    category_summary = dataframe.groupby(
        "category"
    )["amount"].sum().to_dict()

    prompt = f"""
    Analyze this student spending data:

    {category_summary}

    Give budgeting advice in simple bullet points.
    """

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    advice = response.choices[0].message.content

    return advice