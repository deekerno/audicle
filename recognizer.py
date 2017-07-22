import os
import numpy as np
import sound
from keras.layers import Input
from keras.models import model_from_yaml, Model
from keras import backend as K
from keras.layers import Layer
import unittest

MODEL = 'model.yaml'
WEIGHTS = 'weights.h5'

class RecognizerTest(unittest.TestCase):
    def test_model_exists(self):
        self.assertTrue(os.path.isfile(MODEL), 'Neural network not yet constructed!')

    def test_track_info_exists(self):
        self.assertTrue(os.path.isfile(WEIGHTS), 'Neural network untrained!')


# Grabs the output of whichever layer is named as a parameter.
def get_output_function(model, name_layer):
    input = model.get_layer('input').input
    output = model.get_layer(name_layer).output
    f = K.function([input, K.learning_phase()], [output])
    return lambda x: f([x, 0]) # learning_phase = 0 means test


# This is so that model_from_yaml reads in our custom layer.
class Time_Dist_Merge(Layer):
    def __init__(self, **kwargs):
        super(Time_Dist_Merge, self).__init__(**kwargs)

    def call(self, x):
        return K.mean(x, axis=1)

    def get_config(self):
        return super(Time_Dist_Merge, self).get_config()


class Recognizer():
    # Load model with our class for our custom layer and set
    # output function to the last layer of the network.
    def __init__(self):
        with open(MODEL, 'r') as f:
            model = model_from_yaml(f.read(), custom_objects={"Time_Dist_Merge":Time_Dist_Merge})
        model.load_weights(WEIGHTS)
        self.pred_fun = get_output_function(model, 'time__dist__merge_1')
        print("Loaded model.")
    
    def recognize(self, song):
        print("Analyzing song...")
        (features, duration) = sound.load_and_gen(song)
        features = np.reshape(features, (1,) + features.shape)
        predictions = self.pred_fun(features)
        return np.argmax(predictions)   # returns the index of largest element