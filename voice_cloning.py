import torch
from TTS.api import TTS

tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2")


text = """The Isle Tide Hotel is not a hotel. At least, not in the conventional sense. It is a gorgeous building that, every three years, plays host to the Verse - a collective of odd individuals with grand personalities and strange mannerisms. You play as Josh, an estranged father whose daughter has been taken by the Verse, and must infiltrate the organisation to save her. Making this more complicated is the fact that the Verse is a verifiable cult with odd ‘etiquettes’ to follow and secrets that are so juicy they wouldn’t feel out of place in a hot-topic Netflix drama."""

wav = tts.tts(text=text, speaker_wav="my/cloning/critical.wav", language="en")

tts.tts_to_file(text=text, speaker_wav="my/cloning/critical.wav", language="en", file_path="output.wav")
