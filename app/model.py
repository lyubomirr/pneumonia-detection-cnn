import tensorflow as tf
import numpy as np
from tensorflow import keras

class_names = ["normal", "pneumonia"]
IMAGE_HEIGHT = 180
IMAGE_WIDTH = 180

def _config_memory_growth():
    gpus = tf.config.experimental.list_physical_devices('GPU')
    if gpus:
        try:
            # Currently, memory growth needs to be the same across GPUs
            for gpu in gpus:
                tf.config.experimental.set_memory_growth(gpu, True)
        except RuntimeError as e:
            # Memory growth must be set before GPUs have been initialized
            print(e)

_config_memory_growth()    
model = keras.models.load_model("vgg_transfer_learning")

def predict(filepath):
    img = keras.preprocessing.image.load_img(filepath, target_size=(IMAGE_HEIGHT, IMAGE_WIDTH))
    
    img_array = keras.preprocessing.image.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0) # Create a batch
    
    predictions = model.predict(img_array)
    score = tf.nn.softmax(predictions[0])

    return class_names[np.argmax(score)], 100 * np.max(score)

