import subprocess


# function taken from 'https://stackoverflow.com/questions/4760215/running-shell-command-and-capturing-the-output'
def run_command(command):
    p = subprocess.Popen(command,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.STDOUT)
    return iter(p.stdout.readline, '')


def detect(data, vec, bg, pos, neg, stage, width, height, printfct=None):

    train_haar_classifier = 'opencv_traincascade' + ' -data ' + data + ' -vec ' + vec + ' -bg ' \
                           + bg + ' -numPos ' + pos + ' -numNeg ' + neg + ' -numStages ' \
                           + stage+ ' -w ' + width + ' -h ' + height

    for line in run_command(train_haar_classifier):
        if line.decode() == '':
            break
        #print(line.decode())
        if printfct:
            printfct(line.decode())


#detect(r'C:\Users\Serban\Desktop\LicentaResources\Data', r'C:\Users\Serban\Desktop\LicentaResources\vecf.vec',
#       r'C:\Users\Serban\Desktop\LicentaResources\bg.txt', '6', '1200', '5', '24', '24')



#trebuie pus 24 24 la height weight pentru a nu da assertion error.
#se transforma el automat la 24 24 cumva cand se creaza vector file