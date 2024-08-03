from pydub import AudioSegment

# Load the .wav files
audio1 = AudioSegment.from_wav("my/cloning/critical.wav")
audio2 = AudioSegment.from_wav("my/cloning/critical_2.wav")

# Concatenate the audio files
combined = audio1 + audio2

# Export the combined audio to a new .wav file
combined.export("combined.wav", format="wav")
