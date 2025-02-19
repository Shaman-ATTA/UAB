import requests
import os
from config import UNSPLASH_ACCESS_KEY, FREESOUND_ACCESS_KEY

def download_photo(project_path, project_name):
    response = requests.get(f"https://api.unsplash.com/photos/random?client_id={UNSPLASH_ACCESS_KEY}")
    if response.status_code == 200:
        photo_url = response.json()['urls']['regular']
        photo_response = requests.get(photo_url)
        with open(os.path.join(project_path, project_name, 'Assets', 'photo.jpg'), 'wb') as file:
            file.write(photo_response.content)

def download_audio(project_path, project_name):
    response = requests.get(f"https://freesound.org/apiv2/sounds/158847/download/?token={FREESOUND_ACCESS_KEY}")
    if response.status_code == 200:
        audio_url = response.json()['previews']['preview-lq-mp3']
        audio_response = requests.get(audio_url)
        with open(os.path.join(project_path, project_name, 'Assets', 'audio.mp3'), 'wb') as file:
            file.write(audio_response.content)