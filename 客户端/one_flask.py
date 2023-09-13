# -*- coding: utf-8 -*- 

from flask import Flask, jsonify, request
import cv2
import base64
import numpy as np
from cnsenti import Sentiment
import easyocr
app =Flask(__name__)
reader = easyocr.Reader(['ch_sim']) 
def base64_to_image(imgBase64):
    img_data = base64.b64decode(imgBase64)
    bs = np.asarray(bytearray(img_data), dtype='uint8')
    img = cv2.imdecode(bs, cv2.IMREAD_COLOR)
    return img

def base64toText(img):
    np_img = base64_to_image(img)
    #reader = easyocr.Reader(['ch_sim','en']) # this needs to run only once to load the model into memory
    result = reader.readtext( np_img  )    # reader.readtext( "chinese.png" )   
    # data = {
    #     "text": ''.join(res[-2] for res in result)
    # }
    # return jsonify(data)
    return   ''.join(res[-2] for res in result)


def base64toTexts(imgs):
    np_img0 = base64_to_image(imgs[0])
    np_img1 = base64_to_image(imgs[1])
    np_img2 = base64_to_image(imgs[2])
 
    #好像不支持多图，尴尬了
    #np_img0=np.expand_dims(np_img0, axis=0)
    #np_img1=np.expand_dims(np_img1, axis=0)  
    #np_img2=np.expand_dims(np_img2, axis=0)    
    #np_img = np.concatenate((np_img0,np_img1,np_img2))
     
    # reader.readtext( "chinese.png" )    
    result0 = reader.readtext( np_img0  ) 
    result1 = reader.readtext( np_img1  ) 
    result2 = reader.readtext( np_img2  )  
    texts = []  
    texts.append( ''.join(res[-2] for res in result0) )
    texts.append( ''.join(res[-2] for res in result1) )
    texts.append( ''.join(res[-2] for res in result2) )
    return texts

def text2senti(text):  
    senti = Sentiment() 
    result = senti.sentiment_count(text) 
    #print(result) 
    return result


@app.route('/ocr', methods=["POST"])
def ocr():
    data = request.json 
    img = data["base64Img"] 
    text = base64toText(img) 
    res = text2senti(text)
    obj = { 'text': text,'pos': res['pos'], 'neg': res['neg']}
    return obj 
  
@app.route('/ocr3', methods=["POST"])
def ocr3():
    data = request.json 
    img0 = data["base64_0"] 
    img1 = data["base64_1"] 
    img2 = data["base64_2"]  
    texts = base64toTexts([img0,img1,img2])  
    obj = []
    for text in texts:
        res = text2senti(text)
        obj.append( { 'text': text,'pos': res['pos'], 'neg': res['neg']} ) 
    return {'result':obj}

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run()
