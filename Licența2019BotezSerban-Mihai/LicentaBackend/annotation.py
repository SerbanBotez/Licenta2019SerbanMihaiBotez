import subprocess
import os
import shutil


def annotate(images, annotations):
    annotations = os.path.join(images, annotations)
    command = 'opencv_annotation ' + ' -annotations ' + annotations + ' -images ' + images
    sprocess = subprocess.Popen(command)


annotate(r'C:\Users\Serban\Desktop\LicentaResources\positivecats',
         r'C:\Users\Serban\Desktop\LicentaResources\annotations.txt')
