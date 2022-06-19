import requests
import time
import os
import threading

def fetcher(session, url):
    print(f"{os.getpid()} process | {threading.get_ident()} url : {url}")
    with session.get(url) as respone:
        return respone.text

def main():
    urls = ["https://naver.com","https://google.com"] *10

    with requests.Session() as session:
        # session.get(url)
        result = [fetcher(session,url) for url in urls]
        # print(result)

if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(end-start)