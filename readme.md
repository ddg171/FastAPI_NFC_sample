# About

-   FastAPI を利用して標準入力や NFC からのデータを受け付けるアプリのサンプル
-   pipenv を使っています
-   Debian(Chromebook/Crostini)でのみ動作を確認しています。
-   特にコピペ・流用に制限は設けません。
-   コピペ・流用によって生じたあらゆる損害、問題については自己責任でお願いします。

# 起動方法

"pipenv shell"
"uvicorn app:app"

# API について

## NFC 読み込み API(/nfc)

1. curl で localhost:{起動時のポート番号}/nfc に GET リクエストを投げると NFC リーダーが待機状態になります。
2. 10 秒以内に読込処理が発生すると読み込んだ ID 等を文字列で返します。
3. 10 秒読込処理が発生しなければタイムアウトします。

## 標準入力読み込み API( /input)

基本は NFC 読み込み API と同じです。

# 実使用時の注意

-   読み込み待機中に別の読み込みリクエストを投げてもエラーが返ります。先に読込状態になったリクエストが優先されます。
