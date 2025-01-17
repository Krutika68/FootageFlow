# AI Video Storytelling Tool

An AI-powered video-editing and storytelling tool that helps users organize, search, and create meaningful stories from their personal footage. The tool integrates AI for transcription, search functionality, and automatic story creation based on video content and user prompts.

## Features

- **Video Upload**: Users can upload their personal video footage.
- **AI Transcription**: Converts the audio from videos into searchable text.
- **Search Moments**: Users can search for specific moments in the video (e.g., "vacation" or "birthday") based on transcription.
- **Automated Story Creation**: The tool uses AI to generate a story from the uploaded footage based on user prompts.
- **Easy-to-use Interface**: A simple web interface to upload videos, search for moments, and create stories.

## Requirements

- Python 3.x
- Flask (for the web backend)
- OpenAI API key (for GPT-3 and transcription)
- MoviePy (for video processing)
- Streamlit (optional, for frontend)

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/ai-video-storytelling-tool.git
    cd ai-video-storytelling-tool
    ```

2. Create a virtual environment:

    ```bash
    python -m venv venv
    ```

3. Activate the virtual environment:
    - **Windows**:
      ```bash
      venv\Scripts\activate
      ```
    - **Mac/Linux**:
      ```bash
      source venv/bin/activate
      ```

4. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

    The `requirements.txt` should contain the following dependencies:
    ```
    Flask
    moviepy
    openai
    streamlit
    ```

## Configuration

1. **OpenAI API Key**:  
   You need to set up an OpenAI account and get an API key for transcription and story generation. Add your API key in the script or set it as an environment variable.
   
   Example:
   ```python
   openai.api_key = 'your-openai-api-key'

2. ## Running the Flask App:
``` bash
python app.py
```

3. ## Using the Streamlit Interface:
```bash
streamlit run streamlit_app.py
```
