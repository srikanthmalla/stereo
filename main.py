import cv2
import numpy as np
import euromav.left_cam as L
import euromav.right_cam as R
i_l=cv2.imread('./euromav/left.png')
i_r=cv2.imread('./euromav/right.png')

while (True):	
    cv2.imshow('Left Image',i_l)
    cv2.imshow('Right Image',i_r)
    # cv2.imshow('Left rectify',dstL)
    # cv2.imshow('Right rectify',dstR)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break