import os
import librosa
import soundfile as sf

# Define input and output folders
input_folder = r"D:\machine learning\speaker_recognition\16000_pcm_speeches\_background_noise_"
output_folder = r"D:\machine learning\dataset_prepare\three_combined\Background_Noise_three"

# Create output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Function to combine all audio samples into a single audio file
def combine_audio_samples(input_folder, output_file):
    combined_audio = []
    sr = None

    # Iterate over each audio file in the input folder
    for file_name in os.listdir(input_folder):
        file_path = os.path.join(input_folder, file_name)
        audio, sr = librosa.load(file_path, sr=None)
        combined_audio.extend(audio)

    # Save the combined audio as a new audio file
    output_file_path = os.path.join(output_folder, output_file)
    sf.write(output_file_path, combined_audio, sr)

# Combine all audio samples into a single audio file
combined_file_name = "combined_background_noise.wav"
combine_audio_samples(input_folder, combined_file_name)

# Function to split the combined audio into 3-second samples
def split_audio_into_3_sec_samples(combined_file_path, output_folder):
    # Load the combined audio file
    audio, sr = librosa.load(combined_file_path, sr=None)

    # Calculate the number of 3-second samples
    sample_length = sr * 3
    num_samples = len(audio) // sample_length

    # Iterate over each 3-second segment and save as a new audio file
    for i in range(num_samples):
        start_idx = i * sample_length
        end_idx = start_idx + sample_length
        sample = audio[start_idx:end_idx]
        output_file_name = f"noise_{i}.wav"
        output_file_path = os.path.join(output_folder, output_file_name)
        sf.write(output_file_path, sample, sr)

# Split the combined audio into 3-second samples
combined_file_path = os.path.join(output_folder, combined_file_name)
split_audio_into_3_sec_samples(combined_file_path, output_folder)
