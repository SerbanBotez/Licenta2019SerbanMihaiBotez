import subprocess
import os



def annotate(images, output, name, height, refactor):


    name = name + '.txt'
    output = os.path.join(output, name)

    command = 'opencv_annotation ' + ' -annotations ' + output + ' -images ' + images \
                + ' -maxWindowHeight' + height + ' -resizeFactor ' + refactor
    sprocess = subprocess.Popen(command)



