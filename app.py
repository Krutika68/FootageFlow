# app.py
from flask import Flask, request, jsonify, render_template
import os
from utils.transcription import transcribe_video
from utils.search import search_moments_in_transcription
from utils.story_creation import create_story_from_video

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'})
    if file:
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)
        transcription = transcribe_video(filepath)
        return jsonify({'message': 'File successfully uploaded', 'filepath': filepath, 'transcription': transcription})

@app.route('/search', methods=['POST'])
def search():
    data = request.json
    transcription = data['transcription']
    keyword = data['keyword']
    moments = search_moments_in_transcription(transcription, keyword)
    return jsonify({'moments': moments})

@app.route('/create-story', methods=['POST'])
def create_story():
    data = request.json
    video_path = data['video_path']
    prompt = data['prompt']
    story = create_story_from_video(video_path, prompt)
    return jsonify({'story': story})

if __name__ == '__main__':
    app.run(debug=True)
