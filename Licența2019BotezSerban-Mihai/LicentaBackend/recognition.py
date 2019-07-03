import cv2
from keras.models import load_model
import pickle


#to be UPDATED


def recognize(image_path, model_path, bin_path, width, height):

    image = cv2.imread(image_path)
    output = image.copy()
    image = cv2.resize(image, (int(width), int(height)))

    image = image.astype("float") / 255.0

    image = image.reshape((1, image.shape[0], image.shape[1], image.shape[2]))

    model = load_model(model_path)
    lb = pickle.loads(open(bin_path, "rb").read())

    preds = model.predict(image)

    i = preds.argmax(axis=1)[0]
    label = lb.classes_[i]

    text = "{}: {:.2f}%".format(label, preds[0][i] * 100)
    cv2.putText(output, text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7,
                (0, 0, 255), 2)

    cv2.imshow("Image", output)
    cv2.waitKey(0)


#recognize(r'C:\Users\Serban\Desktop\Licenta\keras-tutorial\images\cat.jpg',
#          r'C:\Users\Serban\Desktop\Licenta\keras-tutorial\output\smallvggnet.model',
#          r'C:\Users\Serban\Desktop\Licenta\keras-tutorial\output\smallvggnet_lb.pickle',
#          64, 64)
