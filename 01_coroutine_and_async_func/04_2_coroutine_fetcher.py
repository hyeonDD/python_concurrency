# https://docs.aiohttp.org/en/stable/
# pip3 install aiohttp~=3.7.3

# import requests # 리퀘스트는 동기적인 코드를 사용함
# aiohttp는 코루틴을 사용한 비동기적인 패키지 aiohttp는 코루틴(async)로열어줌

import asyncio
import aiohttp
import time

async def fetcher(session, url):
    async with session.get(url) as respone:
        return await respone.text()

async def main():
    urls = ["https://naver.com","https://google.com","https://instagram.com"] *10

    async with aiohttp.ClientSession() as session:
        result = await asyncio.gather(*[fetcher(session, url) for url in urls])
        # result = await fetcher(session, urls[0])
        print(result)

if __name__ == "__main__":
    start = time.time()
    asyncio.run(main())
    end = time.time()
    print(end-start)