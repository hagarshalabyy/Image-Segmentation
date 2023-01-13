import cv2
import numpy as np
from matplotlib import pyplot as plt

def predict(image):
   
    img = cv2.imread(image)
    resized_img = cv2.resize(img, (960, 540))
    img_gray = cv2.cvtColor(resized_img,cv2.COLOR_BGR2GRAY)
    img_blurred = cv2.GaussianBlur(img_gray,(3,3),0)
    edges  = cv2.Canny(image=img_blurred, threshold1=300, threshold2=250)
    
    lines = cv2.HoughLinesP(edges, 1, np.pi/180, 30, maxLineGap=50)

    copy = img_blurred.copy()

# draw Hough lines
    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv2.line(copy, (x1, y1), (x2, y2), (255, 0, 0), 3)
    
    plt.figure(figsize=(10,10))
    plt.imshow(copy, cmap= "gray")
    plt.show()
