import re

# 文章の区切りに改行入れる。web2.0系は避ける。
def format(text):
  return re.sub('^\s+|\s+$', '', re.sub('\.[^0]', '.\n', text))