def io_bound_func(number:int):
    print("값을 입력해주세요")
    input_value = input()
    return int(input_value)+100

if __name__ == '__main__':
    result = io_bound_func(100)
    print(result )
