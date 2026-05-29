import pytesseract
from PIL import Image
import os

# Force tesseract path
pytesseract.pytesseract.tesseract_cmd = "/usr/bin/tesseract"

def extract_receipt_text(image):

    # Debug check
    print("Tesseract exists:",
          os.path.exists("/usr/bin/tesseract"))

    text = pytesseract.image_to_string(image)

    return text