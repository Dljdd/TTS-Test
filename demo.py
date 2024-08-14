import whisper
from pydub import AudioSegment
import librosa
import numpy as np
import json
import os

def transcribe_and_stretch_audio(input_mp3_file, output_mp3_file, stretch_factor=1.0):
    try:
        # Load the Whisper model
        model = whisper.load_model("base")

        # Transcribe the MP3 file
        transcription = model.transcribe(input_mp3_file)
        text = transcription["text"]
        print(f"Transcribed Text: {text}")

        # Load the MP3 file
        audio = AudioSegment.from_mp3(input_mp3_file)
        audio.export("temp_input.wav", format="wav")

        y, sr = librosa.load("temp_input.wav", sr=None)

        # Stretch the audio
        y_stretched = librosa.effects.time_stretch(y=y, rate=1/stretch_factor)

        # Save the stretched audio as MP3
        librosa.output.write_wav("temp_stretched.wav", y_stretched, sr)
        stretched_audio = AudioSegment.from_wav("temp_stretched.wav")
        stretched_audio.export(output_mp3_file, format="mp3")

        # Generate word-level timestamps based on transcription
        words = text.split()
        duration = librosa.get_duration(y=y_stretched, sr=sr)
        timestamps = np.linspace(0, duration, len(words) + 1)

        # Create a dictionary of word timestamps
        word_timestamps = {words[i]: {"start": timestamps[i], "end": timestamps[i+1]} for i in range(len(words))}

        # Save timestamps to a JSON file
        with open(f"{output_mp3_file[:-4]}_timestamps.json", "w") as f:
            json.dump(word_timestamps, f, indent=2)

        # Clean up temporary files
        os.remove("temp_input.wav")
        os.remove("temp_stretched.wav")

        return word_timestamps

    except Exception as e:
        print(f"Error in transcribe_and_stretch_audio: {str(e)}")
        return None
