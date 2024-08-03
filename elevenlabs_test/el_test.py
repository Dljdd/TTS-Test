from elevenlabs.client import ElevenLabs
from elevenlabs import stream
from pydub import AudioSegment
import io

client = ElevenLabs(
  api_key="", # Defaults to ELEVEN_API_KEY
)

def text_stream():
    yield "Hi there, I'm Eleven "
    yield "I'm a text to speech API "

audio_stream = client.generate(
    text=text_stream(),
    voice="Nicole",
    model="eleven_monolingual_v1",
    stream=True
)



# audio_data = io.BytesIO()

# # Write audio chunks to the BytesIO object
# for audio_chunk in audio_stream:
#     audio_data.write(audio_chunk)

# # Seek back to the start of the BytesIO object
# audio_data.seek(0)

# # Load the audio data into an AudioSegment
# audio_segment = AudioSegment.from_file(audio_data)

# # Export to a WAV file
# audio_segment.export("output.wav", format="wav")

# # Optionally, export to MP3 as well
# audio_segment.export("output.mp3", format="mp3")

# print("Audio saved successfully.")

stream(audio_stream)

