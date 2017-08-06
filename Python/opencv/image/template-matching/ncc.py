#-*- coding:utf-8 -*-
import cv2
import numpy as np

def template_matching_ncc(img, temp):
    # 画像の高さ・幅を取得
    h, w = img.shape
    ht, wt = temp.shape
    
    # スコア格納用の2次元リスト
    score = np.empty((h-ht,w-wt))
    
    # 走査
    for dy in range(0, h - ht):
        for dx in range(0, w - wt):
            img2 = img[dy:dy + ht, dx:dx + wt].reshape(-1)
            temp2 = temp.reshape(-1).astype(np.double)
            num = np.dot(img2, temp2.T).astype(np.double)
            den = np.sqrt(np.sum(img2 ** 2)) / np.sqrt(np.sum(temp2 ** 2))
            if den == 0: score[dy, dx] = 0
            score[dy, dx] = num / den
              
    # スコアが最大の走査位置を返す
    score /= np.max(score)
    return np.unravel_index(score.argmax(), score.shape)


def main():
    # 入力画像とテンプレート画像をグレースケールで取得
    img = cv2.imread("input.png")
    temp = cv2.imread("temp.png")

    # グレースケール変換
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)   
    temp = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)   

    # テンプレートマッチング（評価値SAD）
    point = template_matching_ncc(gray, temp)
    
    # テンプレートマッチングの結果を出力
    cv2.rectangle(img, (point[1], point[0] ), (point[1] + temp.shape[0], point[0] + temp.shape[1]), (0,0,200), 3)
    cv2.imwrite("result.jpg", img2)

    
if __name__ == "__main__":
    main()

