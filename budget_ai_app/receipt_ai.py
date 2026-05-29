```python
import easyocr
import numpy as np
from PIL import Image
import cv2

# Initialize OCR reader
reader = easyocr.Reader(['en'])

def preprocess_image(image):
    """
    Improve receipt image for OCR
    """

    # Convert PIL image to numpy array
    img = np.array(image)

    # Convert RGB to BGR
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Reduce noise
    gray = cv2.GaussianBlur(gray, (3, 3), 0)

    # Threshold for better OCR
    thresh = cv2.threshold(
        gray,
        0,
        255,
        cv2.THRESH_BINARY + cv2.THRESH_OTSU
    )[1]

    return thresh


def extract_receipt_text(image):
    """
    Extract text from receipt image
    """

    # Preprocess image
    processed_image = preprocess_image(image)

    # OCR detection
    results = reader.readtext(processed_image)

    # Combine all detected text
    extracted_text = ""

    for result in results:
        text = result[1]
        extracted_text += text + "\n"

    return extracted_text
```
