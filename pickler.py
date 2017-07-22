import os
import numpy as np
import pandas as pd
import sklearn as skl
import sklearn.utils, sklearn.preprocessing, sklearn.decomposition, sklearn.svm
import pickle
import sound
import unittest

AUDIO_DIR = '/media/stuff/fma_small'
GENRES = ['Electronic', 'Experimental', 'Folk', 'Hip-Hop', 'Instrumental', 'International', 'Pop', 'Rock']
NUM_TRACKS = 8000
SAMPLE_FILE = '000002.mp3'
TRACKS = 'tracks.csv'

class PicklerTest(unittest.TestCase):
	def test_dataset_exists(self):
		self.assertTrue(os.path.exists(AUDIO_DIR), 'Missing dataset!')

	def test_sample_exists(self):
		self.assertTrue(os.path.isfile(SAMPLE_FILE), 'Missing sample file!')

	def test_track_info_exists(self):
		self.assertTrue(os.path.isfile(TRACKS), 'Missing track information!')


def genre_to_index(genre):
	converter = {
		'Electronic' : 0,
		'Experimental' : 1,
		'Folk' : 2,
		'Hip-Hop' : 3,
		'Instrumental' : 4,
		'International' : 5,
		'Pop' : 6,
		'Rock' : 7
	}

	return converter.get(genre, genre)

# Dataset is organized by numbers, not genres
def get_audio_path(audio_dir, track_id):
    tid_str = '{:06d}'.format(track_id)
    return os.path.join(audio_dir, tid_str[:3], tid_str + '.mp3')

# To ensure all mel-spectrograms are the same size 
def get_default_shape():
	default_shape, _ = sound.load_and_gen(SAMPLE_FILE)
	return default_shape.shape

# Load information about all tracks
tracks = pd.read_csv(TRACKS)

# Define parameters in order to filter entire dataset metadata
tracks_dict = {
    "Unnamed: 0" : "val1",	# track_id
    "track.7" : "val2",		# general genre
    "track.8" : "val3",		# numerical genre representation
    "set" : "val4",			# training split
    "set.1" : "val5"		# subset of total dataset
}

# Remove extraneous columns and any tracks that aren't in the fma_small dataset
tracks_filtered = tracks.filter(items=tracks_dict.keys())
tracks_filtered = tracks_filtered.loc[tracks_filtered['set.1'] == 'small']

def compile_data():
	default_shape = get_default_shape()
	x = np.zeros((NUM_TRACKS,) + default_shape, dtype=np.float32)
	y = np.zeros((NUM_TRACKS, len(GENRES)), dtype=np.float32)
	paths = {}
	track_index = 0

	for row in tracks_filtered.itertuples(index=False):		
		
		if isinstance(row._0, str):
			track = int(row._0)
		else:
			track = row._0

		if track == 99134 or track == 108925 or track == 133297:	# broken file
			continue

		path = get_audio_path(AUDIO_DIR, track)
		print("Now processing: " + path + "(" + str(track_index) + ")")
		genre_index = genre_to_index(row._1)
		x[track_index], _ = sound.load_and_gen(path, default_shape)
		y[track_index, genre_index] = 1
		paths[track_index] = os.path.abspath(path)
		track_index = track_index + 1
		# row._0 is the track_id
		# row._1 is the genre
		# row._2 is the genre list
		# row._3 is the split
		# row._4 is the subset

	return (x, y, paths)

(x, y, paths) = compile_data()

data = {'x' : x, 'y' : y, 'paths' : paths}

with open('data.pkl', 'wb') as f:
	pickle.dump(data, f)