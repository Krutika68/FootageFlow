# utils/transcription.py
import openai
from utils.video_processing import extract_audio_from_video

# Set up OpenAI API key
openai.api_key = 'your-openai-api-key'

def transcribe_audio(audio_path):
    audio_file = open(audio_path, 'rb')
    response = openai.Audio.transcribe(
        model="whisper-1", 
        file=audio_file,
        language="en"
    )
    return response['text']

def transcribe_video(video_path):
    audio_path = extract_audio_from_video(video_path)
    transcription = transcribe_audio(audio_path)
    return transcription
