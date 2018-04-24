import numpy as np
import nibabel as nb
import sys

filename=sys.argv[1]
img_obj=nib.load(filename)
image=img_obj.get_data()
mean=np.mean(image)

print(mean)

