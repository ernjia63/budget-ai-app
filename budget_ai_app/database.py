import sqlite3
import pandas as pd

DATABASE_NAME = "budget.db"


def initialize_database():
    """
    Create transactions table if it doesn't exist.
    """

    connection = sqlite3.connect(DATABASE_NAME)

    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS transactions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        transaction_type TEXT,
        category TEXT,
        amount REAL,
        description TEXT,
        transaction_date TEXT
    )
    """)

    connection.commit()
    connection.close()


def add_transaction(
    transaction_type,
    category,
    amount,
    description,
    transaction_date
):
    """
    Save a transaction into database.
    """

    connection = sqlite3.connect(DATABASE_NAME)

    cursor = connection.cursor()

    cursor.execute("""
    INSERT INTO transactions
    (
        transaction_type,
        category,
        amount,
        description,
        transaction_date
    )
    VALUES (?, ?, ?, ?, ?)
    """, (
        transaction_type,
        category,
        amount,
        description,
        transaction_date
    ))

    connection.commit()
    connection.close()


def get_all_transactions():
    """
    Return all transactions as dataframe.
    """

    connection = sqlite3.connect(DATABASE_NAME)

    dataframe = pd.read_sql_query(
        "SELECT * FROM transactions",
        connection
    )

    connection.close()

    return dataframe