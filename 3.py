import numpy as np
import pandas as pd
import os
import shutil
import librosa
import soundfile as sf

# speaker_folders = ["Benjamin_Netanyau","Jens_Stoltenberg","Julia_Gillard","Nelson_Mandela"]
speaker_folders = ["down", "go", "left", "no", "right", "stop", "up", "yes"]
# speaker_folders = [ "Jens_Stoltenberg", "Magaret_Tarcher","Narender_modi","Priyanka_chopra"]

# input_path = "D:\machine learning\speaker_recognition\combined_file "
# input_path = "other"
input_path = "16000_pcm_speeches\data"

output_path = "D:\machine learning\speaker_recognition\others"
# shutil.rmtree(output_path, ignore_errors=True) # remove output folder if it exists
os.makedirs(output_path, exist_ok  = True )

combined_audio = []

for speaker_folder in speaker_folders:
    speaker_folder_path = os.path.join(input_path , speaker_folder)
    wav_files = [f"{i}.wav" for i in range(1400)]
    
    #combined audio 121 files
    

    # for wav_file in wav_files:
    for wav_file in os.listdir(speaker_folder_path):
        wav_file_path = os.path.join(speaker_folder_path, wav_file)
        #loading audio wav file
        audio, sr = librosa.load(wav_file_path, sr= None) # audio(1D numpy array) and sr sampling rate
        combined_audio.extend(audio)
output_file_path = os.path.join(output_path ,f"universal_combined.wav")
sf.write(output_file_path, combined_audio, sr)


# audio, sr = librosa.load("other\Vipin_3.wav", sr= None) # audio(1D numpy array) and sr sampling rate
# combined_audio.extend(audio)
# audio, sr = librosa.load("other\Vipin_4.wav", sr= None) # audio(1D numpy array) and sr sampling rate
# combined_audio.extend(audio)

# output_file_path = os.path.join(output_path ,f"vipin_combined.wav")
# sf.write(output_file_path, combined_audio, sr)


