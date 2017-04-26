# -*- coding: utf-8 -*-
import ftplib

def main():
    # 接続先サーバーのホスト名 or IP adress
    ftp = ftplib.FTP("xxx.xxx.xxx")
    ftp.set_pasv("true")
    # ユーザIDとパスワードを指定しログイン
    ftp.login("user", "password")
    # アップロードするファイル
    fp = open("test.csv")
    # アップロード先のディレクトリ
    ftp.storbinary("STOR /files/test.csv",fp)
    # 終了処理
    ftp.close()
    fp.close()

if __name__=='__main__':
    main()
