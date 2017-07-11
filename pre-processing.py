from scipy import ndimage
from scipy import signal
from skimage import feature
import matplotlib.pyplot as plt
import numpy as np
import cv2

# INITIALZING necessary variables

path='/root/projects/BrainTumor/data/np_data/part_1/image_1.npy'
kernel=np.array([[-1,-1,-1],[-1,9,-1],[-1,-1,-1]])
standard_deviation=1.5

# getting the required data object from path into numpy array
X=np.load(path)

#------------------------------------------
# have to make this a loop
#------------------------------------------
image=X[678]
plt.gray()
# removing noise in the image
image=signal.medfilt(image)

# sharpenening the image as median filter removes noise and 
# smoothens the edges
image=cv2.filter2D(image, -1, kernel)

# Inhomogeniety Correction (IHC)
# 1.
gaussian_filtered=ndimage.gaussian_filter(image,standard_deviation)
# 2.
edge=ndimage.sobel(X[678])
# 3. Adding gaussian_filtered+edge to achive IHC
image=gaussian_filtered+edge
