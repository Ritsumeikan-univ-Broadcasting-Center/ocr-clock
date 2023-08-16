from PIL import Image
import pyocr

# OCRエンジンを取得
engines = pyocr.get_available_tools()
engine = engines[0]

# 画像の文字を読み込む
def ocr(img):
    txt = engine.image_to_string(img, lang="eng")
    return txt

# cv2の画像からpillowの画像へ
def cv2pil(image):
    ''' OpenCV型 -> PIL型 '''
    new_image = image.copy()
    if new_image.ndim == 2:  # モノクロ
        pass
    elif new_image.shape[2] == 3:  # カラー
        new_image = new_image[:, :, ::-1]
    elif new_image.shape[2] == 4:  # 透過
        new_image = new_image[:, :, [2, 1, 0, 3]]
    new_image = Image.fromarray(new_image)
    return new_image

if __name__ == "__main__":
    # 画像を読み込む
    image = Image.open('test.png')
    text = ocr(image)
    print(text) # 「Test Message」が出力される
