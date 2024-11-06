import sounddevice as sd
import soundfile as sf
import os

def record_audio(file_name, duration=15, sample_rate=44100):
    print(f"Recording {duration} seconds of audio...")
    audio = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype='float32')
    sd.wait()
    sf.write(file_name, audio, sample_rate)
    print(f"Audio saved as {file_name}")

def split_audio(input_file, output_dir, segment_duration=1):
    audio, sample_rate = sf.read(input_file)
    num_segments = int(len(audio) / (sample_rate * segment_duration))

    print(f"Splitting audio into {num_segments} {segment_duration}-second segments...")

    for i in range(num_segments):
        start = i * sample_rate * segment_duration
        end = start + sample_rate * segment_duration
        segment = audio[start:end]

        segment_file = os.path.join(output_dir, f"k{i}.wav")
        sf.write(segment_file, segment, sample_rate)

        print(f"Segment {i} saved as {segment_file}")


if __name__ == "__main__":
    # Define paths and parameters

    output_dir = "other"
    os.makedirs(output_dir, exist_ok=True)
    recording_file = os.path.join(output_dir, "rishabh_1.wav")

    # output_split_dir = "16000_pcm_speeches"
    # os.makedirs(output_split_dir, exist_ok=True)
    # recorded_samples_dir = "Vipin" 
    # output_split_dir = os.path.join(output_split_dir, recorded_samples_dir)
    # os.makedirs(output_split_dir, exist_ok=True)
    print("hiiiii")

    # Record audio
    record_audio(recording_file)

    # Split audio into 1-second segments
    # split_audio(recording_file, output_split_dir, segment_duration=1)
