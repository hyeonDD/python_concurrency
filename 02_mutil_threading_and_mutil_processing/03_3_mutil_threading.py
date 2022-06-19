# https://docs.python.org/3.7/library/concurrent.futures.html#concurrent
# 파이썬에서 멀티쓰레드는 병렬적으로 동작하지 않음.
from concurrent.futures import ThreadPoolExecutor
import requests
import time
import os
import threading

def fetcher(params):
    session = params[0]
    url = params[1]
    print(f"{os.getpid()} process | {threading.get_ident()} url : {url}")
    with session.get(url) as respone:
        return respone.text

def main():
    urls = ["https://naver.com","https://google.com"] *10

    executor = ThreadPoolExecutor(max_workers=10)
    with requests.Session() as session:
        # session.get(url)
        # result = [fetcher(session,url) for url in urls]
        # print(result)
        params = [(session,url) for url in urls]
        list(executor.map(fetcher,params))

if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(end-start)