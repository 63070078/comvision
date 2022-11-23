import cv2
import numpy as np
import dlib


#webcam = True

#cap = cv2.VideoCapture("1.mp4")

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

def empty(a):
    pass
cv2.namedWindow('BGR')
cv2.resizeWindow('BGR',440,140)
cv2.createTrackbar('Blue','BGR',0,255,empty)
cv2.createTrackbar('Green','BGR',0,255,empty)
cv2.createTrackbar('Red','BGR',0,255,empty)

def createBox(img,points,scale=5,masked=False,cropped = True):
    if masked:
        mask = np.zeros_like(img)
        mask = cv2.fillPoly(mask,[points],(255,255,255))
        img = cv2.bitwise_and(img,mask)
        # ปาก
      #  cv2.imshow('Mask',img)

    if cropped:
        bbox = cv2.boundingRect(points)
        x,y,w,h = bbox
        imgCrop = img[y:y+h,x:x+w]
        imgCrop = cv2.resize(imgCrop,(0,0),None,scale,scale)
        return imgCrop
    else:
        return mask

while True:
    #webcam
    # if webcam: success,img = cap.read()
    # else:img = cv2.imread('2.jpg')
    # image ใส่รูป
    img = cv2.imread('tae.jpg')

    img = cv2.resize(img,(0,0),None,0.5,0.5)

    # ขนาดรูปตามต้นฉบับ
    #imgOriginal = img.copy() 
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = detector(imgGray)

    for face in faces:
        x1,y1 = face.left(),face.top()
        x2,y2 = face.right(),face.bottom()
        imgOriginal = cv2.rectangle(img, (x1,y1),(x2,y2),(0,255,0),2)
        landmarks = predictor(imgGray,face)
        myPoints =[]
        for n in range(68):
            x = landmarks.part(n).x
            y = landmarks.part(n).y
            myPoints.append([x,y])
            
        myPoints = np.array(myPoints)

        # imgLeftEye = createBox(img,myPoints[36:42],8)
        # cv2.imshow('LeftEye',imgLeftEye)
        b = cv2.getTrackbarPos('Blue','BGR')
        g = cv2.getTrackbarPos('Green','BGR')
        r = cv2.getTrackbarPos('Red','BGR')

        imgLeftEye = createBox(img,myPoints[17:22],8,masked=True,cropped=False)
        imgColorLeftEye = np.zeros_like(imgLeftEye)
        imgColorLeftEye[:] = b,g,r
        imgColorLeftEye = cv2.bitwise_and(imgLeftEye,imgColorLeftEye)
        imgColorLeftEye = cv2.GaussianBlur(imgColorLeftEye,(7,7),10)

        imgRightEye = createBox(img,myPoints[22:27],8,masked=True,cropped=False)
        imgColorRightEye = np.zeros_like(imgRightEye)
        imgColorRightEye[:] = b,g,r
        imgColorRightEye = cv2.bitwise_and(imgRightEye,imgColorRightEye)
        imgColorRightEye = cv2.GaussianBlur(imgColorRightEye,(7,7),10)

        #color_image
        imgL = cv2.addWeighted(imgOriginal,1,imgColorRightEye,0.4,0)
        imgL = cv2.addWeighted(imgL,1,imgColorLeftEye,0.4,0)
        imgL = cv2.addWeighted(imgL,1,imgColorRightEye,0.4,0)
        cv2.imshow('BGR',imgL)

       # cv2.imshow('Lips',imgLips)

    #cv2.imshow("Original",imgOriginal)
    cv2.waitKey(1)