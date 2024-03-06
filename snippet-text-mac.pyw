import os
import pytesseract
import PIL.Image
import pyperclip

# Save the clipboard image to a file using pngpaste
os.system('pngpaste image.png')

# Process the image with Tesseract
pytesseract.pytesseract.tesseract_cmd = '/opt/homebrew/bin/tesseract'  # Path to the tesseract, adjust if necessary

image = pytesseract.image_to_string(PIL.Image.open('image.png'))
print(image)

# Copy the result text to clipboard
pyperclip.copy(image)
 