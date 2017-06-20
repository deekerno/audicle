# Beat tracking example
from __future__ import print_function
import librosa
import numpy as np
import matplotlib.pyplot as plt

# 1. Get the file path to the included audio example
filename = "Lost_Radiance_-_09_-_Look_Around.mp3"

# returns a numpy.ndarray for manipulation
y, sr = librosa.load(filename)
# simple data logging
print(type(y));
print(y.size);
# prints the data from each frame, there are a lot of frames
for i in y:
    print(i);
