T = int(input())

def sumsum(ii, jj, N):
    Sum = 0
    for i in range(4):
        ny = ii+directy[i]
        nx = jj+directx[i]
        if ny < 0 or ny >= N or nx < 0 or nx >= N:
            Sum = 0
            return Sum
        Sum += arr[ny][nx]
    return Sum - arr[ii][jj]

for tst in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    directy=[-1,1,0,0]
    directx=[0,0,-1,1]

    bestest = 0
    best = 0

    for i in range(N):
        for j in range(N):
            bestest = sumsum(i,j, N)
            if bestest > best:
                best = bestest

    print(f'#{tst} {best}')
