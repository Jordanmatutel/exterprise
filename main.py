import os

# Loads the the file of the computers where the image its saved
folder_path = "computer/desktop/file_name/"

# Runs all the folder files
for filename in os.listdir(folder_path):
    # If the file ends with .png, then the algorithm starts searching the data
    if filename.endswith(".png"):
        image_path = os.path.join(folder_path, filename)
        image = cv2.imread(image_path)

        # Convert the image to grayscale
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Apply one filter in order to get better resolution in the image
        gray = cv2.medianBlur(gray, 3)

        # Apply OCR to extract text from image
        text = pytesseract.image_to_string(gray, lang='eng', config='--psm 11')

        # Find the ssn
        ssn = None
        for word in text.split():
            if len(word) == 11 and word.isdigit():
                ssn = word
                break

        # Find the name of the defendant and the accused
        defendant_name = None
        accused_name = None
        words = text.split()
        for i, word in enumerate(words):
            if word.lower() == 'defendant':
                defendant_name = words[i + 1]
            elif word.lower() == 'accused':
                accused_name = words[i + 1]
