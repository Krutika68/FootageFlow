# utils/story_creation.py
import openai
from utils.transcription import transcribe_video

openai.api_key = 'your-openai-api-key'

def create_story_from_video(video_path, prompt):
    transcription = transcribe_video(video_path)
    
    # Create a story using GPT model
    story_prompt = f"Create a story from the following transcription about {prompt}: \n\n{transcription}"
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=story_prompt,
        max_tokens=1000
    )
    return response.choices[0].text.strip()
