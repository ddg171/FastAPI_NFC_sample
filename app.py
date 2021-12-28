from fastapi import FastAPI
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

# 非同期の標準入力関数から受け取った文字列を返すAPI
@app.get("/")
async def input_async():
    try:
        res_str= await asyncio.wait_for(aioconsole.ainput("input"), timeout=10)
        return res_str
    except asyncio.TimeoutError:
        return "ososugi"

# 上記の独自関数をから受け取った文字列を返すAPI
@app.get("/input")
async def input_original():
    try:
        res_str= await asyncio.wait_for(aio_input(), timeout=10)
        return res_str
    except asyncio.TimeoutError:
        return "ososugi"

@app.get("/nfc")
async def nfc():
    global clf
    try:
        res= await asyncio.wait_for(read_nfc_tag_async(), timeout=10)
        return str(res)
    except asyncio.TimeoutError:
        return "ososugi"


if __name__ == "__main__":
    app.run()