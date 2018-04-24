from __future__ import division
import os
import numpy as np
import nibabel as nib
import logging as log
import matplotlib.pyplot as plt
# INITIALIZE parameters
 ##BEGIN
c=4		# number of clusters
m=2		# some fuzzyfication factor
tolerence=0.001	# like threshold for error 0.1%
lamda=0.8 	# generate_nonmembership()
file='/root/projects/BrainTumor/brain_mask/2000.nii.gz'
plt.gray()
 ##END

def check_all_elements(arr):
	arr=arr.flatten()
	for i in arr:
		if i!=arr[100000]:
			print('Array is VALID', arr)
			break
		else:
			pass
		
def generate_fs(Image):
	""" this function takes in an Image of shape (512,512) and generates fuzzy values 
	<Image_fs>for each pixel of the Image """
	
	if np.shape(Image)==(512,512):
		
		gl_max=np.amax(Image) 	# MAXIMUM gray level in the Image

		return Image/gl_max
	else:
		log.warning('shape of the Image passed to <generate_fs()> is INVALID!')

def generate_membership(Image_fs):
	""" this function accepts Image and its corresponding fuzzy set and generates the membership 
	values for each pixel based on the input parameters"""	
	if np.shape(Image_fs)==(512,512):
		
		mean=np.mean(Image_fs)
		membership_val=0.582*(np.expm1(1-abs(Image_fs-mean)))
		print('MAXIMUM of membership', np.amax(membership_val))
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
		print('MAXIMUM of hesitation', np.amax(hesitation))
		if np.amin(hesitation)<0 or np.amax(hesitation)>1:
			log.warning('Value Error: hesitation value out of range')
		else:
			return hesitation
	else:
		log.warning('shape of the Membership or Non-membership passed to <generate_hesitation()> is INVALID!')

def gen_FV(mem, non, hes, p=0.1, q=0.1, a=0.1, b=0.1):
	FV=[]		#0:memL, 1:memU, 2:memW, 3:nonL, 4:nonU, 5:nonW
	mem=mem.flatten()
	non=non.flatten()
	hes=hes.flatten()
	memL=(mem-p*hes).flatten()
	print("--> LOG: checking memL")
	check_all_elements(memL)
	memU=(mem+a*hes).flatten() 
	print("--> LOG: cheching memU")
	check_all_elements(memU)
	memW=memU-memL
	print("--> LOG: checking memW")
	check_all_elements(memW)
	nonL=(non-q*hes).flatten()
	print("--> LOG: checking nonL")
	check_all_elements(nonL)
	nonU=(non+b*hes).flatten()
	print("--> LOG: checking nonU")
	check_all_elements(nonU)
	nonW=nonU-nonL
	print("--> LOG: checking nonW")
	check_all_elements(nonW)

	FV.append(memL)		#memL
	FV.append(memU)		#memU
	FV.append(memW)	    #memW
	FV.append(nonL)		#nonL
	FV.append(nonU)		#nonU
	FV.append(nonW)	    #nonW

	return np.asarray(FV)

def distance(FV, x1, x2):
	"""where x1,x2 are pixel indices of the image after flattening the image matrix and FV #0:memL, 1:memU, 2:memW, 3:nonL, 4:nonU, 5:nonW """
	print(FV)
  	dist=(FV[0][x1]-FV[0][x2])**2 + (FV[1][x1]-FV[1][x2])**2 + (FV[2][x1]-FV[2][x2])**2 + (FV[3][x1]-FV[3][x2])**2 + (FV[4][x1]-FV[4][x2])**2 + (FV[5][x1]-FV[5][x2])**2
  	dist=0.5*(dist**0.5)
  	return dist

# def gen_dist_matrix(FV):
#   touched=[]
#   dist=np.zeros((262144, 262144), dtype='float16')
#   for i in (0, 262144):
#     for j in (0, 262144):
#       if [i,j] not in touched or i != j:
#         dist[i][j]=distance(FV, i, j)
#         touched.append([i,j])
#   del(touched)  	 
#   return dist

print("--> LOG: Starting ...")
print("--> LOG: Loading file ...", file)
ni=nib.load(file)
print("--> LOG: Loading Image ...")
image=ni.get_data()
print("--> LOG: done")
print("--> LOG: Caluculating feature vector for \n", image)
print("--> LOG: maximum pixel intensity:", np.amax(image))
print("--> LOG: mean pixel intensity:",np.mean(image))
print("--> LOG: Checking for validity of the image")
check_all_elements(image)
print("--> LOG: calculating fuzzy sets ...")
fs=generate_fs(image)
print(fs)
check_all_elements(fs)
print("--> LOG: calculating membership ...")
mem=generate_membership(fs)
check_all_elements(mem)
print("--> LOG: calculating nonmembership ...")
non=generate_nonmembership(mem)
check_all_elements(non)
print("--> LOG: calculating hesitation ...")
hes=generate_hesitation(mem, non)
check_all_elements(hes)

fv=gen_FV(mem, non, hes)

print("--> LOG: DONE")


img=np.reshape(fv[5], (512, 512))
plt.imshow(img)
plt.show()
