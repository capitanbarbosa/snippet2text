from PIL import ImageGrab, Image
import PIL.Image
import pytesseract
import clipboard
#--------- coge el clipboard y lo guarda (luego de que tomamos un snap)-------
img = ImageGrab.grabclipboard()
print(img)
# print(isinstance(img, Image.Image))
print(img.size)
print(img.mode)
img.save(r'C:\Users\luisd\OneDrive\Documents\Coding\Wiz Labs\Snippet-to-text\bruh.png')
#--------- pasamos la imagen por tesseract--------
#if no tesseract exe on our PATH, include:
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'

bruh = pytesseract.image_to_string(PIL.Image.open(r'C:\Users\luisd\OneDrive\Documents\Coding\Wiz Labs\Snippet-to-text\bruh.png'))
print(bruh)

#------------------ clipboard windows + V -------------------
clipboard.copy(bruh)

