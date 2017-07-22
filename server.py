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
YT_DOWNLOADS = os.path.join(os.path.dirname(__file__), 'yt_downloads')

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

def make_stats(song):
    stats = {
        'duration' : song.duration,
        'temp' : song.tempo[0],
        'tuning' : song.tuning
    }
    #stats['duration'] = song.duration
    #stats['tempo'] = song.tempo[0]
    #stats['tuning'] = song.tuning
    #stats['mel_freq'] = song.mel_freq
    return stats
    

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
        return jsonify({'message': 'File uploaded.'}), 200


@app.route('/api/youtube', methods=['GET', 'POST'])
def youtube():
    if request.method == 'POST':
        print(request)
        data = request.get_json()
        song_link = data["url"]
        print(song_link)
        with ytdl.YoutubeDL(yt_opts) as ydl:
            ydl.download([song_link])

        song = sound.Sound('song.mp3')
        song.load_and_gen_obj()
        stats = make_stats(song)
        predictions = recognizer.recognize('song.mp3')
        print(predictions)
        return jsonify({'duration': song.duration, 'temp' : song.tempo[0], 'tuning' : song.tuning}), 200