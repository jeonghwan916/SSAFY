# def sum(a, b, c=10): # 매개변수 파라미타   
#     return a + b + c

# print(sum(1, 5)) # 인자값 아규먼트
# ret=sum(1, 5)
# print(type(ret))


# #언패킹시 변수 개수 숫자 맞추지 않아도 되는경우
# num = [1, 2, 3, 4, 5]
# num2 = (1, 2, 3, 4, 5)

# a,b,*c=num
# print(a, b, c)
# a,b,c,*d=num2
# print(a, b, c, d)



# def ad(*a):
#     print(type(a))
#     print(a)

# ad(1, 2, 3)

# def add(**a):
#     print(type(a))
#     print(a)
#     for i, j in a.items():  # 딕셔너리의 키와 밸류를 참조한다
#         print(i, j)

# add(a=1, b=2)

# aa = 5
# bb = 3

# def test():
#      global aa
#      global bb
#      aa+=3
#      bb+=5
#      print(aa,bb)

# test()
# print(aa,bb)


#map 리스트나 튜플같이 순회 가능한 데이터 구조의 값들에 함수를 일괄적으로 적용하고 적용한 후 map이라는 객체로 반화
#zip은 순회 가능한 요소를 잘라서 새로운 튜플의 형태로 저장하는 내장 함수
#zip 이라는 객체로 반환

# a='132'
# b='abc'
# ret=zip(a,b)
# print(ret)
# print(list(ret))

# arr=[[1,2,3],
#      [4,5,6],
#      [7,8,9]]

# for i in range(2, -1, -1):
#     for j in range(2, -1, -1):
#         print(arr[i][j])
     


#filter(적용시킬 함수, 적용할 리스트)
# num = [1,2,3,4,5,6,7,8]

# def geteven(value):
#     if value%2==0: return True
#     else: return False

# ret=filter(geteven, num)
# print(list(ret))


# #lamda (익명함수)
# def getsum(a, b):
#     return a + b
# ret = getsum(3, 5)
# print(ret)

# #==
# #이름이 없는 함수를 만드는데
# #매개변수가 a, b다 그리고 리턴할 값은 a + b다
# #그리고 그 a, b 에 3, 5를 넣는다 (따로 적는것도 가능하다)
# ret = (lambda a, b : a + b)(3, 5)
# print(ret)
# ret = (lambda a, b : a + b)
# print(ret(3, 5))


#[연습문제]

# lst1 = [1, 2, 3, 4, 5]
# lst2 = [6, 7, 8, 9, 10]
# lst3 = [0]*5
# #v1
# for i in range(5):
#     lst3[i] = lst1[i]+lst2[i]
# print(*lst3)

# #v2
# result=(lambda a,b:a+b)
# lst3 = map(result, lst1, lst2)
# print(*lst3)

# #v3
# lst3 = map(lambda a,b:a+b, lst1, lst2)
# print(*lst3)

print(10%3)