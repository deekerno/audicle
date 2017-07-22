import librosa as lbr
import numpy as np
import ffmpy

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
        self.mel_freq = None
        self.onset_env = None
        self.tempo = None
        self.tuning = None
        self.spectro = None
        # spectro_human is the human-readable version in case we want to present it
        self.spectro_human = None

    def load_and_gen_obj(self):
        print("Loading song.")
        self.librosa_rep, self.samp_rate = lbr.load(self.filename)
        # ".T" gives the transposed version of the NumPy array
        self.spectro = lbr.feature.melspectrogram(self.librosa_rep, self.samp_rate, **MEL_KWARGS).T
        self.duration = lbr.get_duration(self.librosa_rep, self.samp_rate)
        self.onset_env = lbr.onset.onset_strength(self.librosa_rep, self.samp_rate)
        self.tempo = lbr.beat.tempo(self.onset_env, self.samp_rate)
        self.tuning = lbr.estimate_tuning(self.librosa_rep, self.samp_rate)
        #self.mel_freq = lbr.mel_frequencies(40)
        print("Features and spectrogram extracted.")

def load_and_gen(filename, given_shape=None):
    librosa_rep, samp_rate = lbr.load(filename, mono=True)
    mel_spec = lbr.feature.melspectrogram(librosa_rep, **MEL_KWARGS).T

    if given_shape is not None:
        if mel_spec.shape[0] < given_shape[0]:
            delta_shape = (given_shape[0] - mel_spec.shape[0],
                    given_shape[1])
            mel_spec = np.append(mel_spec, np.zeros(delta_shape), axis=0)
        elif mel_spec.shape[0] > given_shape[0]:
            mel_spec = mel_spec[: given_shape[0], :]

    mel_spec[mel_spec == 0] = 1e-6
    return (np.log(mel_spec), float(librosa_rep.shape[0]) / samp_rate)