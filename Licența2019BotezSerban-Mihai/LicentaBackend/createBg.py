import os


def createbg(neg_path, location, name, printfunct=None):
    name = name + '.txt'
    location = os.path.join(location, name)
    f = open(location, 'wt')

    for root, dirs, files in os.walk(neg_path):
        for file in files:
            if printfunct:
                printfunct(os.path.join(root, file))

            f.write(os.path.join(root, file))
            f.write('\n')
        if printfunct:
            printfunct('Created the negative images paths file')


