import clipboard
import pytesseract
import PIL.Image
from PIL import ImageGrab, Image

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
print(image)
# ------------------ clipboard windows + V -------------------
clipboard.copy(image)
