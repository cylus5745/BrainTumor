import matplotlib.pyplot as plt
import nibabel as nib
import numpy as np

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

load_file='/home/tumor/tumor/brain_mask/'+'1533'+'.nii.gz'

img_obj=nib.load(load_file)
print(img_obj.header)

img=img_obj.get_data()

plot_image(img, load_file)
