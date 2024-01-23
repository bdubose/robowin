
from PIL import Image, ImageEnhance
from pytesseract import pytesseract


def read_image_text(image: Image) -> str:
    image = enhance_image(image)
    return pytesseract.image_to_string(image)

def enhance_image(image: Image) -> Image:
    image = ImageEnhance.Color(image).enhance(0)
    return image
