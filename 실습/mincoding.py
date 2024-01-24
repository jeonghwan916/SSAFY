arr = list(map(int,input().split()))
for _ in range(15):
    for i in range(len(arr)-1):
        if arr[i]<arr[i+1]:
            x= arr[i]
            arr[i] = arr[i+1]
            arr[i+1]=x
    
print(arr)
