import torch
from TTS.api import TTS

tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2")


text = "Makes sense, beginning with algorithms should be fine I guess. I also bought Nielsen and Chuang's Book for QC. And I'll probably begin preparing for Qiskit Developer exam"

wav = tts.tts(text=text, speaker_wav="my/cloning/audio.wav", language="en")

tts.tts_to_file(text=text, speaker_wav="my/cloning/audio.wav", language="en", file_path="output.wav")
