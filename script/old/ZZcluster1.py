
from __future__ import division
import numpy as np
import os
import h5py
import logging as log
import sklearn.preprocessing as pre
# save_loc='/root/projects/BrainTumor/data/np_data/part_3/'

# path to the directory containing the dataset
path='/root/projects/BrainTumor/dataset/'
# PRAMETERS used in the functions below are INITIALIZED here
lamda=0.8 # generate_nonmembership()
p=0.1
q=0.1
a=0.1
b=0.1
file_names=os.listdir(path)
## FUNCTION DEFINITIONS

def generate_fs(Image):
	""" this function takes in an Image of shape (512,512) and generates fuzzy values 
	<Image_fs>for each pixel of the Image """
	
	if np.shape(Image)==(512,512):
		
		gl_max=np.amax(Image) 	# MAXIMUM gray level in the Image
		gl_min=np.amin(Image)	# MINIMUM gray level in the Image
		
		return (Image-gl_min)/(gl_max-gl_min)
		log.warning('shape of the Image passed to <generate_fs()> is INVALID!')

def generate_membership(Image_fs):
	""" this function accepts Image and its corresponding fuzzy set and generates the membership 
	values for each pixel based on the input parameters"""	
	if np.shape(Image_fs)==(512,512):
		
		mean=np.mean(Image_fs)
		diff=abs(Image_fs-mean)
		membership_val=0.582*(np.expm1(1-diff))
		# i, j = np.where(membership_val == 1.0000169116046684)
		# print(i,j)
		# z=0.582*((np.exp(1-abs(np.amax(Image_fs)-mean)))-1)
		# z2=0.582*((np.exp(1-abs(np.amin(Image_fs)-mean)))-1)
		# z3=0.582*((np.exp(1-abs(0.0824274115866-mean)))-1)
		# print(z,z2,z3, np.amax(membership_val))
		# return membership_val
		if np.amin(membership_val)<0 or np.amax(membership_val)>1:
			log.warning('Value Error: membership value out of range')
		
		else:
			return membership_val
		
	else:
		log.warning('shape of the Image passed to <generate_membership()> is INVALID!')

def generate_nonmembership(Membership_value):

	if np.shape(Membership_value)==(512,512):
		nonmembership=(1-Membership_value)/(1+lamda*Membership_value)

		if np.amin(nonmembership)<0 or np.amax(nonmembership)>1:
			log.warning('Value Error: nonmembership value out of range')
		else:
			return nonmembership
	else:
		log.warning('shape of the Image passed to <generate_nonmembership()> is INVALID!')

def generate_hesitation(Membership_value,Nonmbership_value):

	if (np.shape(Membership_value)==(512,512) and np.shape(Nonmbership_value)==(512,512)):
		hesitation=(1-Membership_value-Nonmbership_value)

		if np.amin(hesitation)<0 or np.amax(hesitation)>1:
			log.warning('Value Error: hesitation value out of range')
		else:
			return hesitation
	else:
		log.warning('shape of the Image passed to <generate_hesitation()> is INVALID!')

def dist(x1,x2):
	"""where x1,x2 are pixel indices of the image after flattening the image matrix"""
	dist=(memL[x1]-memL[x2])**2 + (memU[x1]-memU[x2])**2 + (memW[x1]-memW[x2])**2 + (nonL[x1]-nonL[x2])**2 + (nonU[x1]-nonU[x2])**2 + (nonW[x1]-nonW[x2])**2
	dist=0.5*(dist**0.5)
	return dist	

# def extended_mem():
# 	# for i in range 0,264143:

# 	# return ext_mem

# def update_centers():

######################################################################################

# for i in file_names:
# absolute_path = path+i

f=h5py.File('/root/projects/BrainTumor/dataset/2000.mat')

Image=f['cjdata/image'][()]
	# print("shape of IMAGE:" + i)
	# print(np.shape(Image))
Image_fs =generate_fs(Image)
# Image_fs=pre.normalize(Image)
Image_mem=generate_membership(Image_fs)
# for i in (1,511):
# 	print(Image[i])
# 	print(Image_fs[i])
Image_nonmem=generate_nonmembership(Image_mem)
Image_hes=generate_hesitation(Image_mem, Image_nonmem)
Image_mem = Image_mem.flatten()
Image_nonmem= Image_nonmem.flatten()
Image_hes= Image_hes.flatten()
print(np.shape(Image_mem))
print(np.shape(Image_nonmem))
print(np.shape(Image_hes))
memL=Image_mem-p*Image_hes
memU=Image_mem+a*Image_hes
nonL=Image_nonmem-q*Image_hes
nonU=Image_nonmem+b*Image_hes
memW=memU-memL
nonW=nonU-nonL
print(dist(10,100001))
# i, j = np.where(Image_mem == 1.0000169116046684)
# print(i,j)

# for a,b in zip(i,j):
# 	print(Image_fs[a][b])
# 	print(Image[a][b])
# 	print(Image_mem[a][b])