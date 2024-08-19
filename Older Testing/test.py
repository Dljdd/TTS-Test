from TTS.utils.manage import ModelManager
from TTS.utils.synthesizer import Synthesizer

path = "/Users/dylanmoraes/Documents/GitHub/TTS-Test/venv/lib/python3.11/site-packages/TTS/.models.json"

model_manager = ModelManager(path)

model_path, config_path, model_item = model_manager.download_model("tts_models/multilingual/multi-dataset/xtts_v2")

# Print model_item to check its contents
print("Model item:", model_item)

# Check if default_vocoder is in model_item
# if "default_vocoder" in model_item:
#     voc_path, voc_config_path, _ = model_manager.download_model(model_item["default_vocoder"])
# else:
#     print("No default vocoder found. Using a fallback vocoder.")
#     # You may need to replace this with an appropriate vocoder for your TTS model
#     voc_path, voc_config_path, _ = model_manager.download_model("vocoder_models/en/ljspeech/multiband-melgan")

syn = Synthesizer(
    tts_checkpoint=model_path,
    tts_config_path=config_path,
    # vocoder_checkpoint=voc_path,
    # vocoder_config=voc_config_path
)

text = "Makes sense, beginning with algorithms should be fine I guess. I also bought Nielsen and Chuang's Book for QC. And I'll probably begin preparing for Qiskit Developer exam"

outputs = syn.tts(text)
syn.save_wav(outputs, "audio-3.wav")