name = list(input().split())  # A B C D E
arr = [
    [0, 1, 0, 0, 0],
    [0, 0, 1, 1, 0],
    [1, 0, 0, 0, 1],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0]]

used = [0] * 5
Min = 21e8


def dfs(now, level):
    global Min
    if now == 3:
        if level < Min:
            Min = level

    for i in range(5):
        if arr[now][i] == 1 and used[i] == 0:
            used[i] = 1
            dfs(i, level + 1)
            used[i] = 0


used[0] = 1
dfs(0, 0)  # now level
print(Min)
