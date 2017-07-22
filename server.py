from flask import Flask, flash, jsonify, render_template, request
from flask_cors import CORS
from flask_uploads import patch_request_class
from flask_uploads import UploadSet, AUDIO, UploadConfiguration
import json
import logging
import os
import recognizer
import sound
import time
import unittest
import youtube_dl as ytdl

UPLOADS_DEFAULT_DEST = os.path.join(os.path.dirname(__file__), 'uploads')
# YT_DOWNLOADS = os.path.join(os.path.dirname(__file__), 'yt_downloads')

yt_opts = {
    # 256: high ratio of quality:size, and won't affect the spectrogram greatly
    'format': 'bestaudio/best',
    'outtmpl': 'song.mp4',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '256',
    }]
}

def index_to_genre(index):
    converter = {
        0 : 'Electronic',
        1 : 'Experimental',
        2 : 'Folk',
        3 : 'Hip-Hop',
        4 : 'Instrumental',
        5 : 'International',
        6 : 'Pop',
        7 : 'Rock'
    }

    return converter.get(index, index)

def genre_stat(filename):
        song = sound.Sound(filename)
        song.load_and_gen_obj()
        stats = make_stats(song)
        prediction = recognizer.recognize('song.mp3')
        genre = index_to_genre(prediction)
        return jsonify({'genre' : genre, 'duration': song.duration, 'tempo' : song.tempo[0], 'tuning' : song.tuning}), 200


app = Flask(__name__)
CORS(app)
app.config['UPLOADS_DEFAULT_DEST'] = UPLOADS_DEFAULT_DEST
app.debug = True
songs = UploadSet('songs', AUDIO)

# Configuring the app so that only audio uploads are possible.
# Formats include mp3, aac, wav, opus, etc.
UploadConfiguration(app, songs)
patch_request_class(app)

recognizer = recognizer.Recognizer()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST' and 'audio' in request.files:
        f = songs.save(request.files['song'])
        file = Song(filename=f, user=None)
        file.store()
        
        response = genre_stat(file)
        return response


@app.route('/api/youtube', methods=['GET', 'POST'])
def youtube():
    if request.method == 'POST':
        print(request)
        data = request.get_json()
        song_link = data["url"]
        print(song_link)
        with ytdl.YoutubeDL(yt_opts) as ydl:
            ydl.download([song_link])

        response = genre_stat('song.mp3')
        return response