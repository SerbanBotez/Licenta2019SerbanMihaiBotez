import os
import sys
import fileinput

def crop_annotate(path):

    for line in fileinput.input(path, inplace=True):
        line = line.strip()
        new_line = os.path.join(os.path.split(os.path.split(line)[0])[1], os.path.split(line)[1])
        line = line.replace(line, new_line)
        print(line.strip())

def remove_spaces(path):
    with open(path, 'rb+') as file:
        for line in file:
            if line != b'\r\n':
                file.write(line)
                print(line)

#crop_annotate(r'C:\Users\Serban\Desktop\LicentaResources\anna.txt')
#remove_spaces(r'C:\Users\Serban\Desktop\LicentaResources\anna.txt')
#print('da')

test = '0.25'

test = test.split(',')
x = int(test[0])
y = int(test[1])

print(test, x, y, type(test), type(x), type(y))
