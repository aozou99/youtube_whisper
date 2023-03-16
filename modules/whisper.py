import requests
import os
import modules.format as fmt
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


def call(mp3_filepath, id, title):
    response = requests.post(
        url,
        headers=headers,
        files={'file': open(mp3_filepath, 'rb')},
        data=data
    )

    jsonData = response.json()
    f = open(f'./output/{id}/audio_text.txt', 'w')
    f.write(fmt.format(jsonData["text"]))
    f.close()

    print(f"created {title}")
