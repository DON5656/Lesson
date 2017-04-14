#!/usr/bin/env python
# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time

def main():
    # 使用する出力ピン(GPIO)
    pin_num = 14
        
    　# GPIOピンの定義
　　　　GPIO.setmode(GPIO.BCM)          # GPIO番号で指定
　　　　GPIO.setup(pin_num, GPIO.OUT)   # 出力モード
    
     # 点滅を5セット繰り返し
　　　　for x in range(10):
　　　　　　　　GPIO.output(pin_num, GPIO.HIGH) # 点灯
　　　　　　　　time.sleep(2)                   # 2秒待機
　　　　　　　　GPIO.output(pin_num, GPIO.LOW)  # 消灯
　　　　　　　　time.sleep(2)                   # 2秒待機
        
    # GPIOピンの設定解除        
　　　　GPIO.cleanup()                      

if __name__ == "__main__":
    main()
