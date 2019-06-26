import subprocess
import os


def vec_file(info, location, vec, num, width, heigth):
    vec = os.path.join(location, vec)
    vec = vec + '.vec'

    command = 'opencv_createsamples ' + ' -info ' + info +\
              ' -vec ' + vec + ' -num ' + num + ' -width ' + width +\
              ' -heigth ' + heigth
    print(command)
    sprocess = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    stdout = sprocess.communicate()[0]
    print(stdout)


annotations_path = os.path.dirname(r'C:\Users\Serban\Desktop\LicentaResources\annorations.txt')

# trebuie sters C:\Users\Serban\Desktop\LicentaResources la annotations (paty-uri)

vec_file(r'C:\Users\Serban\Desktop\LicentaResources\annotations.txt',
         r'C:\Users\Serban\Desktop\LicentaResources',
         'vecf', '6', '30', '30')


if os.stat(r'C:\Users\Serban\Desktop\LicentaResources\vecf.vec').st_size == 12:
    os.remove(r'C:\Users\Serban\Desktop\LicentaResources\vecf.vec')
