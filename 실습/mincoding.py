arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split()))
arr3 = []

while 1:
    if arr1 and arr2:
        if arr1[0] >= arr2[0]:
            arr3.append(arr2[0])
            arr2.pop(0)

        elif arr2[0] >= arr1[0]:
            arr3.append(arr1[0])
            arr1.pop(0)

    elif arr1 and not arr2:
        arr3.extend(arr1)
        arr1.clear()

    elif arr2 and not arr1:
        arr3.extend(arr2)
        arr2.clear()
    elif not arr1 and not arr2:
        break

print(*arr3)