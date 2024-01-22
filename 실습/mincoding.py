def input1():
    a, b, c = map(int,input().split())
    return a, b, c

def calc(x):
    print(x[0] + x[1] + x[2])

calc(input1())