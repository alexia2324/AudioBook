import pyttsx3
import PyPDF2
from tkinter.filedialog import askopenfilename


def create_audiobook():
    # 1. Select the PDF file from your computer
    book_path = askopenfilename()

    if not book_path:
        print("No file selected.")
        return

    # 2. Initialize the PDF reader object
    with open(book_path, 'rb') as book:
        pdf_reader = PyPDF2.PdfReader(book)
        pages = len(pdf_reader.pages)  # Get total number of pages

        # 3. Initialize the Text-to-Speech engine
        speaker = pyttsx3.init()

        print(f"Starting to read {pages} pages...")

        # 4. Loop through each page and read the text
        for num in range(0, pages):
            page = pdf_reader.pages[num]
            text = page.extract_text()  # Extract text from current page

            # 5. Make the computer speak the text
            speaker.say(text)
            speaker.runAndWait()  # Process the voice commands


if __name__ == "__main__":
    create_audiobook()
