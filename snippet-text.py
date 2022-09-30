from PIL import ImageGrab, Image
import PIL.Image
import pytesseract
import clipboard
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
print(bruh)

# ------------------ clipboard windows + V -------------------
clipboard.copy(bruh)
