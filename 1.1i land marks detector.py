import cv2
import dlib
from imutils import face_utils
camera=cv2.VideoCapture(0)
face_detector=dlib.get_frontal_face_detector()
# a pretrained  face detecting classifier in dlib module
landmark_detector=dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')
#pretrained external algorithem for detecting 68 points of a face image



while(True):
    ret,img=camera.read()
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    rects=face_detector(gray)
    #algorithem.predict

    for rect in rects:
        x1=rect.left()
        y1=rect.top()
        x2=rect.right()
        y2=rect.bottom()

        cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
        cv2.rectangle(img,(x1-1,y1-10),(x1+60,y1),(0,255,0),-1)
        cv2.putText(img,'face',(x1+2,y1-2),cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,255,255),2)

        points=landmark_detector(gray,rect)
        #passing the gray image and bounding the  rectangle to the lND MARK DETECTOR
        # POINTS OBJECT CONTAIN 68 POINTS

        points=face_utils.shape_to_np(points)

        for p in points:
            cen=(p[0],p[1])
            cv2.circle(img,cen,2,(0,255,255),-1)
        #img-where the rect should be drawn
        #(0,255,0)-color in BGR
        #2-line width in px

        
    
    cv2.imshow('IMG',img)
    cv2.imshow('GRAY',gray)
    cv2.waitKey(1)
   
