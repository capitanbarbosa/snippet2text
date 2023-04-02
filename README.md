# Snippet2Text (OCR)

Grabs the latest image from the clipboard (any snip from the screen) and transforms it to text. Finally, it places the text inside the clipboard ready to be pasted, in milliseconds.

A radial menu will be used to launch the script easily (from inside this repo: https://github.com/dumbeau/AutoHotPie), through a shortcut on the keyboard, to swiftly launch the script from the menu.

- note\*
  We can also use tools such as Windows Power Toy’s “Text Extractor” in the same fashion. But, it is less accurate, has no regexp version, and there is a minimum window snap size (meaning we cannot convert small images containing a very short string.)

Tech Stack / Tools:

- Tesseract
- pyTesseract
- Pie Menu Repo (to launch the script via UI shortcut)

Let’s go:

1. Download and install Tesseract OCR from Mannheim University Library. → [https://digi.bib.uni-mannheim.de/tesseract/](https://digi.bib.uni-mannheim.de/tesseract/)

   - The exact specific version we will use for this example → [tesseract-ocr-w64-setup-5.3.0.20221222.exe](https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-w64-setup-5.3.0.20221222.exe)

2. Once installed, we get our script. → https://github.com/capitanbarbosa/snippet2text

   - There’s 2 versions of Snippet2Text included:
     - with a Regexp that removes any special chars such as -./() (useful for bank inscriptions, form transcription…)
     - without a Regexp; it transforms the text image as-is. (useful for copying code from anywhere; youtube, etc.)

3. Get AutoHotMenu pie menu → create a menu, set up keyboard shortcut.

4. Call the snippet2text script from the shortcut.

![snippet2text-demoVid](https://user-images.githubusercontent.com/65256527/229378550-78eaee33-f6b3-4c84-bb12-ec3925e995eb.gif)

Extract any image to text, from anywhere in seconds. | Integrating Tesseract OCR via a shortcut on Windows with python and pytesseract.
