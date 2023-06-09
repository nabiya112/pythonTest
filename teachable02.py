import tensorflow.keras
import numpy as np
import cv2

model = tensorflow.keras.models.load_model('keras_model.h5')

cap = cv2.VideoCapture(0)

size = (224, 224)

classes = ['hairpin', 'glasses', 'wire']

while cap.isOpened():
    ret, img = cap.read()
    if not ret:
        break

    h, w, _ = img.shape
    cx = h / 2
    img = img[:, 200:200+img.shape[0]]
    img = cv2.flip(img, 1)

    img_input = cv2.resize(img, size)
    img_input = cv2.cvtColor(img_input, cv2.COLOR_BGR2RGB)
    img_input = (img_input.astype(np.float32) / 127.0) - 1
    img_input = np.expand_dims(img_input, axis=0)

    prediction = model.predict(img_input)
    idx = np.argmax(prediction)

    cv2.putText(img, text=classes[idx], org=(10, 30), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=0.8, color=(255, 255, 255), thickness=2)

    cv2.imshow('result', img)
    if cv2.waitKey(1) == ord('q'):
        break
    
# 캠 파일 되는지 먼저 확인하고 이 파일의 classes 배열속에 학습시킨 class 갯수에 맞게 이름을 수정하여 실행한다.
# 사전작업 : pip 업데이트, tensorflow 설치, opencv 설치, numpy 설치