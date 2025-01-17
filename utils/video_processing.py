# utils/video_processing.py
from moviepy.editor import VideoFileClip

def extract_audio_from_video(video_path):
    video = VideoFileClip(video_path)
    audio_path = 'audio.wav'
    video.audio.write_audiofile(audio_path)
    return audio_path
