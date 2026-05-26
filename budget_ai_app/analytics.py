import plotly.express as px


def generate_expense_pie_chart(dataframe):
    """
    Generate expense category pie chart.
    """

    expense_dataframe = dataframe[
        dataframe["transaction_type"] == "Expense"
    ]

    figure = px.pie(
        expense_dataframe,
        names="category",
        values="amount",
        title="Expense Distribution"
    )

    return figure


def calculate_summary(dataframe):
    """
    Generate total income and expense summary.
    """

    total_income = dataframe[
        dataframe["transaction_type"] == "Income"
    ]["amount"].sum()

    total_expense = dataframe[
        dataframe["transaction_type"] == "Expense"
    ]["amount"].sum()

    balance = total_income - total_expense

    return {
        "income": total_income,
        "expense": total_expense,
        "balance": balance
    }