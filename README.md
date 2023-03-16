# 概要
Youtubeの動画から文字起こしできます

# 使い方

## Install
M1 Macだとpython-dotenvでエラーが出るかも。
自分はanaconda経由でインストールできました。
```
$ pip install python-dotenv 
$ pip install yt-dlp
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

## ツールを実行
実行すると`output`ディレクトリに結果が出力されます。
```python
$ python main.py
```