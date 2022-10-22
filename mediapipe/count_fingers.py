import cv2
import mediapipe as mp

mano= mp.solutions.hands
dibujar= mp.solutions.drawing_utils

hands= mano.Hands(min_detection_confidence=0.8, min_tracking_confidence=0.5)

cap= cv2.VideoCapture(0)

while True:
    success, image = cap.read()


    cv2.imshow("Controlador de medios", image)
    
    key=cv2.waitKey(1)
    if key == 32:
        break

cv2.destroyAllWindows()