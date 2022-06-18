# https://2.python-requests.org/en/master/user/advanced/#id1
# requests 는 동기적으로 작성되어있지만, 어쩔수없이 aiohttp를 사용하지 못하는 상황에서도 멀티쓰레딩 혹은 멀티 프로세싱을 통해 동시성 혹은 병렬적으로 프로그래밍할 수 있어야한다.

import requests
import time

def fetcher(session, url):
    with session.get(url) as respone:
        return respone.text

def main():
    urls = ["https://naver.com","https://google.com","https://instagram.com"] *10

    with requests.Session() as session:
        # session.get(url)
        result = [fetcher(session,url) for url in urls]
        print(result)

if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(end-start)