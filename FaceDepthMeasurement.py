import threading
import winsound
import cv2
import cvzone
from cvzone.FaceMeshModule import FaceMeshDetector

cap = cv2.VideoCapture(0)
detector = FaceMeshDetector(maxFaces=1)

alarm = False
alarm_mode = False


def beep_alarm():
    global alarm
    print("Alarm.....")
    if alarm_mode:
        winsound.Beep(2500, 500)
    alarm = False


while True:
    success, img = cap.read()
    img, faces = detector.findFaceMesh(img, draw=False)  # get face lines

    if faces:
        face = faces[0]  # so consider only one face
        pointLeft = face[145]  # get leftEye
        pointRight = face[374]  # get rightEye

        # cv2.line(img, pointLeft, pointRight, (0, 200, 0), 3)
        # cv2.circle(img, pointRight, 5, (255, 0, 255), cv2.FILLED)
        # cv2.circle(img, pointLeft, 5, (255, 0, 255), cv2.FILLED)

        w, _ = detector.findDistance(pointLeft, pointRight)  # , _ remove rest of content w- fixels
        W = 6.3

        # # finding focal length
        #     W = 6.3
        #     d = 50
        #     f = (w*d)/W

        # finding distance
        f = 840
        d = (W * f) / w

        cvzone.putTextRect(img, f'Depth : {int(d)}cm', (face[10][0] - 100, face[10][1] - 50), scale=2)

        if d < 50:
            if not alarm:
                alarm = True
                alarm_mode = True
                threading.Thread(target=beep_alarm).start()

    cv2.imshow("Image", img)
    cv2.waitKey(1)
