from keras import backend as K
from keras.layers import (
	TimeDistributed,
	LSTM,
	Dense,
	Dropout,
	Input,
	Convolution1D
	MaxPooling1D,
	)
from keras.utils import np_utils
import numpy as np
import os


SEED = 4331    # random seed for the network