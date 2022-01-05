from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse

import asyncio
import aioconsole
import nfc
from nfc_run import read_nfc_tag_async

app = FastAPI()


# input関数を非同期処理化した関数
async def aio_input():
    loop = asyncio.get_running_loop()
    d = await loop.run_in_executor(None,input)
    loop.close()
    return d

@app.get("/")
def index_redirect():
    return RedirectResponse("/index.html")


# 上記の独自関数をから受け取った文字列を返すAPI
@app.get("/input")
async def input_original():
    try:
        res_str= await asyncio.wait_for(aio_input(), timeout=10)
        return res_str
    except asyncio.TimeoutError:
        return {"result":"待ち受け時間を超過しました。"}


@app.get("/nfc")
async def nfc():
    try:
        res= await asyncio.wait_for(read_nfc_tag_async(), timeout=5)
        return {"result":str(res)}
        
    except asyncio.TimeoutError:
        return {"result":"待ち受け時間を超過しました。"}
        


app.mount("/", StaticFiles(directory="static"), name="static")

if __name__ == "__main__":
    app.run()