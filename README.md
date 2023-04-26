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
$ python -m pip install python-dotenv yt-dlp openai
```
## API Keyの取得
whisperのAPI Keyを取得してください。  
https://whisperapi.com/

openaiのAPI Keyを取得してください。  
https://platform.openai.com/account/api-keys

## API Keyを環境変数に設定
.envを作成して、各環境変数に取得したAPI Keyを設定してください。
```
$ cp .env.example .env
```

## Youtubeの動画URLを記載
文字起こししたい動画URLを`youtube.list`に記載してください。  
改行で複数指定もできます。
### 注意
- 30分以上の動画はwhisperの無料枠を超えてしまうので、課金してください。
- 要約の出力を行うためにopenapiを利用していますが、入力可能な文字数制限があるため、文字起こしの結果が大きい場合はsummary.txtは出力されません。

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
  └── ucn4jAPWBdQ                                   # 動画のID
      ├── .Must Know Javascript Interview Questions # 動画のタイトル
      ├── audio.mp3                                 # 音声
      ├── audio_text.txt                            # 音声から変換されたテキスト
      ├── meta.json                                 # 動画のメタ情報
      └── summary.txt                               # 内容の概要
```
