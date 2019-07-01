import subprocess
import os
import fileinput


def run_command(command):
    p = subprocess.Popen(command,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.STDOUT)
    return iter(p.stdout.readline, '')


def crop_annotate(path):

    for line in fileinput.input(path, inplace=True):
        line = line.strip()
        new_line = os.path.join(os.path.split(os.path.split(line)[0])[1], os.path.split(line)[1])
        line = line.replace(line, new_line)
        print(line.strip())


def create_vec(positives, output, name, number, printfunct=None):

    crop_annotate(positives)
    name = name + '.vec'
    output = os.path.join(output, name)

    f = open(positives, 'rb')
    for line in f:
        line = os.path.join(os.path.split(os.path.split(line)[0])[1], os.path.split(line)[1])
        #print(line)

    #print(positives, output, name, number)

    command = 'opencv_createsamples ' + ' -info ' + positives +\
              ' -vec ' + output + ' -num ' + number

    for line in run_command(command):
        if line.decode() == '':
            break
        if printfunct:
            printfunct(line.decode())


#create_vec(r'C:\Users\Serban\Desktop\LicentaResources\annotd.txt',
#           r'C:\Users\Serban\Desktop\LicentaResources', 'vect', '10')








#annotations_path = os.path.dirname(r'C:\Users\Serban\Desktop\LicentaResources\annorations.txt')

# trebuie sters C:\Users\Serban\Desktop\LicentaResources la annotations (paty-uri)

#vec_file(r'C:\Users\Serban\Desktop\LicentaResources\annotations.txt',
#         r'C:\Users\Serban\Desktop\LicentaResources',
#         'vect', '6', '30', '30')


#if os.stat(r'C:\Users\Serban\Desktop\LicentaResources\vecf.vec').st_size == 12:
#   os.remove(r'C:\Users\Serban\Desktop\LicentaResources\vecf.vec')
