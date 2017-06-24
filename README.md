# cop4331
Processes of Object-Oriented Development

## Installation/Requirements
This project requires Python 3+ and makes use of several frameworks, e.g. Flask, Angular, Keras, etc. You'll probably need to have ffmpeg installed and accessible on your system. To setup your environment, please make a new virtualenv using `python -m venv venv` and then activate it by using `source venv/bin/activate`. Then, run `pip install -r requirements.txt`. Note that you may need to have numpy installed first, as one of the packages' dependencies requires it; you can do that by running `pip install numpy` first.

## Major Components
* Angular - app frontend
* Flask - app backend
* Keras - framework for defining our neural networks
* LibROSA - used to generate spectrograms for use in the detection network
* Theano - underlying engine for Keras
* YouTube-dl - used to process YouTube links for download