import cv2
from urllib.request import urlopen
import numpy as np
import ssl
import json


def _url_to_image(url) -> [[]]:
    ssl._create_default_https_context = ssl._create_unverified_context
    req = urlopen(url)
    arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
    img = cv2.imdecode(arr, -1)
    return img


def img(image_path: str = None, url_path: str = None):
    classifier = cv2.CascadeClassifier('frontalface_default.xml')
    if url_path is not None:
        img_file = _url_to_image(url_path)
    else:
        img_file = cv2.imread(image_path)
    gray = cv2.cvtColor(img_file, cv2.COLOR_BGR2GRAY)
    faces = classifier.detectMultiScale(gray, 1.1, 4)
    list_json = []
    for (x, y, w, h) in faces:
        list_json.append({"x": int(x), "y": int(y), "w": int(w), "h": int(h)})
    return list_json
