import cv2
import time
from ocr import ocr, cv2pil

# 画像の2値化
def binarization(img, threshold):
    # 二値化(閾値100を超えた画素を255にする。)
    ret, img_thresh = cv2.threshold(img, threshold, 255, cv2.THRESH_BINARY)
    return ret, img_thresh

if __name__ == "__main__":
    # VideoCaptureのインスタンスを作成する。
    # 引数でカメラを選べれる。
    cap = cv2.VideoCapture(0)
    var = 100 # 2値化の閾値
    while(60):
        ret, frame = cap.read()
        cv2.imshow(frame)
        frame_2 = binarization(frame, var)
        frame_3 = cv2pil(frame_2)
        txt = ocr(frame_3)
        print(txt)
        time.sleep(0.5)
    # キャプチャをリリースして、ウィンドウをすべて閉じる
    cap.release()
    cv2.destroyAllWindows()