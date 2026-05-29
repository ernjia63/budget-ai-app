import pytesseract
import re


def extract_receipt_text(image):
    """
    Extract text from receipt image using OCR.
    """

    text = pytesseract.image_to_string(image)

    return text


def detect_total_amount(text):
    """
    Detect total amount from receipt text.
    """

    amounts = re.findall(r"\d+\.\d{2}", text)

    if amounts:
        return max([float(amount) for amount in amounts])

    return 0.0


def classify_expense_category(text):
    """
    Categorize expense using keyword matching.
    """

    text = text.lower()

    food_keywords = [
        "mcd",
        "kfc",
        "starbucks",
        "restaurant"
    ]

    transport_keywords = [
        "grab",
        "uber",
        "lrt",
        "parking"
    ]

    shopping_keywords = [
        "uniqlo",
        "watsons",
        "guardian"
    ]

    for keyword in food_keywords:
        if keyword in text:
            return "Food"

    for keyword in transport_keywords:
        if keyword in text:
            return "Transport"

    for keyword in shopping_keywords:
        if keyword in text:
            return "Shopping"

    return "Others"