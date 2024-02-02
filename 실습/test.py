cardlist = list(input())
bk = [0]*5

for i in range(len(cardlist)):
    bk[ord(cardlist[i])-ord('A')] += 1

Sum=0
for i in range(5):
    if bk[i] > 0:
        Sum +=1

print(f'{Sum}개')


