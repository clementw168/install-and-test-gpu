""" This script prints information about the TensorFlow installation and trains a model on MNIST. """

import tensorflow as tf
from tensorflow_utils import architecture, get_info
tf.get_logger().setLevel('ERROR')


if __name__=="__main__":


    get_info.tf_info()
    get_info.gpu_info()

    print()

    (x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()



    model = architecture.BaseClassif()
    model.compile(optimizer='adam',
                    loss='sparse_categorical_crossentropy',
                    metrics=['accuracy'])

    model.fit(x_train, y_train, epochs=5, validation_data=(x_test, y_test))

