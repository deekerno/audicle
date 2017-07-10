from keras import backend as K
from keras.layers import (
	Activation,
	Conv1D,
	Dense,
	Dropout,
	Input,
	LSTM,
	MaxPooling1D,
	TimeDistributed,
	)
from keras.optimizers import Adam
from keras.utils import np_utils
from sklearn.model_selection import train_test_split as tts
import numpy as np
import os


SEED = 4331    # random seed for the network
NUM_LAYERS = 3 # number of conv-act-pool layers before dropout
FILTER_LENGTH = 5
CONV_FILTER_COUNT = 256
LSTM_COUNT = 256
BATCH_SIZE = 32
EPOCH_COUNT = 100