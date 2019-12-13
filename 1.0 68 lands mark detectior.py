import cv2
import dlib
camera=cv2.VideoCapture(0)

# camera is a video object,0-default camera,1,2-webcams/usb cams connected
#file_path can be also given,ip adress wifi cameras

while(True):
    ret,img=camera.read()
#capturing 1 frame from the video source 'camera object' and save it in 'img,
#ret is boolean value,1-camera is avilable,0-camera is not available

##print(ret==True):
##  cv2.imshow('IMG',img)

# avoid error when not camra(use ret)
    #img[50:100,50:100]=[255,0,0]

    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    #img-source image,cv2.COLOR_BGR2GRAY-color conversion flag
    #gray-resultant gray scaled image
    
    cv2.imshow('IMG',img)
    cv2.imshow('GRAY',gray)
    cv2.waitKey(1)
    # ims delay between each frame
