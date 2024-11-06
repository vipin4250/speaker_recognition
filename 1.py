import numpy as np
from recording_helper import record_audio, split_audio
import sounddevice as sd
import soundfile as sf
import os


input_dir = "combined_file"
# input_dir = "other"
os.makedirs(input_dir, exist_ok=True)
recording_file = os.path.join(input_dir, "vipin_7.wav")
# recording_file = os.path.join(input_dir, "jg_2_combined.wav")

# output_split_dir = "input_splits"
output_split_dir = "16000_pcm_speeches" 
os.makedirs(output_split_dir, exist_ok=True)
recorded_samples_dir = "sandwich"
output_split_dir = os.path.join(output_split_dir, recorded_samples_dir)
os.makedirs(output_split_dir, exist_ok=True)
print("hiiii")

split_audio(recording_file, output_split_dir, segment_duration=5)
