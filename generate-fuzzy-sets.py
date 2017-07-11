##########################################################################
## @author: silvanus david  (070717)									##
##																		##
## This program defines the functions needed for generating fuzzy sets  ##
## from the pre-processed image data to further use it for clustering   ##
##########################################################################

import os
#import skfuzzy as fuzz
import numpy as np
import logging as log

# PRAMETERS used in the functions below are INITIALIZED here
lamda=0.1 # generate_nonmembership()

# defining all Functions necessary 
def generate_fs(image):
""" this function takes in an image of shape (512,512) and generates fuzzy values <image_fs>
for each pixel of the image """
	
	if np.shape(image)==(512,512):
		
		gl_max=np.amax(image) 	# MAXIMUM gray level in the image
		gl_min=np.amin(image)	# MINIMUM gray level in the image

		# to store the membership values for the 2D MR image
		#image_fs=np.zeros((512,512))
		#image_fs=(image-glmin)/(gl_max-gl_min)
		#return image_fs
		return (image-glmin)/(gl_max-gl_min)
	else:
		log.warning('shape of the image passed to <generate_fs()> is INVALID!')

def generate_membership(image_fs):
""" this function accepts image and its corresponding fuzzy set and generates the membership 
values for each pixel based on the input parameters"""	
	if np.shape(image_fs)==(512,512):
		mean=np.mean(image_fs) #  /|\		figure out hoe to calculate mean using restricted equivaleance
							   # /_*_\
		#membership_value=np.zeros((512,512))
		#membership_value=0.582*((np.exp(1-abs(image_fs-mean)))-1)
		#return membership_value
		return 0.582*((np.exp(1-abs(image_fs-mean)))-1)

	else:
		log.warning('shape of the image passed to <generate_membership()> is INVALID!')

def generate_nonmembership(membership_value):

	if np.shape(membership_value)==(512,512):
		#nonmembership_value=np.zeros(512,512)
		#nonmembership_value=(1-membership_value)/(1+lamda*membership_value)
		#return nonmembership_value
		return (1-membership_value)/(1+lamda*membership_value)

	else:
		log.warning('shape of the image passed to <generate_nonmembership()> is INVALID!')

def generate_hesitation(membership_value,nonmembership_value):

	if np.shape(membership_value)==(512,512) && np.shape(nonmembership_value)==(512,512):
		#hesitation_value=(1-membership_value-nonmembership_value)
		#return hesitation_value
		return (1-membership_value-nonmembership_value)
	else:
		log.warning('shape of the image passed to <generate_hesitation()> is INVALID!')


#############################################################################
## generating an Intutionistic Fuzzy Set(IFS) for the given images for later 
## use in developing Interval Valued Intutionistic Fuzzy Set(IVFS) which are used 
## in c-means clustering  for detecting the tumors in the brain scans provided
#############################################################################

# PARAMETERS required are INITIALIZED here
#path=""						#set this path to the numpy image datasets stored in image_X.npy file
example=0						#to keep a track of the current exaple in the iteration
files= os.listdir(path)
#IMAGE_FS=[]
#IMAGE_FS=np.asarray(IMAGE_FS)
#MEMBERSHIP_VALUE=[]
#MEMBERSHIP_VALUE=np.asarray(MEMBERSHIP_VALUE)
#NONMEMBERSHIP_VALUE=[]
#NONMEMBERSHIP_VALUE=np.asarray(NONMEMBERSHIP_VALUE)
#HESITATION_VALUE=[]
#HESITATION_VALUE=np.asarray(HESITATION_VALUE)
# start
IMAGE=np.load(path)

IMAGE_FS=generate_fs(IMAGE[0])
MEMBERSHIP_VALUE=generate_membership(IMAGE_FS)
NONMEMBERSHIP_VALUE=generate_nonmembership(MEMBERSHIP_VALUE)
HESITATION_VALUE=generate_hesitation(MEMBERSHIP_VALUE,NONMEMBERSHIP_VALUE)

for i in range(1,len(IMAGE)):	# starts from 1 as fuzzy values are already calculated for IMAGE[0] the first image is already 
	IMAGE_FS=np.vstack([IMAGE_FS,generate_fs(IMAGE[i])])
	MEMBERSHIP_VALUE=np.vstack([MEMBERSHIP_VALUE,generate_membership(IMAGE_FS[i])])
	NONMEMBERSHIP_VALUE=np.vstack([NONMEMBERSHIP_VALUE,generate_nonmembership(MEMBERSHIP_VALUE[i])])
	HESITATION_VALUE=np.vstack([HESITATION_VALUE,generate_hesitation(MEMBERSHIP_VALUE[i],NONMEMBERSHIP_VALUE[i])])

