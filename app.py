import os
from flask import Flask, render_template, request
import cv2 as cv
import argparse
import sys
import numpy as np
import os.path
from yolo_detection import hello 
from ocr_core import ocr_core
UPLOAD_FOLDER = '/static/uploads/'
UPLOAD_FOLDER2 = '/static/detect_cut/'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def home_page():
    return render_template('index.html')


@app.route('/upload', methods=['GET', 'POST'])
def upload_page():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            return render_template('upload.html', msg='No file selected')
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            return render_template('upload.html', msg='No file selected')

        if file and allowed_file(file.filename):
            file.save(os.path.join(os.getcwd() + UPLOAD_FOLDER, file.filename))
            print(file.filename);
            # call the yolo3 function on it
            extracted_text = hello(file) 
            extracted_text2 = ocr_core(file)

 

            # extract the text/predeted image and display it
            return render_template('upload.html',
                                   msg='Successfully processed',
                                   extracted_text=extracted_text2,
                                   img_src=UPLOAD_FOLDER + extracted_text,
                                   img_cut=UPLOAD_FOLDER2 +file.filename)
    elif request.method == 'GET':
        return render_template('upload.html')

if __name__ == '__main__':
    app.run(debug=True)
