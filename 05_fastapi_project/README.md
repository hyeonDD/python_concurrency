# 프로젝트 콜레렉터스 북북이

- ASGI란?
    - ASGI는 애플리케이션 프로그램(FastAPI)의 실행결과를 웹 서버에 전달해주며, 웹 서버는 ASGI로부터 전달받은 응답 결과를 웹 클라이언트(브라우저)에게 전송한다.
    - [ASGI_docs](https://asgi.readthedocs.io/en/latest/introduction.html)
    - 서버 게이트웨이 : 서버로 들어가는 입구 역할
    - WSGI는 동기적인 프로그램만 가능, ASGI는 비동기적인 프로그램도 가능

- Uvicorn란?
    - uvicorn : ASGI 웹 애플리케이션을 실행하는 서버
    - starlette : 웹 애플리케이션 프레임워크

- Fast API란?
    - [FASTAPI_docs](https://fastapi.tiangolo.com/ko/)
    - 파이썬의 웹프레임워크

- "WSGI를 업그레이드하지 않는 이유는 무엇입니까?"라고 물을 수 있습니다. 이것은 수년 동안 여러 번 요청되었으며 일반적으로 문제는 WSGI의 단일 호출 가능 인터페이스가 WebSocket과 같은 복잡한 웹 프로토콜에 적합하지 않다는 것입니다.

WSGI 애플리케이션은 요청을 받고 응답을 반환하는 단일 동기 호출 가능입니다. 이것은 긴 폴링 HTTP 또는 WebSocket 연결과 같이 오래 지속되는 연결을 허용하지 않습니다.

이 호출 가능을 비동기식으로 만들더라도 요청을 제공하기 위한 단일 경로만 있으므로(WebSocket 프레임 수신과 같은) 여러 수신 이벤트가 있는 프로토콜은 이를 트리거할 수 없습니다.의 단점을 보완

# Fast api 사용 패키지

- pip3 install fastapi
- pip3 install uvicorn

- fastapi 서버 on 명령어 
```
uvicorn main:app --reload
```

# jinja 템플릿 사용하기

- pip3 install jinja2
- pip3 install aiofiles