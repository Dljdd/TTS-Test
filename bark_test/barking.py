from bark import SAMPLE_RATE, generate_audio, preload_models
from scipy.io.wavfile import write as write_wav
from IPython.display import Audio

# download and load all models
preload_models()

# generate audio from text
text_prompt = text = """The Isle Tide Hotel is not a hotel. At least, not in the conventional sense. [mysterious voice]
It is a gorgeous building that, every three years, plays host to the Verse [pause for effect]- a collective of odd individuals with grand personalities and strange mannerisms. 
You play as Josh, an estranged father whose daughter has been taken by the Verse, and must infiltrate the organisation to save her. 
Making this more complicated is the fact that the Verse is a verifiable cult with odd etiquettes to follow and secrets that are so juicy they wouldn’t feel out of place in a hot-topic Netflix drama."""

audio_array = generate_audio(text_prompt)

# save audio to disk
write_wav("bark_generation.wav", SAMPLE_RATE, audio_array)
  
# play text in notebook
Audio(audio_array, rate=SAMPLE_RATE)