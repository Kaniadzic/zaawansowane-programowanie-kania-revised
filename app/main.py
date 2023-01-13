import os
import sys
import cv2 as cv
import imutils
from PIL import Image
from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import flash
from flask import Response
from werkzeug.utils import secure_filename
from .consts import ALLOWED_EXTENSIONS
from .consts import UPLOAD_FOLDER
import time
import numpy as np


# region Config

app = Flask(__name__, template_folder='View')

HAAR_CASCADE = cv.CascadeClassifier('app/Model/haar_fuulbody.xml')
VIDEO_DETECTION = cv.dnn.readNetFromCaffe('app/Model/deploy.prototxt.txt',
                                          'app/Model/res10_300x300_ssd_iter_140000.caffemodel')

app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

camera = cv.VideoCapture(0)

global grey, negative, face
grey = 0
negative = 0
face = 0

# endregion

# region Helper Methods


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def get_file_extension(filename):
    return filename.rsplit('.', 1)[1].lower()


def detect_persons():
    img = cv.imread(app.config['UPLOAD_FOLDER'] + 'image.jpg')
    img = imutils.resize(img, width=min(600, img.shape[1]))

    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    body_rect = HAAR_CASCADE.detectMultiScale(
        gray, scaleFactor=1.01, minNeighbors=1
    )

    for (x, y, w, h) in body_rect:
        cv.rectangle(img, (x, y), (x+w, y+h), (49, 225, 247), thickness=2)

    return (img, len(body_rect))

# endregion


# region Video

def gen_frames():
    global out, capture

    while True:
        success, frame = camera.read()

        if (success):
            if (face):
                frame = detect_face(frame)
            if (grey):
                frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
            if (negative):
                frame = cv.bitwise_not(frame)

            try:
                ret, buffer = cv.imencode('.jpg', cv.flip(frame, 1))
                frame = buffer.tobytes()
                yield (b'--frame\r\n'
                       b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
            except Exception as ex:
                pass
        else:
            pass


def detect_face(frame):
    global VIDEO_DETECTION
    (h, w) = frame.shape[:2]
    blob = cv.dnn.blobFromImage(cv.resize(frame, (300, 300)), 1.0, (300, 300), (104.0, 177.0, 123.0))
    VIDEO_DETECTION.setInput(blob)
    detections = VIDEO_DETECTION.forward()
    confidence = detections[0, 0, 0, 2]

    if confidence < 0.5:
        return frame

    box = detections[0, 0, 0, 3:7] * np.array([w, h, w, h])
    (startX, startY, endX, endY) = box.astype("int")

    try:
        frame = frame[startY:endY, startX:endX]
        (h, w) = frame.shape[:2]
        r = 480 / float(h)
        dim = (int(w * r), 480)
        frame = cv.resize(frame, dim)
    except Exception as ex:
        pass
    return frame
# endregion

# region Endpoints


@app.route('/', methods=['GET'])
def home():
    return render_template("index.html", title="OpenEye")


@app.route('/imgdetection', methods=['GET'])
def imgdetection():
    return render_template("imgdetection.html", title="OpenEye - Image Detection", main_text="Select an image to upload")


@app.route('/imgdetection', methods=['POST'])
def detect_image():
    # sprawdzenie czy obrazek jest w requeście
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)

    # sprawdzenie czy obrazek jest w requeście
    file = request.files['file']
    if file.filename == '':
        flash('No image selected for uploading')
        return redirect(request.url)

    # sprawdzenie czy przesłany plik ma odpowiednie rozszerzenie
    if file and allowed_file(file.filename):
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], 'image.jpg'))
        flash('File uploaded succesfully')

        (person_detection, detection_count) = detect_persons()
        person_detection = cv.cvtColor(person_detection, cv.COLOR_BGR2RGB)

        person_detection = Image.fromarray(person_detection, "RGB")
        person_detection.save(os.path.join(app.config['UPLOAD_FOLDER'], f'image.jpg'))

        return render_template('imgdetection.html', detection_completed=True, main_text=f"Detected persons: {detection_count}")
    else:
        flash('Allowed image types are: png, jpg, jpeg and gif')
        return redirect(request.url)


@app.route('/display_image')
def display_image():
    return redirect(url_for('static', filename='uploads/image.jpg'), code=301)


@app.route('/viddetection', methods=['GET'])
def viddetection():
    return render_template("viddetection.html", title="OpenEye - Video Detection")


@app.route('/help', methods=['GET'])
def help():
    return render_template("help.html", title="OpenEye - Help")


@app.route('/about', methods=['GET'])
def about():
    return render_template("about.html", title="OpenEye - About")


@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/video_tasks', methods=['POST', 'GET'])
def video_tasks():
    global switch, camera

    if request.method == 'POST':
        if request.form.get('grey') == 'Grey':
            global grey
            grey = not grey
        elif request.form.get('negative') == 'Negative':
            global negative
            negative = not negative
        elif request.form.get('face') == 'Face Only':
            global face
            face = not face
            if (face):
                time.sleep(4)
    elif request.method == 'GET':
        return render_template('viddetection.html')

    return render_template('viddetection.html')
# endregion
