import cv2
import cvzone
from cvzone.HandTrackingModule import HandDetector
import numpy as np
import threading


class pong:
    def __init__(self):
        pass
    def start(self):
        print('Game Started')
        camvision = cv2
        cvz = cvzone
        cap = camvision.VideoCapture(0)
        cap.set(3, 1280)
        cap.set(4, 720)
        
        # Importing all images
        imgBackground = camvision.imread("Resources/Background.png")
        imgGameOver = camvision.imread("Resources/gameOver.png")
        imgBall = camvision.imread("Resources/Ball.png", camvision.IMREAD_UNCHANGED)
        imgBat1 = camvision.imread("Resources/bat1.png", camvision.IMREAD_UNCHANGED)
        imgBat2 = camvision.imread("Resources/bat2.png", camvision.IMREAD_UNCHANGED)
        
        # Hand Detector
        detector = cvz.HandTrackingModule.HandDetector(detectionCon=0.8, maxHands=2)
        
        # Variables
        ballPos = [100, 100]
        speedX = 15
        speedY = 15
        gameOver = False
        score = [0, 0]
        
        
        while True:
            _, img = cap.read()
            img = camvision.flip(img, 1)
            imgRaw = img.copy()

            # Find the hand and its landmarks
            hands, img = detector.findHands(img, flipType=False)  # with draw

            # Overlaying the background image
            img = camvision.addWeighted(img, 0.2, imgBackground, 0.8, 0)

            # Check for hands
            if hands:
                for hand in hands:
                    x, y, w, h = hand['bbox']
                    h1, w1, _ = imgBat1.shape
                    y1 = y - h1 // 2
                    y1 = np.clip(y1, 20, 415)

                    if hand['type'] == "Left" :
                        img = cvz.overlayPNG(img, imgBat1, (59, y1))
                        if 59 < ballPos[0] < 59 + w1 and y1 < ballPos[1] < y1 + h1:
                            speedX = -speedX
                            ballPos[0] += 30
                            score[0] += 1

                    if hand['type'] == "Right" :
                        img = cvz.overlayPNG(img, imgBat2, (1195, y1))
                        if 1195 - 50 < ballPos[0] < 1195 and y1 < ballPos[1] < y1 + h1:
                            speedX = -speedX
                            ballPos[0] -= 30
                            score[1] += 1

            # Game Over
            if ballPos[0] < 40 or ballPos[0] > 1200:
                gameOver = True

            if gameOver:
                img = imgGameOver
                camvision.putText(img, str(score[1] + score[0]).zfill(2), (585, 360), camvision.FONT_HERSHEY_COMPLEX,
                            2.5, (200, 0, 200), 5)

            # If game not over move the ball
            else:

                # Move the Ball
                if ballPos[1] >= 500 or ballPos[1] <= 10:
                    speedY = -speedY

                ballPos[0] += speedX
                ballPos[1] += speedY

                # Draw the ball
                img = cvz.overlayPNG(img, imgBall, ballPos)

                camvision.putText(img, str(score[0]), (300, 650), camvision.FONT_HERSHEY_COMPLEX, 3, (255, 255, 255), 5)
                camvision.putText(img, str(score[1]), (900, 650), camvision.FONT_HERSHEY_COMPLEX, 3, (255, 255, 255), 5)

            # img[580:700, 20:233] = camvision.resize(imgRaw, (213, 120))

            camvision.imshow("Image", img)
            key = camvision.waitKey(1)
            if key == 32:
                break
            if key == ord('r'):
                ballPos = [100, 100]
                speedX = 15
                speedY = 15
                gameOver = False
                score = [0, 0]
                imgGameOver = camvision.imread("Resources/gameOver.png")
p=pong()
def start():
    t1=threading.Thread(target=p.start)
    t1.start()