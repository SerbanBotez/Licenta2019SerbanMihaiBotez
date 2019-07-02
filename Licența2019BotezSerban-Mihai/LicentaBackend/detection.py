import cv2


def detect_faces(image, classifier, name, scale_factor, min_neigh, min_size):
    img = cv2.imread(image)
    imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    clas = cv2.CascadeClassifier(classifier)

    scale_factor = float(scale_factor)
    min_neigh = int(min_neigh)

    x = min_size.split(',')[0]
    y = min_size.split(',')[1]
    min_size = list()
    x = int(x)
    y = int(y)
    min_size.append(x)
    min_size.append(y)
    min_size = tuple(min_size)

    faces = clas.detectMultiScale(imgray, scaleFactor=scale_factor, minNeighbors=min_neigh, minSize=min_size,
                                  flags=cv2.CASCADE_SCALE_IMAGE)

    response = name + ' #{}'
#   for statement taken from http://www.anit.az/?p=1132
    for (i, (x, y, w, h)) in enumerate(faces):
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
        cv2.putText(img, response.format(i + 1), (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.55, (0, 0, 255), 2)

    cv2.imshow("Image", img)
    cv2.waitKey(0)


# detect_faces(r'C:\Users\Serban\Desktop\LicentaResources\positivecats\cats_00002.jpg',
#             r'C:\Users\Serban\Desktop\LicentaResources\haarcascade_frontalcatface_extended.xml','cat' ,1.1, 10,
#              '40, 40', prinfct=None)


# la cats_00002.jpg gaseste un false negative daca pun 1.01 la scale factor
# la cats_00005.jpg gaseste daca ii pun 1.01 la scale factor
