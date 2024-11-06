import os
import subprocess

# Input and output directories
input_dir = "D:/machine learning/speaker_recognition/16000_pcm_speeches"
output_dir = "Norm_16000_pcm_speeches"
speaker_folders = ["vipin"]
# speaker_folders = ["Benjamin_Netanyau", "Jens_Stoltenberg", "Julia_Gillard", "Magaret_Tarcher", "Nelson_Mandela", "Narender_modi","Priyanka_chopra"]


# Create the output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

for speaker_folder in speaker_folders:
    speaker_folder_path = os.path.join(input_dir , speaker_folder)
    output_dirse = output_dir+"/"+speaker_folder
    subprocess.run(f"mkdir -p \"{output_dirse}\"", shell=True)
    for filename in os.listdir(speaker_folder_path):
        if filename.endswith(".wav") or filename.endswith(".mp3"):  # Adjust extensions as needed
            input_file = os.path.join(input_dir+"/"+speaker_folder, filename)
            
            output_file = os.path.join(output_dir+"/"+speaker_folder, filename)
            # Construct FFmpeg command to process the audio file
            command = f"ffmpeg-normalize \"{input_file}\" -o \"{output_file}\""
            # Execute FFmpeg command using subprocess
            subprocess.run(command, shell=True)

print("Audio conversion completed.")
