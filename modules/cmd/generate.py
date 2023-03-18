import modules.lib.whisper as whisper
import modules.lib.ydl as ydl
import modules.lib.openai as openai
import modules.lib.path as path
import modules.lib.format as fmt


def _task(url):
    if not url.startswith('http'):
        return

    meta = ydl.download(url)

    res = whisper.call(
        path.save_path(meta['id'], 'audio.mp3'), meta['id'], meta['title'])

    path.save_file(meta['id'], 'audio_text.txt',
                   fmt.text_readable(res['text']))

    path.save_file(meta['id'], 'summary.txt', fmt.text_readable(
        openai.summarize_text(res['text'])))


def exec():
    with open('youtube.list', 'r') as f:
        urls = f.read().split("\n")

    for url in urls:
        try:
            _task(url)
        except Exception as e:
            print(f'{url} failed.', e)
