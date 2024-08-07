import cv2
import random

scale = 0.5
circles=[]
counter = 0
counter2 =0
point1=[]
point2=[]
myPoints=[]
myColor=[]

def mousePoints(event,x,y,flags,param):
    global counter, counter2, point1, point2, myPoints, myColor
    if event == cv2.EVENT_LBUTTONDOWN:
        if counter == 0:
            point1=int(x/scale),int(y/scale)
            counter+=1
            myColor = (random.randint(0,2)*200,random.randint(0,2)*200,random.randint(0,2)*200)
        elif counter == 1:
            point2=int(x/scale),int(y/scale)
            type = input("Enter Type: ")
            name = input("Enter Name: ")
            myPoints.append((point1, point2, type, name))
            counter =0
        circles.append([x,y,myColor])
        counter2+=1

img = cv2.imread("../passport/imgQ.jpg")
img = cv2.resize(img,(900,600))

while True:
    for x,y,color in circles:
        cv2.circle(img,(x,y),3,color,cv2.FILLED)
    cv2.imshow("Original Image",img)
    cv2.setMouseCallback("Original Image", mousePoints)
    if cv2.waitKey(1)& 0xFF == ord('s'):
        print(myPoints)
        break