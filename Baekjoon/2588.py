# 2588
# 곱셈

imort sys

def std_input():
    return sys.stdin.readline().strip()


if __name__ == "__main__":
    # input
    num = int(std_input())
    num_list = list(map(int, std_input()))
    
    # output
    result = [0, 0, 0, 0]
    for index, _ in enumerate(num_list):
        result[2-index] = num * _
        result[3] += result[2-index] * pow(10, 2 - index)
        
    # print
    for _ in result:
        print(_)
