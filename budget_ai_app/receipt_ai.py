import pytesseract
import re


def extract_text(image):
    """
    Extract receipt text using OCR.
    """

    return pytesseract.image_to_string(image)


def detect_total(text):
    """
    Detect highest monetary amount.
    """

    amounts = re.findall(r"\d+\.\d{2}", text)

    if amounts:
        return max([float(x) for x in amounts])

    return 0.0


def classify_category(text):
    """
    Predict expense category.
    """

    text = text.lower()

    if "grab" in text:
        return "Transport"

    if "mcd" in text or "kfc" in text:
        return "Food"

    if "watsons" in text:
        return "Health"

    return "Others"
