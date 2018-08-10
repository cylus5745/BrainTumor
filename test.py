import numpy as np
#import nibabel as nb
import matplotlib.pyplot as plt
#import os

# def get_ordered_file_names(dir_path, suffix):
# 	""" <suffix=STRING> is the file extention of the files in <dir_path=STRING> """
# 	files=os.listdir(dir_path)

# 	# extract the numbers from file names
# 	sorted_int=[]
# 	sorted_str=[]
# 	temp=[]
# 	for f in files:
# 		temp=f.split('.')
# 		sorted_int.append(int(temp[0]))
# 	sorted_int.sort(key=int)

# 	# concatenate the full path after numerically sorting the files in the folder
# 	for s in sorted_int:
# 		temp=dir_path+str(s)+suffix
# 		sorted_str.append(temp)

# 	return sorted_str

# plt.gray()

# file_names=get_ordered_file_names('/root/projects/BrainTumor/brain/', '.nii.gz')
# #file_names=sorted(int(file_names[:-7]), key= int )
# for f in file_names:
# 	ni=nb.load(f)
# 	img=ni.get_data()
# 	print(f)
# 	plt.imshow(img)
# 	plt.show()

# 	choice = input('Enter "1" to move or "0" to not move :')

# 	if choice == 1:

# 		cmd = "mv "+ f +" /root/projects/BrainTumor/newBrain/"

# 		os.system(cmd)

# 	else:
# 		pass

dice=np.load('diceValueF.npy')
plt.ylabel('Dice Coeffecient')
plt.xlabel('Images->')
plt.title('Dice Similarity Coeffecient')
plt.plot(dice,'r-o')
plt.show()

pre=np.load('precisionF.npy')
plt.ylabel('Precision')
plt.xlabel('Images->')
plt.title('Precision')
plt.plot(pre,'g-o')
plt.show()

rec=np.load('recallF.npy')
plt.ylabel('Recall')
plt.xlabel('Images->')
plt.title('Recall')
plt.plot(rec, 'b-o')

plt.show()