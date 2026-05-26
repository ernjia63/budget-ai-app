import streamlit as st
from PIL import Image

from database import *
from receipt_ai import *
from analytics import *
from ai_advisor import *
from jobs import *

# ---------------------------------------------------
# INITIALIZATION
# ---------------------------------------------------

initialize_database()

st.set_page_config(
    page_title="Budget AI App",
    layout="wide"
)

st.title("💰 Budget AI App")

# ---------------------------------------------------
# SIDEBAR MENU
# ---------------------------------------------------

menu = st.sidebar.selectbox(
    "Select Feature",
    [
        "Add Transaction",
        "Receipt Scanner",
        "Dashboard",
        "AI Advice",
        "Student Jobs"
    ]
)

# ---------------------------------------------------
# ADD TRANSACTION
# ---------------------------------------------------

if menu == "Add Transaction":

    st.header("Add Income / Expense")

    transaction_type = st.selectbox(
        "Transaction Type",
        ["Income", "Expense"]
    )

    category = st.text_input("Category")

    amount = st.number_input(
        "Amount",
        min_value=0.0
    )

    description = st.text_input(
        "Description"
    )

    transaction_date = st.date_input(
        "Date"
    )

    if st.button("Save Transaction"):

        add_transaction(
            transaction_type,
            category,
            amount,
            description,
            str(transaction_date)
        )

        st.success(
            "Transaction saved successfully!"
        )

# ---------------------------------------------------
# RECEIPT SCANNER
# ---------------------------------------------------

elif menu == "Receipt Scanner":

    st.header("Receipt AI Scanner")

    uploaded_file = st.file_uploader(
        "Upload Receipt",
        type=["png", "jpg", "jpeg"]
    )

    if uploaded_file:

        image = Image.open(uploaded_file)

        st.image(image)

        receipt_text = extract_receipt_text(
            image
        )

        st.subheader("Extracted Text")

        st.text(receipt_text)

        detected_amount = detect_total_amount(
            receipt_text
        )

        detected_category = (
            classify_expense_category(
                receipt_text
            )
        )

        st.success(
            f"Detected Amount: RM {detected_amount}"
        )

        st.success(
            f"Detected Category: "
            f"{detected_category}"
        )

# ---------------------------------------------------
# DASHBOARD
# ---------------------------------------------------

elif menu == "Dashboard":

    st.header("Financial Dashboard")

    dataframe = get_all_transactions()

    st.dataframe(dataframe)

    summary = calculate_summary(
        dataframe
    )

    st.metric(
        "Total Income",
        f"RM {summary['income']:.2f}"
    )

    st.metric(
        "Total Expense",
        f"RM {summary['expense']:.2f}"
    )

    st.metric(
        "Balance",
        f"RM {summary['balance']:.2f}"
    )

    figure = generate_expense_pie_chart(
        dataframe
    )

    st.plotly_chart(
        figure,
        use_container_width=True
    )

# ---------------------------------------------------
# AI ADVICE
# ---------------------------------------------------

elif menu == "AI Advice":

    st.header("AI Financial Advisor")

    dataframe = get_all_transactions()

    if st.button("Generate Advice"):

        advice = generate_budget_advice(
            dataframe
        )

        st.write(advice)

# ---------------------------------------------------
# STUDENT JOBS
# ---------------------------------------------------

elif menu == "Student Jobs":

    st.header("Nearby Student Jobs")

    location = st.text_input(
        "Location",
        "Petaling Jaya"
    )

    if st.button("Search Jobs"):

        jobs = search_student_jobs(
            location
        )

        for job in jobs:

            st.subheader(job["title"])

            st.write(
                job["company"]["display_name"]
            )

            st.write(
                job["location"]["display_name"]
            )

            st.write(
                job["description"][:250]
            )