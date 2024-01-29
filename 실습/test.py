arr=[[0]*3 for _ in range(2)]
arr2 = list(map(int,input().split()))
x=0

for i in range(2):
    for j in range(3):
        arr[i][j] = arr2[x]
        x+=1

print(arr)

