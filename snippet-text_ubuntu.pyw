import pytesseract
from PIL import Image
import pyperclip
import os

# Specify the path to the Tesseract executable on your system
pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'  # Update this path if different

# Directory where screenshots are saved
screenshot_directory = '/home/wiz/Pictures/Screenshots'

# Get the list of all files in the directory sorted by modification time
list_of_files = sorted(
    [os.path.join(screenshot_directory, f) for f in os.listdir(screenshot_directory)],
    key=os.path.getmtime
)

# Pick the most recent file
latest_image_path = list_of_files[-1]  # Assuming there is at least one image in the directory

# Ensure the selected file is an image
if latest_image_path.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif')):
    img = Image.open(latest_image_path)
    print(f"Processing image: {latest_image_path}")
    print(img.size)
    print(img.mode)
    # --------- OCR with Tesseract --------
    text = pytesseract.image_to_string(img)
    print(text)

    # ------------------ Copy to Clipboard -------------------
    pyperclip.copy(text)
else:
    print("The latest file is not an image.")
