import modules.whisper as whisper
import modules.ydl as ydl

with open('youtube.list', 'r') as f:
    urls = f.read().split("\n")

for url in urls:
    if not url.startswith('http'):
        continue
    meta = ydl.download(url)
    whisper.call(
        f"./output/{meta['id']}/audio.mp3", meta['id'], meta['title'])

print('success!')
