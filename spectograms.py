import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np
import os

# Path to directory with split audio files
input_dir = "output_segments"
output_dir = "spectrograms"
os.makedirs(output_dir, exist_ok=True)

# Process each file
for file in os.listdir(input_dir):
    if file.endswith(".wav"):
        file_path = os.path.join(input_dir, file)
        y, sr = librosa.load(file_path)

        # Generate and save the spectrogram
        plt.figure(figsize=(10, 4))
        spectrogram = librosa.feature.melspectrogram(y=y, sr=sr)
        librosa.display.specshow(librosa.power_to_db(spectrogram, ref=np.max),
                                 sr=sr, x_axis="time", y_axis="mel")
        plt.colorbar(format="%+2.0f dB")
        plt.title(f"Spectrogram of {file}")
        plt.tight_layout()
        output_path = os.path.join(output_dir, f"{os.path.splitext(file)[0]}.png")
        plt.savefig(output_path)
        plt.close()
        print(f"Spectrogram saved for {file}: {output_path}")
