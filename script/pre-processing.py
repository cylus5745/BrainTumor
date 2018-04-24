from scipy import ndimage, signal
import numpy as np
import h5py as h5
import nibabel as nib
import os
# INITIALZING necessary variables

save_loc='/root/projects/BrainTumor/Nifti_data/'
file_path='/root/projects/BrainTumor/dataset/'
sd=1.5	# Standard deviation
weight=0.25	# For unsharp masking and IHC

# list of the file names
file_names=os.listdir(file_path)

for i in file_names:
	# Getting the required data object from path into numpy array
	curr_file=file_path+i
	f=h5.File(curr_file)
	
	image = f['cjdata/image'][()]
	# Applying median filter to the image
	image_med = signal.medfilt(image)
	print('Median filter :'+ i[:-4])
	# Sharpenening the image as median filter removes noise and smoothens the edges
	# So, applying Unsharp masking
	#BEGIN
	blurred = ndimage.gaussian_filter(image_med, sd)
	sharp_image = image_med - weight*blurred
	#END
	print('Unsharp masking :'+i[:-4])
	# Inhomogeniety Correction (IHC)
	# 1. Correcting Intensity Homogeniety
	gaussian_filtered=ndimage.gaussian_filter(image,sd)
	# 2. To retain edge data
	edge=ndimage.sobel(gaussian_filtered)
	# 3. Adding gaussian_filtered+edge to achive IHC
	final=gaussian_filtered+weight*edge
	# 4. Applying thresholding on final to remove negetive pixel values
	flat_final=final.flatten()
	for j in range(0,262143):
		if flat_final[j]<0:
			flat_final[j]=0
	final=np.reshape(flat_final,(512,512))
	print('IHC :'+i[:-4] )

	# Saving them in Nifti format to use them in skull stripping
	image_nib=nib.Nifti2Image(final, affine=np.eye(4))
	nib.save(image_nib, save_loc+i[:-4])
	print('saved as .nii @:' + save_loc+i[:-4] )


##to read the saved file do 
#BEGIN
#nib_obj=nib.load(filename)
#image=nib_obj.get_data()
