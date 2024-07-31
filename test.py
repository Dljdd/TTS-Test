from TTS.utils.manage import ModelManager
from TTS.utils.synthesizer import Synthesizer
import random

path = "/Users/dylanmoraes/Documents/GitHub/TTS-Test/venv/lib/python3.11/site-packages/TTS/.models.json"

model_manager = ModelManager(path)

model_path, config_path, model_item = model_manager.download_model("tts_models/multilingual/multi-dataset/your_tts")

print("Model item:", model_item)

syn = Synthesizer(
    tts_checkpoint=model_path,
    tts_config_path=config_path,
)

text = "Makes sense, beginning with algorithms should be fine I guess. I also bought Nielsen and Chuang's Book for QC. And I'll probably begin preparing for Qiskit Developer exam"

# Get the number of speakers in the model
num_speakers = syn.tts_model.num_speakers

# Choose a random speaker index
speaker_idx = random.randint(0, num_speakers - 1)

print(f"Using speaker index: {speaker_idx}")

# Generate speech using the random speaker index
outputs = syn.tts(text, speaker_idx=speaker_idx)

# Save the generated audio
syn.save_wav(outputs, "audio-2.wav")