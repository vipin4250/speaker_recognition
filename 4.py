from scipy.io import wavfile
import noisereduce as nr
import os


speaker_folders = ["audio2"]
# speaker_folders = ["Priyanka_chopra_combined"]
speaker_name = [ "Benjamin_Netanyau", "Jens_Stoltenberg", "Julia_Gillard", "Magaret_Tarcher", "Nelson_Mandela", "Narender_modi","Priyanka_chopra"]

input_path = "D:\machine learning\speaker_recognition\input_voices"
speaker_folder_path = os.path.join(input_path, 'temp_audio.wav')
# load data
rate, data = wavfile.read(speaker_folder_path)

output_dir = "input_voices"
os.makedirs(output_dir, exist_ok=True)
recording_file = os.path.join(output_dir, "audio2.wav")

# perform noise reduction
reduced_noise = nr.reduce_noise(y=data, sr=rate)
wavfile.write(recording_file, rate, reduced_noise)