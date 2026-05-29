```python
import pytesseract
import re
from PIL import Image


# ---------------------------------------------------
# EXTRACT TEXT FROM RECEIPT
# ---------------------------------------------------

def extract_receipt_text(image):
    """
    Extract text from receipt image using OCR.
    """

    try:

        # Convert image to RGB
        image = image.convert("RGB")

        # Extract text
        text = pytesseract.image_to_string(image)

        # Handle empty OCR result
        if not text.strip():

            return "No text detected from receipt."

        return text

    except Exception as error:

        return f"OCR Error: {error}"


# ---------------------------------------------------
# DETECT TOTAL AMOUNT
# ---------------------------------------------------

def detect_total_amount(text):
    """
    Detect highest amount from receipt text.
    """

    try:

        # Find decimal numbers
        amounts = re.findall(r"\d+\.\d{2}", text)

        if amounts:

            amounts = [
                float(amount)
                for amount in amounts
            ]

            return max(amounts)

        return 0.0

    except Exception as error:

        print(f"Amount Detection Error: {error}")

        return 0.0


# ---------------------------------------------------
# CLASSIFY EXPENSE CATEGORY
# ---------------------------------------------------

def classify_expense_category(text):
    """
    Categorize expense using keywords.
    """

    try:

        text = text.lower()

        # Food
        food_keywords = [
            "mcd",
            "kfc",
            "starbucks",
            "restaurant",
            "food",
            "coffee",
            "tea"
        ]

        # Transport
        transport_keywords = [
            "grab",
            "uber",
            "parking",
            "lrt",
            "mrt",
            "petrol",
            "shell",
            "petronas"
        ]

        # Shopping
        shopping_keywords = [
            "watsons",
            "guardian",
            "uniqlo",
            "mr diy",
            "shopping"
        ]

        # Grocery
        grocery_keywords = [
            "tesco",
            "aeon",
            "lotus",
            "99 speedmart",
            "grocery"
        ]

        # Match keywords
        for keyword in food_keywords:

            if keyword in text:
                return "Food"

        for keyword in transport_keywords:

            if keyword in text:
                return "Transport"

        for keyword in shopping_keywords:

            if keyword in text:
                return "Shopping"

        for keyword in grocery_keywords:

            if keyword in text:
                return "Groceries"

        return "Others"

    except Exception as error:

        print(f"Category Classification Error: {error}")

        return "Others"


# ---------------------------------------------------
# PROCESS RECEIPT
# ---------------------------------------------------

def process_receipt(image):
    """
    Complete receipt processing pipeline.
    """

    text = extract_receipt_text(image)

    amount = detect_total_amount(text)

    category = classify_expense_category(text)

    return {
        "text": text,
        "amount": amount,
        "category": category
    }
```

