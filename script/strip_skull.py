from __future__ import division
import os
import numpy as np
import nibabel as nib

#INITIALIZING VARIABLES
file_path='/home/tumor/tumor/Nifti_data/'
save_loc='/home/tumor/tumor/brain_mask/'
count=1
file_names=os.listdir(file_path)
saved_files=os.listdir(save_loc)
SIZE=len(file_names)
SIZE_SAVED=len(saved_files)/2	# /2 because there is image and imagemask in the saved location

for filename in file_names:
  
  if filename not in saved_files:				# the if statement is added as the process was stopped midway by some retard and few of the file were already skullstripped
    # declaring the path for opening and saving the file 
    abs_path=file_path+filename
    save_as=save_loc+filename
  
    # calculating the threshold value for the image
    img_obj=nib.load(abs_path)
    image=img_obj.get_data()
    threshold=np.mean(image)/1000
    print('--> LOG: mean calculated for '+filename+' :'+str(threshold))
  
    #Running fsl-BET2 Robust brain extraction tool
    print('--> LOG: Running fsl-BET2 Robust brain extraction tool')
    bashcmd='bet'+' '+abs_path+' '+save_as+' '+'-R -f'+' '+str(threshold)+' '+'-g 0 -c 0256 0256 0 -m -t'
    print('--> LOG: handover to fsl')
    os.system(bashcmd)
    print('--> LOG: return from fsl ...')
    print('--> LOG: Brain Extraction tool exited normally. \n Finished... ')
    left=SIZE-count-SIZE_SAVED
    print('--> LOG: Number of images LEFT = '+ str(left))
    print('===============================================================')
    count=count+1

print('strip_skull exited normaly. \n Finidhed ...')
