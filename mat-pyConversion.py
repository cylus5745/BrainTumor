import numpy as np
import os
import h5py

###############################################################################################################################
# This program goes through the .mat file which contain Stuctre 'cjdata' with fields - PID, label, image, tumorBorder, tumorMask
# and converts data in each filed in the <cjdata> into a numpy array and then saves the array in the current directory with 
# respective field names. The path to the dataset is to be mentioned in the <path>.
# If the data is too large to be processed at a time, copy part of the data into the <path> and then assign the value to the <part>
# accordingly
# NOTE: the program is designed to be time ineffecient inorder to manage the memory effeciency
################################################################################################################################

# To store all the data objects of a perticular filed at a time
temp_list=[]
# To store the list of absolute paths of each .mat file
absolute_path=[]

# INITIALIZING VARIABLES

# path to the directory containing the dataset
path='/root/projects/BrainTumor/dataset/'
# list of fields contained in <cjdata>
var_=['PID','label','image','tumorBorder','tumorMask']
# Keeps track of which field is being processed at the time
loop=0
# If not partitioning the data into different parts leave it as 1 
# else assign the partition number
part=1



# list of the file names
file_names=os.listdir(path)

# generating the absolute paths for all the .mat files
for i in file_names:
	absolute_path.append(path+i)

# File names no longer required
del(file_names)

# For eack field loop once
while(loop<5):
	
	field = 'cjdata/'+var_[loop]

	for i in absolute_path:
		f=h5py.File(i)
		temp_list.append(f[field])

	# 0 for PID
	if loop==0:
		PID=np.array(temp_list)
		f.close()
		print('Shape of PID :')
		print(np.shape(PID))
		name='PID_'+str(part)
		#np.save(name,PID)
		del(PID)

	# 1 for label
	if loop==1:
		label=np.array(temp_list,'<u8')
		f.close()
		print('Shape of label :')
		print(np.shape(label))
		name='label_'+str(part)
		np.save(name,label)
		del(label)

	#2 for image
	elif loop==2:
		image=np.array(temp_list)
		f.close()
		print('Shape of image :')
		print(np.shape(image))
		name='image_'+str(part)
		np.save(name,image)
		del(image)

	#3 for tumorBorder	
	elif loop==3:
		tumorBorder=np.array(temp_list)
		f.close()
		print('Shape of tumorBorder :')
		print(np.shape(tumorBorder))
		name='tumorBorder_'+str(part)
		np.save(name,tumorBorder)
		del(tumorBorder)

		#4 for tumorMask
	elif loop==4:
		tumorMask=np.array(temp_list)
		f.close()
		print('Shape of tumorMask :')
		print(np.shape(tumorMask))
		name='tumorMask_'+str(part)
		np.save(name,tumorMask)
		del(tumorMask)

	loop+=1
	# reset temp_list to use it for the next field
	temp_list=[]