# cop4331
Processes of Object-Oriented Development

## Installation/Requirements
This project requires Python 3+ and makes use of several frameworks, e.g. Flask, Angular, Keras, etc. It assumes you are using a Unix-based system. You'll also probably need to have ffmpeg installed and accessible on your system. To setup your environment, please make a new virtualenv using `python -m venv venv` and then activate it by using `source venv/bin/activate`. Then, run `pip install -r requirements.txt`. Note that you may need to have numpy installed first, as one of the packages' dependencies requires it; you can do that by running `pip install numpy` first.

## Run the App
To run the web app, please open two shells and run the following commands.

First shell:
1. `cd static`
2. `ng serve`

Second shell:
1. `export FLASK_APP=server.py`
2. `flask run`

[add more instructions as we get closer to finishing]

## Major Components
* A-Frame - visualisation engine
* Angular - app frontend
* Flask - app backend
* Keras - framework for defining our neural networks
* LibROSA - used to generate spectrograms for use in the detection network
* Tensorflow - underlying engine for Keras
* YouTube-dl - used to process YouTube links for download

## Other Stuff
We used the [Free Music Archive](https://github.com/mdeff/fma) to train the genre detection neural network; the `fma_small` dataset was chosen as it contains a total of 8000 30-second tracks balanced across eight (8) genres, including newly popular ones such as electronic(a).