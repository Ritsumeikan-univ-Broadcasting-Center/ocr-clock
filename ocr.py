from PIL import Image
import pyocr

# OCRエンジンを取得
engines = pyocr.get_available_tools()
engine = engines[0]

# 画像を読み込む
img = Image.open('test.png')

# 画像の文字を読み込む
txt = engine.image_to_string(img, lang="eng")
print(txt) # 「Test Message」が出力される
