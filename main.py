import cv2
import numpy as np
import euromav.left_cam as L
import euromav.right_cam as R
from draw_epipolarlines import * 

left_frame=cv2.imread('./euromav/left.png')
right_frame=cv2.imread('./euromav/right.png')

h, w = left_frame.shape[:2] # both frames should be of same shape

#transformation between two cameras
T=np.matmul(np.linalg.inv(R.transformation),L.transformation)
rotation=T[0:3,0:3]
translation=T[0:3,3]

#Perform stereorectification 
R1, R2, P1, P2, Q, validPixROI1, validPixROI2 = cv2.stereoRectify(L.camera_matrix, L.dist_coeffs, R.camera_matrix, R.dist_coeffs, (w,h), rotation, translation, cv2.CALIB_ZERO_DISPARITY,0, (0,0))
mapxL, mapyL = cv2.initUndistortRectifyMap(L.camera_matrix, L.dist_coeffs, R1, P1, (w,h), cv2.CV_32FC1)
mapxR, mapyR = cv2.initUndistortRectifyMap(R.camera_matrix, R.dist_coeffs, R2, P2, (w,h), cv2.CV_32FC1)
dstL = cv2.remap(left_frame, mapxL, mapyL,cv2.INTER_LINEAR)
dstR = cv2.remap(right_frame, mapxR, mapyR,cv2.INTER_LINEAR)

draw_epipolarlines(left_frame,right_frame)
draw_epipolarlines(dstL,dstR)

# display the images
# while (True):	
    # cv2.imshow('Left Image',img3)
    # cv2.imshow('Right Image',img5)
    # cv2.imshow('Left rectify',dstL)
    # cv2.imshow('Right rectify',dstR)
    # if cv2.waitKey(1) & 0xFF == ord('q'):
    #     break