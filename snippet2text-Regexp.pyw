import clipboard
import pytesseract
import PIL.Image
from PIL import ImageGrab, Image
import re


def remove_special_characters_and_spaces(bruh):
    return re.sub(r'[^\w-]+', '', bruh)


# dewd
# --------- coge el clipboard y lo guarda (luego de que tomamos un snap)-------
img = ImageGrab.grabclipboard()
print(img)
# print(isinstance(img, Image.Image))
print(img.size)
print(img.mode)
img.save('bruh.png')
# --------- pasamos la imagen por tesseract--------
# if no tesseract exe on our PATH, include:
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

bruh = pytesseract.image_to_string(PIL.Image.open(
    'bruh.png'))
print(remove_special_characters_and_spaces(bruh).replace("-", ""))

# ------------------ clipboard windows + V -------------------
clipboard.copy(remove_special_characters_and_spaces(bruh).replace("-", ""))


# sample-213213-000-323*111
