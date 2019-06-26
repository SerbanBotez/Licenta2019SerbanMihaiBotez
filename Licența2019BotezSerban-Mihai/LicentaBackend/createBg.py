import os
import sys

path = r'C:\Users\Serban\Desktop\LicentaResources\personneg' #path to iamge folder
foldpath = r'C:\Users\Serban\Desktop\LicentaResources\bg.txt'       #path to new file

f = open(foldpath, 'wt')

for root, dirs, files in os.walk(path):
    for file in files:
        print(os.path.join(root, file))
        f.write(os.path.join(root, file))
        f.write('\n')

