from src.audiobook import create_audiobook

if __name__ == "__main__":
    print("--- Audiobook Creator ---")
    print("Please select a PDF file from the window that just opened...")

    try:
        create_audiobook()
        print("\nFinished reading the document successfully!")
    except Exception as e:
        print(f"\nAn error occurred: {e}")