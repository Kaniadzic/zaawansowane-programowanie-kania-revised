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

        img = cv.imread(f'{self.path}/{image_path}')
        img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

        # converted_img = cv.threshold(
        #     cv.medianBlur(img, 3), 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU
        # )[1]

        converted_img = cv.threshold(
            cv.bilateralFilter(img, 5, 75, 75), 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU
        )[1]

        # converted_img = cv.threshold(
        #     cv.GaussianBlur(img, (5, 5), 0), 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU
        # )[1]

        # converted_img = cv.threshold(
        #     cv.medianBlur(img, 3), 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 32
        # )[1]

        cv.imshow('image', converted_img)
        cv.waitKey(0)
        cv.destroyAllWindows()

        print(f'Przetwarzenie obrazka {image_path}...')
        text = pytesseract.image_to_string(converted_img)
        print(text)


processor = ImageProcessing('C:\\Users\\student\\source\\repos\\imageprocessing\\images')
images = processor.read_files()

print(images)
for img in images:
    processor.process_image(img)
