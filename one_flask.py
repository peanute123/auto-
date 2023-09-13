# -*- coding: utf-8 -*- 

from flask import Flask, jsonify, request
import cv2
import base64
import numpy as np

app =Flask(__name__)


def base64_to_image(imgBase64):
    img_data = base64.b64decode(imgBase64)
    bs = np.asarray(bytearray(img_data), dtype='uint8')
    img = cv2.imdecode(bs, cv2.IMREAD_COLOR)
    return img

import easyocr
@app.route('/ocr', methods=["POST"])
def ocr():
    data = request.json
    ####接收到的信息 print("Request dict data key is: \n", data.keys(), type(data))
    img = data["base64Img"] 
    np_img = base64_to_image(img)
    reader = easyocr.Reader(['ch_sim','en']) # this needs to run only once to load the model into memory
    result = reader.readtext( np_img  )    # reader.readtext( "chinese.png" )   
    data = {
        "text": ','.join(res[-2] for res in result)
    }
    return jsonify(data)

@app.route('/')
def hello_world():
    return 'Hello, World!'
  
if __name__ == '__main__':
    app.run()