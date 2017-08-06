#-*- coding:utf-8 -*-
import cv2
import numpy as np

def template_matching_ncc(src, temp):
    # 画像の高さ・幅を取得
    h, w = src.shape
    ht, wt = temp.shape
    
    # スコア格納用の2次元リスト
    score = np.empty((h-ht, w-wt))
    
    # 走査
    for dy in range(0, h - ht):
        for dx in range(0, w - wt):
            num = np.sum(src[dy:dy + ht, dx:dx + wt] * temp)
            den = np.sqrt(np.sum(src) ** 2) / np.sqrt(np.sum(temp) ** 2)
            if den == 0: score[dy, dx] = 0
            score[dy, dx] = num / den
        
    # スコアが最小の走査位置を返す
    return np.unravel_index(score.argmin(), score.shape)


def main():
    # 入力画像とテンプレート画像をグレースケールで取得
    img = cv2.imread("input.png")
    temp = cv2.imread("temp.png")

    # グレースケール変換
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)   
    temp = cv2.cvtColor(temp, cv2.COLOR_RGB2GRAY)   

    # テンプレートマッチング（評価値NCC）
    point = template_matching_ncc(gray, temp)
    
    # テンプレートマッチングの結果を出力
    cv2.rectangle(img, (point[1], point[0] ), (point[1] + temp.shape[0], point[0] + temp.shape[1]), (0,0,200), 3)
    cv2.imwrite("result.png", img)

    
if __name__ == "__main__":
    main()
