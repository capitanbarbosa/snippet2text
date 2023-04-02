import clipboard
import pytesseract
import PIL.Image
from PIL import ImageGrab, Image
import re


def remove_special_characters_and_spaces(image):
    return re.sub(r'[^\w-]+', '', image)


# dewd
# --------- coge el clipboard y lo guarda (luego de que tomamos un snap)-------
img = ImageGrab.grabclipboard()
print(img)
# print(isinstance(img, Image.Image))
print(img.size)
print(img.mode)
img.save('image.png')
# --------- pasamos la imagen por tesseract--------
# if no tesseract exe on our PATH, include:
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

image = pytesseract.image_to_string(PIL.Image.open(
    'image.png'))
print(remove_special_characters_and_spaces(image).replace("-", ""))

# ------------------ clipboard windows + V -------------------
clipboard.copy(remove_special_characters_and_spaces(image).replace("-", ""))


# sample-213213-000-323*111
