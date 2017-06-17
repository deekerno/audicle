from flask import Flask, flash, render_template, request
from flask_uploads import patch_request_class
from flask_uploads import UploadSet, AUDIO, UploadConfiguration
import logging
import os
import time
import youtube_dl as ytdl

UPLOADS_DEFAULT_DEST = os.path.join(os.path.dirname(__file__), 'uploads')
YT_DOWNLOADS = os.path.join(os.path.dirname(__file__), 'yt_downloads')


# youtube-dl spits out a metric ton of information, so we define a logging
# object to handle all the spam
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
app.config['UPLOADS_DEFAULT_DEST'] = UPLOADS_DEFAULT_DEST
songs = UploadSet('songs', AUDIO)

UploadConfiguration(app, songs)
patch_request_class(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST' and 'audio' in request.files:
        f = songs.save(request.files['song'])


@app.route('/youtube', methods=['GET', 'POST'])
def youtube():
    if request.method == 'POST':
        song_link = request.form['link']
        print(song_link)
        with ytdl.YoutubeDL(yt_opts) as ydl:
            ydl.download([song_link])
        return render_template('index.html')