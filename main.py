import pytesseract.pytesseract
import cv2 as cv
import os

pytesseract.pytesseract.tesseract_cmd = 'C:\\Users\\student\\AppData\\Local\\Tesseract-OCR\\tesseract.exe'


class ImageProcessing:
    def __init__(self, folder_images_path: str):
        self.path = folder_images_path
        self.images = []

    def read_files(self):
        dir_files = os.listdir(self.path)
        for file in dir_files:
            if file[-4:].lower() == 'jpeg':
                self.images.append(file)
            elif file[-4:].lower() == '.jpg':
                self.images.append(file)
            elif file[-4:].lower() == '.png':
                self.images.append(file)

        return self.images

    def process_image(self, image_path: str):
        # img = cv.imread(image_path)
        img = cv.imread(f'{self.path}/{image_path}')
        print(f'Przetwarzenie obrazka {image_path}...')
        text = pytesseract.image_to_string(img)
        print(text)


processor = ImageProcessing('C:\\Users\\student\\source\\repos\\imageprocessing\\images')
images = processor.read_files()

print(images)
for img in images:
    processor.process_image(img)
