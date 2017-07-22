# Beat tracking example
from __future__ import print_function
import librosa
import numpy as np
import matplotlib.pyplot as plt
import pickle
import json

# based on how long a human ear can actually recognize changes in sound
WINDOW_SIZE = 2048
WINDOW_STRIDE = WINDOW_SIZE // 2
N_MELS = 128
MEL_KWARGS = {
    'n_fft': WINDOW_SIZE,
    'hop_length': WINDOW_STRIDE,
    'n_mels': N_MELS
}

# get the file path to the included audio example
filename = "Lost_Radiance_-_09_-_Look_Around.mp3"

# returns a numpy.ndarray for manipulation
y, sr = librosa.load(filename, mono=True)

# convert to mel spec for better analysis
# this is easier to understand by comparison
melGraph = librosa.feature.melspectrogram(y, **MEL_KWARGS)
print(type(melGraph));
np.log(melGraph);
# simple data logging to test details of input
# print(type(y));
# print(y.size);
# print("max value is");
# print(np.amax(y));
# print("min value is");
# print(np.amin(y));
print(json.dump(melgraph))
