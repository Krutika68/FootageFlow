# utils/search.py
def search_moments_in_transcription(transcription, keyword):
    moments = []
    lines = transcription.split('\n')
    for line in lines:
        if keyword.lower() in line.lower():
            moments.append(line)
    return moments
