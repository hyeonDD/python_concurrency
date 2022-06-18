# 코루틴 파이썬 공식문서
# https://docs.python.org/ko/3/library/asyncio-task.html
import asyncio

async def hello_world():
    print("Hello world")

if __name__ == "__main__":
    asyncio.run(hello_world())