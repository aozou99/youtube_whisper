import requests
import os
from dotenv import load_dotenv

load_dotenv()

url = "https://transcribe.whisperapi.com"
headers = {
    'Authorization': f'Bearer {os.environ.get("WHISPER_API_KEY")}'
}
data = {
    "fileType": "mp3",
    "diarization": "false",
    "numSpeakers": "2",
    "language": "en",
    "task": "transcribe"
}


def call(mp3_filepath):
    response = requests.post(
        url,
        headers=headers,
        files={'file': open(mp3_filepath, 'rb')},
        data=data
    )

    return response.json()
