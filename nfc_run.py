import nfc
import asyncio

# NFCでデータを読み込むための関数
def read_nfc_tag(clf):
    data = None
    # アロー関数的な処理
    def connected(tag):
        # スコープの扱いに注意
        nonlocal data
        data = tag
    # 接続したらこの行で止まる
    clf.connect(rdwr ={'on-connect': connected})
    # 読み込んだらconnected関数が実行されて次の行でreturn
    return data

# 上の読み込み処理を非同期処理にした関数
async def read_nfc_tag_async():
    clf=  nfc.ContactlessFrontend('usb')    
    try:
        print("start")
        # イベントループを取得して
        loop = asyncio.get_running_loop()
        # そこに非同期にしたい処理を入れる感じ
        d = await loop.run_in_executor(None, read_nfc_tag,clf)
    finally:
        # 必ず接続を閉じる
        print("close")
        clf.close()
    return d

async def main():
    clf=  nfc.ContactlessFrontend('usb')
    try:
        # 超便利。指定した時間を超えたらエラーになる
        result = await asyncio.wait_for(read_nfc_tag_async(), timeout=5) 
        print(result)
    except asyncio.TimeoutError:
        print("timeout")
    return 0

if  __name__ == "__main__":
    asyncio.run(main())