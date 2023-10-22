import os

os.environ["CUDA_VISIBLE_DEVICES"] = ""  # Set the environment variable to use CPU only
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"  # Set to suppress INFO-level messages

from tensorflow import keras, io, float32, data as tf_data, constant, image as tf_image
from tensorflow_hub import KerasLayer
from numpy import max, argmax


# Load the classifier model
def load_model():
    model_path = 'mobile_net_final.h5'
    model = keras.models.load_model(model_path, custom_objects={'KerasLayer': KerasLayer})
    return model


def process_image(image_path):
    """
    Takes a filepath to an image and converts the image into a tensor of the appropriate shape for the model.
    """
    # Read the image file:
    image = io.read_file(image_path)
    # Convert the jpg image into a tensor with 3 color channels
    image = tf_image.decode_jpeg(image, channels=3)
    # Normalize the color channels
    image = tf_image.convert_image_dtype(image, float32)
    # Resize the image
    image = tf_image.resize(image, size=[224, 224])
    return image


def create_data_batches(image):
    # If the data is a test image, we will not have a label:
    data = tf_data.Dataset.from_tensor_slices(
        (constant([image])))  # Creates a dataset out of slices of the given tensors using only the filepaths
    data_batch = data.map(process_image).batch(32)  # Applies the process_image() function to the sliced data in batches
    return data_batch


def predict(model, image):
    unique_labels = ['African Honey Bee',
                     'Aphid',
                     'Armyworm Moth',
                     'Brown Marmorated Stink Bug',
                     'Cabbage Looper Moth',
                     'Colorado Potato Beetle',
                     'Corn Earworm Moth',
                     'European Corn Borer Moth',
                     'Five-spotted Hawk Moth',
                     'Flea Beetle',
                     'Fruit Fly',
                     'Japanese Beetle',
                     'Spider Mite',
                     'Thrip',
                     'Western Corn Rootworm Beetle'
                     ]

    batch = create_data_batches(image)
    prediction = model.predict(batch)
    confidence = prediction[0]
    label = unique_labels[argmax(confidence)]
    confidence = max(confidence) * 100
    return label, confidence
