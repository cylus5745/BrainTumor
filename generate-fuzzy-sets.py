
##########################################################################
## @author: silvanus david  (070717)									##
##																		##
## This program defines the functions needed for generating fuzzy sets  ##
## from the pre-processed Image data to further use it for clustering   ##
## NOTE: the program is designed to be time ineffecient inorder to      ##
## manage the memory effeciency											##
##########################################################################

import os
#import skfuzzy as fuzz
import numpy as np
import logging as log

# PRAMETERS used in the functions below are INITIALIZED here
lamda=0.1 # generate_nonmembership()

# defining all Functions necessary 
def generate_fs(Image):
	""" this function takes in an Image of shape (512,512) and generates fuzzy values 
	<Image_fs>for each pixel of the Image """
	
	if np.shape(Image)==(512,512):
		
		gl_max=np.amax(Image) 	# MAXIMUM gray level in the Image
		gl_min=np.amin(Image)	# MINIMUM gray level in the Image

		# to store the membership values for the 2D MR Image
		#Image_fs=np.zeros((512,512))
		#Image_fs=(Image-glmin)/(gl_max-gl_min)
		#return Image_fs
		return (Image-gl_min)/(gl_max-gl_min)
	else:
		log.warning('shape of the Image passed to <generate_fs()> is INVALID!')

def generate_membership(Image_fs):
	""" this function accepts Image and its corresponding fuzzy set and generates the membership 
	values for each pixel based on the input parameters"""	
	if np.shape(Image_fs)==(512,512):
		mean=np.mean(Image_fs) #  /|\		figure out hoe to calculate mean using restricted equivaleance
							   # /_*_\
		#Membership_value=np.zeros((512,512))
		#Membership_value=0.582*((np.exp(1-abs(Image_fs-mean)))-1)
		#return Membership_value
		return 0.582*((np.exp(1-abs(Image_fs-mean)))-1)

	else:
		log.warning('shape of the Image passed to <generate_membership()> is INVALID!')

def generate_nonmembership(Membership_value):

	if np.shape(Membership_value)==(512,512):
		#Nonmbership_value=np.zeros(512,512)
		#Nonmbership_value=(1-Membership_value)/(1+lamda*Membership_value)
		#return Nonmbership_value
		return (1-Membership_value)/(1+lamda*Membership_value)

	else:
		log.warning('shape of the Image passed to <generate_nonmembership()> is INVALID!')

def generate_hesitation(Membership_value,Nonmbership_value):

	if (np.shape(Membership_value)==(512,512) and np.shape(Nonmbership_value)==(512,512)):
		#Hesitation_value=(1-Membership_value-Nonmbership_value)
		#return Hesitation_value
		return (1-Membership_value-Nonmbership_value)
	else:
		log.warning('shape of the Image passed to <generate_hesitation()> is INVALID!')


#############################################################################
## generating an Intutionistic Fuzzy Set(IFS) for the given Images for later 
## use in developing Interval Valued Intutionistic Fuzzy Set(IVFS) which are used 
## in c-means clustering  for detecting the tumors in the brain scans provided
#############################################################################

# PARAMETERS required are INITIALIZED here
path="/root/projects/BrainTumor/data/np_data/part_2/image_2.npy"						#set this path to the numpy Image datasets stored in Image_X.npy file
fuzzy='/root/projects/BrainTumor/data/np_data/part_2/Fuzzy-values'


# start
Image=np.load(path)
shape=np.shape(Image)


Hesitation_value=np.zeros(shape)

# Image_fs=generate_fs(Image[0])
# Membership_value=generate_membership(Image_fs)
# Nonmbership_value=generate_nonmembership(Membership_value)
# Hesitation_value=generate_hesitation(Membership_value,Nonmbership_value)
for turn in range(1,5):
# only create the array necessart for the particular turn
	if turn==1:
		print('init Image_fs')
		Image_fs=np.zeros(shape)
	elif turn==2:
		print('init Membership')
		Membership_value=np.zeros(shape)
	elif turn==3:
		print('init Nonmembership')
		Nonmembership_value=np.zeros(shape)
	elif turn==4:
		print('init Hesitation')
		Hesitation_value=np.zeros(shape)

	print('-------------------turn :',turn,"-------------------")
	example=0						#to keep a track of the current exaple in the iteration
	while(example<300):
	#For ach example generate on fuzzy set at each turn
		print("Generating Fuzzy Values for EXAMPLE:",example)
		if turn==1:
			Image_fs[example]=Image_fs[example]+generate_fs(Image[example])
		elif turn==2:
			Membership_value[example]=Membership_value[example]+generate_membership(Image_fs[example])
		elif turn==3:
			Nonmembership_value[example]=Nonmembership_value[example]+generate_nonmembership(Membership_value[example])
		elif turn==4:
			Hesitation_value[example]=Hesitation_value[example]+generate_hesitation(Membership_value[example],Nonmembership_value[example])
		example=example+1

	if turn==2:
		temp=fuzzy+'membership_value'
		print('----------Saving MEMBERSHIP----------')
		np.save(temp,Membership_value)
		print('done...')
		del (Image_fs)
	elif turn==3:
		temp=fuzzy+'nonmembership_value'
		print('----------Saving NONMEMBERSHIP----------')
		np.save(temp, Nonmembership_value)
		print('done...')
	elif turn==4:
		temp=fuzzy+'hesitation_value'
		print('----------Saving Hesitation----------')
		np.save(temp, Hesitation_value)
		print('done...')