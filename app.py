from flask import Flask, flash, render_template, redirect, request, url_for
import os
import cv2
import numpy as np
from keras.models import load_model
from keras.preprocessing import image
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['SECRET_KEY'] = "supertopsecretprivatekey"
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('new.html', message="No image has been uploaded")

    if request.method == 'POST':
        f = request.files['image']
        basepath = os.path.dirname(__file__)
        src = f.filename
        src = "Upload/"+src
        file_path = os.path.join(
            basepath, 'Upload', secure_filename(f.filename))
        size = os.stat(file_path).st_size
        if size > 10000000:
            return render_template('new.html', message="size is more than 10MB")

        f.save(file_path)
        preds = predict(file_path)
        if preds == 1:
            # isrc="static/face2.jpg
            return render_template('new.html', message="Positive")
        else:
            # isrc="static/face2.jpg
            return render_template('new.html', message="Negative")


@app.route('/', methods=['GET', 'POST'])
def predict(filep):
    model = load_model('hack.h5')
    img = image.load_img(filep, target_size=(224, 224))
    x = image.img_to_array(img)
    img = cv2.resize(x, (224, 224))
    img = np.reshape(img, [-1, 224, 224, 3])
    prediction = model.predict([img])
    prediction = np.argmax(prediction)
    return prediction


@ app.route('/unt', methods=['GET', 'POST'])
def unt():
    if request.method == 'POST':
        cov = request.form["BP"]
        ox = request.form["oxy"]
        temp = request.form["temp"]
        cough = request.form["cough"]
        name = request.form["fname"]
        r1 = "hidden"
        r2 = "hidden"
        r3 = "hidden"
        r4 = "hidden"
        if int(ox) < 91:
            r3 = ""
        if int(temp) > 100:
            r1 = ""
        if cough == "yes":
            r2 = ""
        if cov == "yes":
            r4 = ""
        return render_template('third.html', naam=name, cov=r4, fever=r1, cough=r2, oxygen=r3)
    if request.method == 'GET':
        return render_template('unt.html')


if __name__ == "__main__":
    app.run('127.0.0.1', debug=True)
