arr = list(map(int,input().split()))

for i in range(len(arr)):
    if arr[i] < 5:
        str = '불합격'
    else:
        str = '합격'
    print(f'{i}번은 {arr[i]}점 {str}')

