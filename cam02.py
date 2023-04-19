import cv2

cap = cv2.VideoCapture(0)  # 0은 내장 카메라, 1은 외부 카메라를 의미합니다.

while True:
    ret, frame = cap.read()  # 카메라에서 프레임을 읽어옵니다.
    
    # 프레임 처리 작업
    # ...

    cv2.imshow("Camera", frame)  # 프레임을 화면에 출력합니다.
    
    if cv2.waitKey(1) == ord('q'):  # 'q'를 누르면 종료합니다.
        break

cap.release()  # 카메라를 해제합니다.
cv2.destroyAllWindows()  # 모든 창을 닫습니다.