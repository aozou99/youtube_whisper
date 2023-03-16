from yt_dlp import YoutubeDL
import json


def download(url):
    # メタデータ取得
    with YoutubeDL() as ydl:
        meta = ydl.extract_info(url, download=False)

    # ダウンロード条件を設定する。音声だけ。
    ydl_video_opts = {
        'outtmpl': 'output/%(id)s/'+'audio.mp3',
        'format': 'bestaudio'
    }

    # ダウンロード
    with YoutubeDL(ydl_video_opts) as ydl:
        ydl.download([url])

    # ダウンロードした動画情報を配置
    filtered_meta = {key: meta[key] for key in [
        "id", "title", "description", "webpage_url", "duration_string"]}
    f = open(f'./output/{meta["id"]}/meta.json', 'w')
    json.dump(filtered_meta, f, ensure_ascii=False, indent=4,
              sort_keys=True, separators=(',', ': '))
    f.close()

    # タイトルだけの空ファイル
    f = open(f'./output/{meta["id"]}/.{meta["title"]}', 'w')
    f.close()

    return meta
