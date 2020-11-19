from flask import Flask, request, jsonify
from face_detection import img


app = Flask(__name__)


@app.route("/predict")
def hello():
    # use http://127.0.0.1:5000/predict?url=https://xxxx.xxx
    # or http://127.0.0.1:5000/predict?name=face-8.png
    url = request.args.get('url', default=None, type=str)
    name = request.args.get('name', default=None, type=str)
    array = img(image_path=name, url_path=url)
    return jsonify(array)


if __name__ == "__main__":
    app.run()