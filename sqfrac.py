import matplotlib.pyplot as plt
import numpy as np
import random

triX=[0,1500,1500,0,0]
triY=[0,0,1500,1500,0]

## co-ordinates of the starting points
startX=[500]
startY=[500]

## to randomly choose from the shuffled dice array
ind=[0,1,2,3]
## Dice values
dice=[1,2,3,4]
prev = 10
i=0
## equivalent to shuffling the dice
def get_random():
	random.shuffle(dice)
	random.shuffle(ind)
	return dice[ind[3]]

plt.figure()
## plotting the triangle
plt.plot(triX, triY)

## starting the iterations
while i<500000:
	i=i+1
	## rolling the dice
	temp=get_random()

	if prev == temp:
		continue

	## verbose for cli
	print(i, '-->', temp)
	
	## getting index of the current point on co-0rdinate system
	index=len(startX)-1
	tempX=startX[index]
	tempY=startY[index]

	## updating the current point and storing it inthe array to plot later
	if temp == 1 :
		startX.append((tempX+triX[0])/2)
		startY.append((tempY+triY[0])/2)

	if temp == 2 :
		startX.append((tempX+triX[2])/2)
		startY.append((tempY+triY[2])/2)

	if temp == 3 :
		startX.append((tempX+triX[1])/2)
		startY.append((tempY+triY[1])/2)	

	if temp == 4:
		startX.append((tempX+triX[3])/2)
		startY.append((tempY+triY[3])/2)

	prev=temp
## plotting the graph of all the locations of the point traversed on the co-ordinate plane
plt.scatter(startX, startY)
plt.show()
