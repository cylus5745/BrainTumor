from scipy import misc
import matplotlib.pyplot as plt
import h5py
import nibabel as nb
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

def get_file_number(file_):
	temp=file_.split('/')
	temp=temp[-1]
	temp.split('.')
	return (int(temp[0]))

i=1

images_=get_ordered_file_names('/root/projects/BrainTumor/compare/','.png')
#masks_=get_ordered_file_names('/root/projects/BrainTumor/brain/', '.nii.gz')
count=0
plt.gray()
for m in images_:
	print(m)
	count=count+1
	# file_n=get_file_number(m)
	# getting braim image
	# f=h5py.File(m)
	# image=f['cjdata/image'][()]
	# nb_obj=nb.load(m)
	# mask=nb_obj.get_data()
	image = misc.imread(m)

		
	plt.subplot(3,3,i)
	i=i+1
	plt.imshow(image)
	
plt.show()