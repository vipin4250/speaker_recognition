import os
import librosa
import numpy as np
import soundfile as sf

# Define input and output paths
# input_folder = r"D:\machine learning\dataset_prepare\Small_three"
# output_folder = r"D:\machine learning\dataset_prepare\Small_nine"
input_folder = r"D:\machine learning\dataset_prepare\16000_pcm_speeches\Background_Noise"
output_folder = r"D:\machine learning\dataset_prepare\three_combined\Background_Noise_three"

# Create output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Function to combine three 1-second samples into one 3-second sample
def combine_samples(input_files, output_file):
    combined_signal = np.zeros(0)
    for file in input_files:
        # Load the 1-second voice sample
        file_path = os.path.join(input_folder, file)
        signal, sr = librosa.load(file_path, sr=None)
        
        # If the sample is shorter than 1 second, pad it with zeros
        if len(signal) < sr:
            signal = np.pad(signal, (0, sr - len(signal)), 'constant')
        
        # Take the first second of the sample
        combined_signal = np.concatenate((combined_signal, signal), axis=None)
    
    # Save the combined signal as a new audio file
    output_file_path = os.path.join(output_folder, output_file)
    sf.write(output_file_path, combined_signal, sr)

# List all files in the input folder
input_files = os.listdir(input_folder)

# Iterate over every three consecutive files
for i in range(0, len(input_files), 3):
    files_to_combine = input_files[i:i+3]
    
    # Combine three 1-second samples into one 3-second sample
    output_file_name = f"Background_{i // 3}.wav"
    # output_file_name = f"combined_{i // 3}.wav"
    combine_samples(files_to_combine, output_file_name)
