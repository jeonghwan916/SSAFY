T = int(input())

for test_ase in range(1, T + 1):
    bunuck = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    bt = [0]*10
    N = list(input().split())

    arr = list(input().split())

    for i in range(10):
        for j in arr:
            if bunuck[i] == j:
                bt[i] += 1
    print(f'{N[0]}')
    for i in range(10):
        if bt[i] >= 1:
            for j in range(bt[i]):
                print(bunuck[i], end=' ')
    print()


