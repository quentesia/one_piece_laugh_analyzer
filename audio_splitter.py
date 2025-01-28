from pydub import AudioSegment

# Load your .wav file
audio = AudioSegment.from_wav("all_laughs.wav")

# Timestamps in seconds
timestamps = [(0, 3.29 ), (3.3, 4.85), (4.88, 8.28), (8.3, 10.99), (11.01, 13.65), (13.67, 16.19), (16.21, 17.69), (17.71, 20.43), (21.86, 25.01), (25.03, 29.88), 
              (29.91, 32.59), (32.7, 34.53), (35.55, 37.53), (37.56, 39.69), (39.71, 43.15), (43.17, 44.88), (44.9, 56.6), (56.62, 59.54), (59.6, 61.57), (61.61, 64.32), 
              (64.35, 65.96), (65.98, 69.66), (69.7, 72), (72.1, 82.1), (82.2, 84.52), (86.4, 88.03), (88.05, 89.19), (89.21, 93.83), (93.87, 97.77), (99.07, 101.44), 
              (101.6, 106.1), (106.2, 110.57), (110.7, 112.5), (112.65, 116.68), (116.8, 127), (127.15, 134.6), (135.44, 138.1), (138.24, 139.52), (139.6,144.79), (144.85, 148.89), (149, 151.95),
              (152, 154.41), (154.5, 158.67), (158.7, 162.21), (162.25, 164.08), (164.21, 166.72), (167.7, 173), (173.1, 177.68), (177.7, 180.26), (180.3, 183.62), (183.7, 186.58)]  

#conversion to ms
timestamps_ms = [(int(start * 1000), int(end * 1000)) for start, end in timestamps]

# Split and export
for i, (start, end) in enumerate(timestamps_ms):
    segment = audio[start:end]  # Slice the audio
    segment.export(f"laughs/segment_{i + 1}.wav", format="wav")  # Export segment

print("Splitting complete! Segments saved.")
