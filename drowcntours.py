import cv2
import numpy as np
from PIL import Image

def show_img(im):
    Image.fromarray(im).show()

def drawContours(img):
    #使用cvtColor（） 函数将原始 RGB 图像转换为灰度图像。
    img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    #show_img(img_gray)
    
    # apply binary thresholding
    ret, thresh = cv2.threshold(img_gray, 150, 255, cv2.THRESH_BINARY)

    # detect the contours on the binary image using cv2.CHAIN_APPROX_NONE CHAIN_APPROX_SIMPLE
    contours, hierarchy = cv2.findContours(image=thresh, mode=cv2.RETR_LIST, method=cv2.CHAIN_APPROX_NONE )
    '''
    RETR_LIST和RETR_EXTERNAL执行所需的时间最少，因为RETR_LIST不定义任何层次结构，
    RETR_EXTERNAL只检索父轮廓
    RETR_CCOMP执行时间第二长。它检索所有轮廓并定义两级层次结构。
    RETR_TREE需要最长时间的执行时间，因为它会检索所有轮廓，并为每个父子关系定义独立的层次结构级别。'''
    print(len(hierarchy))
                                      
    # draw contours on the original image
    image_copy = img.copy()
    cv2.drawContours(image=image_copy, contours=contours, contourIdx=1, color=(0, 255, 0), thickness=1, lineType=cv2.LINE_AA)
    
    show_img(image_copy)



if __name__=='__main__':
    img=cv2.imread('cut/0.jpg') 
    
    drawContours(img)