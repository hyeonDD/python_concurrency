# pip3 install reqeusts
import requests

def io_bound_network_func():
    result = requests.get("https://google.com")
    return result

if __name__ == '__main__':
    result = io_bound_network_func()
    # 여러번 요청하면 오래걸림 (io bound network)
    """
    for i in ragne(10):
        result = io_bound_network_func()
    """
    print(result)
