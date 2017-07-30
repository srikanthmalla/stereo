import numpy as np
# General sensor definitions.
# sensor_type: camera
# comment: VI-Sensor cam0 (MT9M034)

# Sensor extrinsics wrt. the body-frame.
# T_BS:
#   cols: 4
#   rows: 4

T=np.array( [[0.0148655429818, -0.999880929698, 0.00414029679422, -0.0216401454975],
         		[0.999557249008, 0.0149672133247, 0.025715529948, -0.064676986768],
       			[-0.0257744366974, 0.00375618835797, 0.999660727178, 0.00981073058949],
         		[0.0, 0.0, 0.0, 1.0]],dtype=np.float32)

# Camera specific definitions.
# rate_hz: 20
resolution=np.array([752, 480],dtype=np.float32)
camera_model= 'pinhole'
intrinsics=np.array([458.654, 457.296, 367.215, 248.375],dtype=np.float32) #fu, fv, cu, cv

# distortion_coefficients
k=np.array([-0.28340811, 0.07395907, 0.00019359, 1.76187114e-05],dtype=np.float32)
distortion_model= 'radial-tangential'

