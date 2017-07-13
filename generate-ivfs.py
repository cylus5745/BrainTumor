#########################################################################
## @author: silvanusdavid (120717)										#
## This program generates IVFS from IFS in a 3 step process				#
## 1. load all required arrays into memory								#
## 2. do the calculations on them										#
## 3. store the result back into the secondary memory					#
#########################################################################

import numpy as np

# INITIALIZE all the PARAMETERS required to use in the program
p=0.1
q=0.1
a=0.1
b=0.1
fiels=1
# 0 for lower limit 1 for upper limit
path_membership='/root/projects/BrainTumor/data/np_data/part_2/Fuzzy-values/membership_value.npy'
path_nonmembership='/root/projects/BrainTumor/data/np_data/part_2/Fuzzy-values/nonmembership_value.npy'
path_hesitation='/root/projects/BrainTumor/data/np_data/part_2/Fuzzy-values/hesitation_value.npy'
save_loc='/root/projects/BrainTumor/data/np_data/part_2/Fuzzy-values/IVFS/'

# WARNING!
# NEED TO WRITE CODE FOR GECKING THE VALIDITY OF THE PARAMETERS
# WHICH ARE ENTERDED BY THE USER

# calculating the membership values
m=np.load(path_membership) # membership values
h=np.load(path_hesitation) # hesitation values

# lower limit
print('loaded the membership and hesitation\nworking on memL')
memL=m-p*h
name=save_loc+'memL'
np.save(name,memL)
#del(memL)
print('done...\nworking on memU ')
# upper limit
memU=m+a*h
del(m)
name=save_loc+'memU'
np.save(name,memU)

# finding Wmem
memW=memU-memL
name=save_loc+'memW'
np.save(name, memW)
del(memW)
del(memL)
del(memU)


# calcuating the non-membership values
n=np.load(path_nonmembership)
print('done... \n loaded nonmembership...\nworking on nonL')

# lower limit
nonL=n-q*h
name=save_loc+'nonL'
np.save(name,nonL)
#del(nonL)
print('done... \nworking on nonU...')

# upper limit
nonU=n+b*h
name=save_loc+'nonU'
np.save(name,nonU)

# calculating Wnon
nonW=nonU-nonL
name=save_loc+'nonW'
np.save(name,nonW)
del(nonW)
del(nonL)
del(nonU)
print('done... \n ')
del(n)
del(h)
