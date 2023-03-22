def text_readable(text: str):
    d = {
        '. ': '.\n',
        '? ': '?\n'
    }
    for old, new in d.items():
        text = text.replace(old, new)
    return text
