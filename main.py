import cv2
import numpy as np
import os

path = '../passport/'
per = 25
roi = [((574, 228), (924, 266), 'text', 'type'), ((992, 228), (1150, 272), 'text', 'code'), ((1280, 230), (1584, 278), 'text', 'Passport No'), ((568, 306), (1760, 390), 'test', 'Surname')]

imgQ = cv2.imread('../passport/imgQ.jpg')
h,w,c = imgQ.shape

orb = cv2.ORB_create(1000)
kp1,des1 = orb.detectAndCompute(imgQ, None)

# impKp1 = cv2.drawKeypoints(imgQ,kp1,None)
# cv2.imshow('Keypoints Image', impKp1)

picList = os.listdir(path)
for j,y in enumerate(picList):
    img = cv2.imread(path + y)
    h,w,c = img.shape
    # img = cv2.resize(img,(w//3, h//3))
    # cv2.imshow(y, img)
    kp2,des2 = orb.detectAndCompute(img, None)
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    matches = bf.match(des2, des1)
    matches = sorted(matches, key = lambda x:x.distance)
    good = matches[:int(len(matches)*(per/100))]
    imgMatch = cv2.drawMatches(img,kp2,imgQ,kp1, good,None, flags=2)
    # cv2.imshow(y, imgMatch)
    
    srcPoints = np.float32([kp2[m.queryIdx].pt for m in good]).reshape(-1,1,2)
    dstPoints = np.float32([kp1[m.trainIdx].pt for m in good]).reshape(-1,1,2)
    
    M, _ =cv2.findHomography(srcPoints, dstPoints, cv2.RANSAC,5.0)
    imgScan = cv2.warpPerspective(img, M, (w,h))
    img = cv2.resize(imgScan,(w//3, h//3))
    cv2.imshow(y, imgScan)
    

# cv2.imshow('Original Image', imgQ)
# imgQ = cv2.resize(imgQ,(w//3, h//3))
cv2.waitKey(0)