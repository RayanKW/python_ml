import cv2
import os

cap = cv2.VideoCapture(0)
cap.set(3, 648)
cap.set(4, 488)

imgBackground = cv2.imread('Resources/background.png')

folderModePath = 'Resources/Modes'
modePathList = os.listdir(folderModePath)
imgModeList = []
for i in modePathList:
    imgModeList.append(cv2.imread(os.path.join(folderModePath)))
    print(len(imgModeList))

while True:
    success, img=cap.read()
    imgBackground[162:162 + 480, 55:55 + 640] = img
    # imgBackground[44:44 + 633, 808:808 + 414] = imgModeList[1]
    cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    
    cv2.imshow('webcam', img)
    cv2.imshow('face', imgBackground)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
    
    cap.release()
    cv2.destroyAllWindows()