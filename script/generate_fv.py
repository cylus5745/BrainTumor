import theano 
import theano.tensor as T
import numpy as np 
import nibabel as nib
import os
import matplotlib.pyplot as plt

def plot(image, title='plot'):
	image=image.flatten()
	plt.plot(image)
	plt.title(title)
	plt.show()

def plot_image(image, title='image'):
	plt.gray()
	plt.imshow(image)
	plt.title(title)
	plt.show()
###########################################
"""All Theano functions are defined here"""
###########################################
#---------- BEGIN ----------
image=T.vector('image' ,'float64')
fs=T.vector('fs','float64')
# mem=T.vector('mem','float32')
# fs_mean=T.scalar('fs_mean')

fs = image/T.max(image)

generate_fs = theano.function(inputs=[image], outputs=[fs])
#---------- END -------------

# loading the .nii files which are pre-processed and skull stripped
data_dir_path='/root/projects/BrainTumor/Nifti_data/'

# file_names=os.listdir(data_dir_path)

# for i in file_names:
# 	absolute_file_path=data_dir_path+i
# 	nib_obj=nib.load(absolute_file_path)


def generate_mem(fs):
	""" this function accepts Image and its corresponding fuzzy set and generates the membership 
	values for each pixel based on the input parameters"""	
	if np.shape(fs)==(1,262144):
		
		mean=np.mean(fs)
		membership_val=0.582*np.expm1(1-abs(fs-mean))

		if np.amin(membership_val)<0 or np.amax(membership_val)>1:
			log.warning('Value Error: membership value out of range')

		else:
			return membership_val

	else:
		log.warning('shape of the Image passed to <generate_membership()> is INVALID!')


absolute_file_path = data_dir_path+'1535.nii'
nib_obj=nib.load(absolute_file_path)
image=nib_obj.get_data()
if np.shape(image)==(512,512):
	flat_image=image.flatten()
	fs=generate_fs(flat_image)
	print(np.shape(fs))
	mem = generate_mem(fs)
	# non = generate_non(mem)
	print(mem, np.amax(mem), np.amin(mem))
	plot(mem, 'membership values')
	plot_image(np.reshape(mem,(512,512)), 'membership image')