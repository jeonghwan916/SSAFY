arr = [0]*6
a, b = map(int,input().split())
c=0
for i in range (a, b+1):
    arr[c]=i
    c+=1

for i in range (0, b-a+1):
    print(arr[i],end='')