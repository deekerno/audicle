# beat tracking example
from __future__ import print_function
import librosa
import numpy as np
import matplotlib.pyplot as plt

# get the file path to the included audio example
filename = "Lost_Radiance_-_09_-_Look_Around.mp3"

# load the audio as a waveform `y`
# store the sampling rate as `sr`
y, sr = librosa.load(filename)

# run the default beat tracker
tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)

y_percussive = librosa.effects.hpss(y)
tempo, beats = librosa.beat.beat_track(y=y_percussive, sr=sr)
print(beats);
print('Estimated tempo: {:.2f} beats per minute'.format(tempo))

# convert the frame indices of beat events into timestamps
beat_times = librosa.frames_to_time(beat_frames, sr=sr)

# print('Saving output to beat_times.csv')
librosa.output.times_csv('beat_times.csv', beat_times)
