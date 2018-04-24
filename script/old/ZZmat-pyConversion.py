
######################################################################################################################################
## @author: silvanusdavid 																											##
##																																	##
## This program goes through the .mat file which contain Stuctre 'cjdata' with fields - PID, label, image, tumorBorder, tumorMask   ##
## and converts data in each filed in the <cjdata> into a numpy array and then saves the array in the current directory with        ##
## If the data is too large to be processed at a time, copy part of the data into the <path> and then assign the value to the <part>##
## accordingly																													    ##	
## NOTE: the program is designed to be time ineffecient inorder to manage the memory effeciency                                     ##
######################################################################################################################################

import numpy as np
import os
import h5py

# To store all the data objects of a perticular file at a time
temp_list=[]
# To store the list of absolute paths of each .mat file
absolute_path=[]
save_loc='/root/projects/BrainTumor/data/np_data/part_3/'

# INITIALIZING VARIABLES
zzz=1
# path to the directory containing the dataset
path='/root/projects/BrainTumor/dataset/'
# list of fields contained in <cjdata>
#var_=['PID','label','image','tumorBorder','tumorMask']
var_=['label','image','tumorMask']
# Keeps track of which field is being processed at the time
loop=0

# list of the file names
file_names=os.listdir(path)

# generating the absolute paths for all the .mat files
for i in file_names:
	absolute_path.append(path+i)

# File names no longer required
del(file_names)

# For eack field loop once
while(loop<3):
	print('------------------LOOP:',loop)
	field = 'cjdata/'+var_[loop]
	print(field)
	for i in absolute_path:
		flag=1
		f=h5py.File(i)
		temp=f[field][()]
		if loop == 1 or loop ==2:
			if len(temp)==256:
				flag=0
		if flag==1:
			temp_list.append(temp)

	# # 0 for PID
	# if loop==0:
	# 	PID=np.array(temp_list)
	# 	f.close()
	# 	print('Shape of PID :')
	# 	print(np.shape(PID))
	# 	name='PID_'+str(part)
	# 	#np.save(name,PID)
	# 	del(PID)

	# 1 for label
	if loop==0:
		label=np.array(temp_list,'<u2')
		temp_list=[]
		f.close()
		print('Shape of label :')
		print(np.shape(label))
		name=save_loc+'label'
		print('saving label as array...')
		np.save(name,label)
		print('done ...\ndeleting list')
		del(label)

	#2 for image
	elif loop==1:
		image=np.array(temp_list,dtype='int16')
		temp_list=[]
		f.close()
		print('Shape of image :')
		print(np.shape(image))
		name=save_loc+'image'
		print('saving image as array ...')
		np.save(name,image)
		print('done ...\ndeleting list')
		del(image)

	# #3 for tumorBorder	
	# elif loop==3:
	# 	tumorBorder=np.array(temp_list)
	# 	f.close()
	# 	print('Shape of tumorBorder :')
	# 	print(np.shape(tumorBorder))
	# 	name=save_loc+'tumorBorder'
	# 	print('saving tumorBorder as array ...')
	# 	np.save(name,tumorBorder)
	# 	print('done ...\ndeleting list')
	# 	del(tumorBorder)

		#4 for tumorMask
	elif loop==2:
		tumorMask=np.array(temp_list,dtype='<u8')
		temp_list=[]
		f.close()
		print('Shape of tumorMask :')
		print(np.shape(tumorMask))
		name=save_loc+'tumorMask'
		print('saving tumorMask as array ...')
		np.save(name,tumorMask)
		print('done ...\ndeleting list')
		del(tumorMask)

	else:
		print('<loop> (required_fields) OUT OF BOUND.')

	loop+=1
	# reset temp_list to use it for the next field
	print("'temp_list' reset ...\n")