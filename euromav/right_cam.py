import numpy as np
# General sensor definitions.
# sensor_type: camera
# comment: VI-Sensor cam1 (MT9M034)

# Sensor extrinsics wrt. the body-frame.
# T_BS:
#   cols: 4
#   rows: 4
T= np.array([[0.0125552670891, -0.999755099723, 0.0182237714554, -0.0198435579556],
         		[0.999598781151, 0.0130119051815, 0.0251588363115, 0.0453689425024],
        		[-0.0253898008918, 0.0179005838253, 0.999517347078, 0.00786212447038],
         		[0.0, 0.0, 0.0, 1.0]],dtype=np.float32)

# Camera specific definitions.
# rate_hz: 20
resolution=np.array([752, 480],dtype=np.float32)
camera_model='pinhole'
intrinsics=np.array([457.587, 456.134, 379.999, 255.238],dtype=np.float32) #fu, fv, cu, cv

# distortion_coefficients
k=np.array([-0.28368365,  0.07451284, -0.00010473, -3.55590700e-05],np.float32)
distortion_model='radial-tangential'