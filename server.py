from flask import Flask, flash, jsonify, render_template, request
from flask_cors import CORS
from flask_uploads import patch_request_class
from flask_uploads import UploadSet, AUDIO, UploadConfiguration
import json
import logging
import os
import time
import youtube_dl as ytdl

UPLOADS_DEFAULT_DEST = os.path.join(os.path.dirname(__file__), 'uploads')
YT_DOWNLOADS = os.path.join(os.path.dirname(__file__), 'yt_downloads')


class AppLogger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)


yt_opts = {
    # v0: high ratio of quality:size, and won't affect the spectrogram greatly
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '256',
    }]
}

app = Flask(__name__)
CORS(app)
app.config['UPLOADS_DEFAULT_DEST'] = UPLOADS_DEFAULT_DEST
app.debug = True
songs = UploadSet('songs', AUDIO)

# Configuring the app so that only audio uploads are possible. Formats
# include mp3, aac, wav, opus, etc.
UploadConfiguration(app, songs)
patch_request_class(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST' and 'audio' in request.files:
        f = songs.save(request.files['song'])
        file = Song(filename=f, user=None)
        file.store()
        return render_template('index.html')


@app.route('/api/youtube', methods=['GET', 'POST'])
def youtube():
    #if request.method == 'POST':
    #    song_link = request.form['link']
    #    print(song_link)
    #    with ytdl.YoutubeDL(yt_opts) as ydl:
    #        ydl.download([song_link])
    #    return render_template('index.html')
    if request.method == 'POST':
        print(request)
        data = request.get_json()
        song_link = data["url"]
        print(song_link)
        with ytdl.YoutubeDL(yt_opts) as ydl:
            ydl.download([song_link])
        return jsonify({'message': 'YEAHHHHH DAWG'}), 200