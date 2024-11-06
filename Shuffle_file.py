import os
import random
import shutil

# Define input and output folders
input_folder = r"D:\machine learning\dataset_prepare\Small_nine"
output_folder = r"D:\machine learning\dataset_prepare\Shuffled_files_nine"

# Create output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# List all files in the input folder
file_names = os.listdir(input_folder)

# Shuffle the list of file names
random.shuffle(file_names)

# Function to copy files with shuffled names to the output folder
def shuffle_and_copy_files(input_folder, output_folder, file_names):
    for i, file_name in enumerate(file_names):
        input_file_path = os.path.join(input_folder, file_name)
        output_file_name = f"shuffled_{i}.wav"  # New shuffled file name
        output_file_path = os.path.join(output_folder, output_file_name)
        shutil.copyfile(input_file_path, output_file_path)

# Copy shuffled files to the output folder with new names
shuffle_and_copy_files(input_folder, output_folder, file_names)
