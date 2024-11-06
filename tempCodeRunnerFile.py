from flask import Flask, render_template, request
import os
import numpy as np
import shutil
import librosa
import soundfile as sf
from IPython.display import display, Audio
import librosa.display
import tensorflow as tf




app = Flask(__name__)

@app.route("/")
def hello():
 return "hello world3"

app.run(debug=True)