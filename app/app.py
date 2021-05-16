from flask import Flask, render_template, request, jsonify
from model import predict
from werkzeug.utils import secure_filename
import os
import pathlib

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template("index.html")

@app.route("/submit", methods=['POST'])
def submit():
    file = request.files["pic"]
    filename = secure_filename(file.filename)

    path = os.path.join(pathlib.Path().absolute(), 'uploads', filename)
    file.save(path)

    classname, confidence = predict(path)
    os.remove(path)
    
    return jsonify({"class": classname, "confidence": confidence})

if __name__ == '__main__':
    app.run()