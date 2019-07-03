import pickle

import cv2
import os
from imutils import paths
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelBinarizer
from sklearn.metrics import classification_report
from keras.preprocessing.image import ImageDataGenerator
from keras.optimizers import SGD
import matplotlib.pyplot as plt
import numpy as np
import LicentaBackend.model_arhitecture

# script adapted after the tutorial at:
# https://www.pyimagesearch.com/2018/09/10/keras-tutorial-how-to-get-started-with-keras-deep-learning-and-python/


def create_mod(training, model_loc, binary, plot, epochs, train_test, batch_sz, printfct=None):

    images = []
    labels = []

    #data = r'C:\Users\Serban\Desktop\Licenta\keras-tutorial\animals'
    data = training

    Path = sorted(list(paths.list_images(data)))

    # flatten se executa automat intr-un CNN, iar dimensiunile cerute de VGG sunt 64x64
    nr = 0
    for path in Path:
        image = cv2.imread(path)
        image = cv2.resize(image, (64, 64))
        images.append(image)
        label = path.split(os.path.sep)[-2]
        labels.append(label)

    images = np.array(images, dtype="float") / 255.0
    labels = np.array(labels)

    (trainX, testX, trainY, testY) = train_test_split(images, labels, test_size=float(train_test), random_state=42)

    lb = LabelBinarizer()
    trainY = lb.fit_transform(trainY)
    testY = lb.transform(testY)

    aug = ImageDataGenerator(rotation_range=30, width_shift_range=0.1,
                             height_shift_range=0.1, shear_range=0.2, zoom_range=0.2,
                             horizontal_flip=True, fill_mode="nearest")

    model = LicentaBackend.model_arhitecture.build_model(64, 64, 3, classes=len(lb.classes_))

    INIT_LR = 0.01
    EPOCHS = int(epochs) # (75)
    BS = int(batch_sz)  # (32)

    if printfct:

        printfct("[INFO] training network...")
        opt = SGD(lr=INIT_LR, decay=INIT_LR / EPOCHS)
        model.compile(loss="categorical_crossentropy", optimizer=opt, metrics=["accuracy"])

        H = model.fit_generator(aug.flow(trainX, trainY, batch_size=BS), validation_data=(testX, testY),
                            steps_per_epoch=len(trainX) // BS, epochs=EPOCHS)

        printfct("[INFO] evaluating network...")
        predictions = model.predict(testX, batch_size=32)
        print(classification_report(testY.argmax(axis=1),
                                    predictions.argmax(axis=1), target_names=lb.classes_))

    # plot the training loss and accuracy
    N = np.arange(0, EPOCHS)
    plt.style.use("ggplot")
    plt.figure()
    plt.plot(N, H.history["loss"], label="train_loss")
    plt.plot(N, H.history["val_loss"], label="val_loss")
    plt.plot(N, H.history["acc"], label="train_acc")
    plt.plot(N, H.history["val_acc"], label="val_acc")
    plt.title("Training Loss and Accuracy (VGGNet)")
    plt.xlabel("Epoch #")
    plt.ylabel("Loss/Accuracy")
    plt.legend()
    plt.savefig(plot)

    # save the model and label binarizer to disk
    if printfct:
        printfct("[INFO] serializing network and label binarizer...")
    model.save(model_loc)
    f = open(binary, "wb")
    f.write(pickle.dumps(lb))
    f.close()
