from TTS.utils.manage import ModelManager
from TTS.utils.synthesizer import Synthesizer
import librosa
import numpy as np
from pydub import AudioSegment
import json
import os
import torch
from TTS.api import TTS

tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2")

# Your existing code
path = "/Users/dylanmoraes/Documents/GitHub/TTS-Test/virtualenv/lib/python3.11/site-packages/TTS/.models.json"
model_manager = ModelManager(path)

print("Downloading model...")
model_path, config_path, model_item = model_manager.download_model("tts_models/multilingual/multi-dataset/xtts_v2")
config_path="/Users/dylanmoraes/Library/Application Support/tts/tts_models--multilingual--multi-dataset--xtts_v2/config.json"
print(f"Model path: {model_path}")
print(f"Config path: {config_path}")
print(f"Model item: {model_item}")

if config_path is None or not os.path.exists(config_path):
    print("Error: Config path is None or does not exist.")
    print("Attempting to find config file in the same directory as the model...")
    model_dir = os.path.dirname(model_path)
    possible_config = os.path.join(model_dir, "config.json")
    if os.path.exists(possible_config):
        config_path = possible_config
        print(f"Found config file: {config_path}")
    else:
        print("Could not find config file. Please check your model installation.")
        exit(1)

try:
    syn = Synthesizer(
        tts_checkpoint=model_path,
        tts_config_path=config_path,
    )
except Exception as e:
    print(f"Error initializing Synthesizer: {str(e)}")
    exit(1)

def generate_tts_with_timestamps(text, output_file, stretch_factor=1.0,speaker_wav="my/cloning/audio.wav", language="en"):
    try:
        # Generate TTS audio
        # wav = tts.tts(text=text, speaker_wav="my/cloning/audio.wav", language="en")

        wav = tts.tts_to_file(text=text, speaker_wav="my/cloning/audio.wav", language="en", file_path="output.wav")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print(wav, type(wav))

        # Load the audio file
        y, sr = librosa.load(output_file)

        # Stretch the audio
        y_stretched = librosa.effects.time_stretch(y=y, rate=1/stretch_factor)

        # Save the stretched audio
        librosa.output.write_wav(output_file, y_stretched, sr)

        # Generate word-level timestamps
        words = text.split()
        duration = librosa.get_duration(y=y_stretched, sr=sr)
        timestamps = np.linspace(0, duration, len(words) + 1)

        # Create a dictionary of word timestamps
        word_timestamps = {words[i]: {"start": timestamps[i], "end": timestamps[i+1]} for i in range(len(words))}

        # Save timestamps to a JSON file
        with open(f"{output_file[:-4]}_timestamps.json", "w") as f:
            json.dump(word_timestamps, f, indent=2)

        return word_timestamps
    except Exception as e:
        print(f"Error in generate_tts_with_timestamps: {str(e)}")
        return None

# Example usage
text = """The Isle Tide Hotel is not a hotel. At least, not in the conventional sense. It is a gorgeous building that, every three years, plays host to the Verse - a collective of odd individuals with grand personalities and strange mannerisms. You play as Josh, an estranged father whose daughter has been taken by the Verse, and must infiltrate the organisation to save her. Making this more complicated is the fact that the Verse is a verifiable cult with odd ‘etiquettes’ to follow and secrets that are so juicy they wouldn’t feel out of place in a hot-topic Netflix drama."""
output_file = "audio-stretched.wav"
stretch_factor = 1.2  # Slow down the audio by 20%

timestamps = generate_tts_with_timestamps(text, output_file, stretch_factor, speaker_wav="my/cloning/audio.wav", language="en")
if timestamps:
    print("Generated audio with timestamps:", timestamps)
else:
    print("Failed to generate audio with timestamps.")