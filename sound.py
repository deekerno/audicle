import librosa as lbr
import librosa.display
import matplotlib.pyplot as plt
import matplotlib.style as sty
import numpy as np

WINDOW_SIZE = 2048
# Stride controls how the window convolves around the input
WINDOW_STRIDE = WINDOW_SIZE // 2 # integer division
N_MELS = 128
MEL_KWARGS = {
	'n_fft': WINDOW_SIZE,
	'hop_length': WINDOW_STRIDE,
	'n_mels': N_MELS
}

class Sound(object):
	"""
	Any time a song is passed to the system, we'll make an object so that
	we can easily access its corresponding characteristics. The numerical
	attributes are being filled with None values at instantiation so that
	we can test if audio processing framework is actually setting the values
	of the object.
	"""
	def __init__(self, filename):
		self.filename = filename
		# librosa_rep is the time series given after loading a file with librosa
		self.librosa_rep = None
		self.samp_rate = None
		self.duration = None 
		self.tempo = None
		self.spectro = None
		# spectro_human is the human-readable version in case we want to present it
		self.spectro_human = None

def load_and_gen(self):
	self.librosa_rep, self.samp_rate = lbr.load(self.filename)
	# ".T" gives the transposed version of the NumPy array
	self.spectro = lbr.feature.melspectrogram(self.librosa_rep, self.samp_rate, **MEL_KWARGS).T

