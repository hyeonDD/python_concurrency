# https://www.crummy.com/software/BeautifulSoup/bs4/doc/
# pip install beautifulsoup4

from bs4 import BeautifulSoup
import aiohttp
import asyncio

async def fetch(session, url):
    async with session.get(url) as respone:
        html = await respone.text()
        soup = BeautifulSoup(html,'html.parser')
        cont_thumb = soup.find_all('div','cont_thumb')
        # print(cont_thumb)
        for cont in cont_thumb:
            title = cont.find('p','txt_thumb')
            if title is not None:
                print(title.text)

async def main():
    BASE_URL = "https://bjpublic.tistory.com/category/%EC%A0%84%EC%B2%B4%20%EC%B6%9C%EA%B0%84%20%EB%8F%84%EC%84%9C"
    urls = [f"{BASE_URL}?page={i}" for i in range(1, 10)]
    async with aiohttp.ClientSession() as session:
        await asyncio.gather(*[fetch(session, url) for url in urls])

if __name__ == "__main__":
    asyncio.run(main())