import cv2
import pickle
import numpy as np
import cvzone


#Video Processing
cap = cv2.VideoCapture("carPark.mp4")

#Load a Pickel file
with open('CarParkPos', 'rb') as f:
    pos_list = pickle.load(f)

#Width and Height of the bbox
width, height = 107, 48


def check_parking_space(img_prop):

    space_counter = 0

    for pos in pos_list:
        x, y = pos
        img_crop = img_prop[y: y+height, x: x+width]
        # cv2.imshow(str(x * y), img_crop)
        count = cv2.countNonZero(img_crop)


        if count < 1200:
            color = (0, 255, 0)
            thickness = 5
            space_counter += 1
        else:
            color = (0, 0, 255)
            thickness = 2

        cv2.rectangle(img, pos, (pos[0] + width, pos[1] + height), color, thickness)
        cvzone.putTextRect(img, str(count), (x, y + height - 3), scale=1,
                           thickness=2, offset=0, colorR=color)

    cvzone.putTextRect(img, f'Free: {space_counter}/{len(pos_list)}', (100, 50), scale=3,
                           thickness=5, offset=20, colorR=(0,200,0))


while True:

    #Rpeat the Video
    if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)

    #Read the Video
    success, img = cap.read()

    #Change the Video to GrayScale and Blur --> Binary array
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_blur = cv2.GaussianBlur(img_gray, (3, 3), 1)
    img_threshold = cv2.adaptiveThreshold(img_blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                         cv2.THRESH_BINARY_INV, 25, 16)
    img_median = cv2.medianBlur(img_threshold, 5)
    kernel = np.ones((5, 5), np.uint8)
    img_dialate = cv2.dilate(img_median, kernel, iterations = 1)

    #Check parking spaces and show the bbox
    check_parking_space(img_dialate)

    cv2.imshow('img', img)
    # cv2.imshow('img_Thresh', img_median)
    cv2.waitKey(10)