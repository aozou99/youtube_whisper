# 概要
Youtubeの動画から文字起こしできます。
# 使い方

## 環境
```
Apple M1
Python 3.9.7
```
## Install
```
$ python -m pip install python-dotenv yt-dlp
```
## API Keyの取得
whisperのAPI Keyを取得してください。  
https://whisperapi.com/

## API Keyを環境変数に設定
.envを作成して、WHISPER_API_KEYに設定してください。
```
$ cp .env.example .env
```

## Youtubeの動画URLを記載
文字起こししたい動画URLを`youtube.list`に記載してください。  
改行で複数指定もできます。
### 注意
30分以上の動画は無料枠を超えてしまうので、課金してください。

### gitの変更対象外に設定
```
git update-index --assume-unchanged youtube.list
```

## ツールを実行
実行すると`output`ディレクトリに結果が出力されます。
```python
$ python main.py
$ tree -a output
  output
  └── ucn4jAPWBdQ
      ├── .Must Know Javascript Interview Questions
      ├── audio.mp3
      ├── audio_text.txt
      └── meta.json
```
