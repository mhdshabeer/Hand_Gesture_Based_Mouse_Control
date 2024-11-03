import cv2
import numpy as np
import mediapipe as mp
import pyautogui

# Video capturing
cap = cv2.VideoCapture(0)

# Hand Detector in Mediapipe
HD = mp.solutions.hands.Hands()

#for drawing points on hand
du = mp.solutions.drawing_utils

#screen height and width
sw , sh = pyautogui.size()
index_x =0
index_y = 0
while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame,1)
    f_height , f_width , i= frame.shape
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    op = HD.process(rgb)
    hands = op.multi_hand_landmarks
    if hands:
        for hand in hands:
            du.draw_landmarks(frame,hand)
            landmark = hand.landmark
            for id,ld in enumerate(landmark):
                x = int(ld.x*f_width)
                y = int(ld.y*f_height)
                if id==8:
                    cv2.circle(img=frame,center=(x,y),color=(0,255,255),radius=15)
                    index_x = sw/f_width*x
                    index_y = sh/f_height*y

                if id==12:
                    cv2.circle(img=frame,center=(x,y),color=(0,255,255),radius=15)
                    mid_x = sw/f_width*x
                    mid_y = sh/f_height*y
                    pyautogui.moveTo(mid_x,mid_y)
                    print(abs(mid_x - index_x))
                    if(abs(mid_x - index_x)<40):
                        print('right click')
                        pyautogui.rightClick()
                        pyautogui.sleep(1)
                if id==4:
                    cv2.circle(img=frame,center=(x,y),color=(0,255,255),radius=15)
                    thumb_x = sw/f_width*x
                    thumb_y = sh/f_height*y
                    if(abs(thumb_y - index_y)<40):
                        print('left click')
                        pyautogui.leftClick()
                        pyautogui.sleep(1)


    cv2.imshow('Frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
