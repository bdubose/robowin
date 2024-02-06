"""Functions for reading and manipulating images."""

from PIL import Image, ImageEnhance
from pytesseract import pytesseract


def read_image_text(image: Image) -> str:
    """Reads text from provided Image."""
    image = enhance_image(image)
    # --psm 6 tells tesseract that this is a single uniform block of text
    return pytesseract.image_to_string(image, lang='eng', config='--psm 6')

def enhance_image(image: Image) -> Image:
    """Applies various enhancements to the provided Image."""
    image = ImageEnhance.Color(image).enhance(0)
    return image
