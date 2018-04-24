% getting the list of filenames into 'files'

files=dir('*.mat')

% processing each image at a time and storing it in 'new' directory

for file=files
load(file(1,1).name)

% dumbass file is a structure and when you are refering them you have tou refer as if they are in a matrix 
% using their positional parameters

% preprocessing part
img=medfilt2(cjdata(1,1).image)
img=imsharpen(img)
img=anisoOS(img)    //BUG!--------------------------!-!-!-!-!-!-!-!-!-BUG!! :change image to double

% saving the preprocessed image in the 'new directory'
temp=strcat('new/', file(1,1).name)
save(temp, cjdata, '-v7.3')
end
