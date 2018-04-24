###########################################################################
## @author: silvanusdavid (130717)										 ##
## 																		 ##
## This program implements FUXZZY C-MEANS CLUSTERING based of the IVIFS  ##
## ########################################################################

from __furure__ import division
import numpy as np

## BEGIN: 
##     IMPORT the data from the .npy files into memeory
memL=np.load('memL.npy')
memU=np.load('memU.npy')
memW=np.load('memW.npy')
nonL=np.load('nonL.npy')
nonU=np.load('nonU.npy')
nonW=np.load('nonW.npy')
## END

# Initializing cluster centers
#V=np.zeros
c=4	# number of cluster centers


## Defining functions
def dist(X1,X2):
	""" calculates the distance between the point X1 and X2"""
	dist=(memL[X1]-memL[X2])**2 + (memU[X1]-memU[X2])**2 + (memW[X1]-memW[X2])**2 + (nonL[X1]-nonL[X2])**2 + (nonU[X1]-nonU[X2])**2 + (nonW[X1]-nonW[X2])**2
	dist=0.5*(dist**0.5)
	return dist

def U(X1):
	for i in range 
	return memVal
