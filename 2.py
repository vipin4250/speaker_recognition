import numpy as np
import pandas as pd
import os
import shutil
import librosa
import soundfile as sf

# speaker_folders = [ "Jens_Stoltenberg", "Magaret_Tarcher","Narender_modi","Priyanka_chopra"]
# speaker_folders = ["Benjamin_Netanyau", "Jens_Stoltenberg", "Julia_Gillard", "Magaret_Tarcher", "Nelson_Mandela", "Narender_modi","Priyanka_chopra"]
speaker_folders = ["vipin"]
# number_of_files = 2
number_of_files = 10

input_path = "16000_pcm_speeches"
# output_path = "D:\machine learning\speaker_recognition\other"
output_path = "D:\machine learning\speaker_recognition\combined_file"
# shutil.rmtree(output_path, ignore_errors=True) # remove output folder if it exists
# os.makedirs(output_path, exist_ok  = True )

for speaker_folder in speaker_folders:
    speaker_folder_path = os.path.join(input_path , speaker_folder)
    wav_files = [f"{i+150}.wav" for i in range(number_of_files)]
    
    #combined audio 121 files
    
    combined_audio = []

    for wav_file in wav_files:
        wav_file_path = os.path.join(speaker_folder_path, wav_file)
        #loading audio wav file
        audio, sr = librosa.load(wav_file_path, sr= None) # audio(1D numpy array) and sr sampling rate
        combined_audio.extend(audio)
        
    output_file_path = os.path.join(output_path ,f"{speaker_folder}_3_combined.wav")
    sf.write(output_file_path, combined_audio, sr)