import numpy as np
import h5py
import matplotlib.pyplot as plt
import os

def get_ordered_file_names(dir_path, suffix):
	""" <suffix=STRING> is the file extention of the files in <dir_path=STRING> """
	files=os.listdir(dir_path)

	# extract the numbers from file names
	sorted_int=[]
	sorted_str=[]
	temp=[]
	for f in files:
		temp=f.split('.')
		sorted_int.append(int(temp[0]))
	sorted_int.sort(key=int)

	# concatenate the full path after numerically sorting the files in the folder
	for s in sorted_int:
		temp=dir_path+str(s)+suffix
		sorted_str.append(temp)

	return sorted_str

dir_='/root/projects/BrainTumor/dataset/'
suff='.mat'

files=get_ordered_file_names(dir_, suff)
count=0
for f in files:
    print('File Number:', f)
    f_obj=h5py.File(f)
    img=f_obj['cjdata/image'][()]

    plt.gray()
    plt.imshow(img)
    plt.show()

    choice = input('Enter "1" to move or "0" to not move :')

    if choice == 1:
      cmd = "mv "+ f +" /root/projects/BrainTumor/data/"
      os.system(cmd)

    else:
      pass
