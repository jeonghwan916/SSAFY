def restructure_word(word, arr):
    w_l = list(word)
    for i in range(len(w_l)):
        if w_l[i].isdecimal():
            for _ in range(w_l[i]):
                arr.pop()
        else:
            arr.remove(w_l[i])
    result = arr
    return result


   
original_word = '코딩 공부는ㄴ 1일ㄹ 1커ㅓ밋ㅅ @@@#^()#_+!&~:"'
word = '1ㄴ2ㄹ3ㅓ4ㅅ5'
arr = []
arr.extend(original_word)
print(arr)

result = restructure_word(word, arr)
