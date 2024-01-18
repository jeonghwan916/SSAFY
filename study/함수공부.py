# 사용자정의 함수

print(' ()   ()  ')
print('(        )')
print('(  0  0  )')
print('(    *   )')
print('(  \__/  )')
print('  ()  () ')
print()

def rabit():
    print(' ()   ()  ')
    print('(        )')
    print('(  0  0  )')
    print('(    *   )')
    print('(  \__/  )')
    print('  ()  () ')
    print()


rabit()

#-------------------------------------------------
#
#1. 두 수의 합을 출력하는 함수 (argument(인자값) / parameter(매개변수))

def getsum(a,b):
    print(a+b)
    print('#')

getsum(3,7)

#-------------------------------------------------
#
#2. 두 수의 합을 반환하는 함수

# return

def getsum(a,b):
    return a+b

result=getsum(3,7)
print(result)

#-------------------------------------------------
##3. 두수의 합과 곱을 반환하는 함수

# '#' 출력 안됨
def getsum(a,b):
    return a+b
#        return a*b
    print('#')

result=getsum(3,7)
print(result)

#-------------------------------------------------

# 2개 반환하고 싶다면? (튜플활용)
def getsum(a,b):
    return a+b,a*b

result=getsum(3,7)
print(result)
print(type(result))

#-------------------------------------------------

# return 값이 없을 시? (none 반환 함수종료)
def getsum(a,b):
    return

result=getsum(3,7)
print(result)

#-------------------------------------------------

# argument가 여러개 일때 argument랑 parameter랑 개수 맟춰줬음

def getsum(a,b,c):
    return a+b+c

result=getsum(1,2,3)
print(result)

#-------------------------------------------------
#
# 물론 argement랑 parameter랑 개수가 다르게 구현 가능

#[예시1] defalt parameter (맨 뒤에 써야함)

def getsum(a,b,c=3):
    return a+b+c

result=getsum(1,2)
print(result)

#-------------------------------------------------
#
#[예시2] umpacking을 이용한 경우

#그전에 packing unpacking 에 대해서 보자

# 패킹 (값을 묶어서 변수에 할당)
num=[1,2,3,4,5]
num2=(1,2,3,4,5)
print(num,num2)

# 언패킹 (값들을 여러개 변수로 나눔)

a,b,c,d,e=num
print(a,b,c,d,e)

a,b,c,d,e=num2
print(a,b,c,d,e)

# 언패킹시 남는값을 * 사용하여 리스트에 담을수 있다
num=[1,2,3,4,5]
num2=(1,2,3,4,5)

a,b,*c=num
print(a,b,c)

a,b,*c=num2
print(a,b,c)
print(*c)

a,*b,c=num
print(a,b,c)

#-------------------------------------------------
#
#[예시2] umpacking을 이용한 인자값 전달의 경우 (튜플)

# argument랑 parameter랑 개수가 같아야 하는데
# 가변인자 사용한다면 parameter를 간단하게 사용가능
# *a에 튜플의 형태로 저장

def getsum(*a):
    print(type(a))
    return a[0]+a[1]+a[2]
result=getsum(1,2,3)
print(result)

#-------------------------------------------------
#
#[예시3]

# 그냥 가변인자 말고도 키워드 가변인자 라는 것도 있는데
# 인자값이 key value의 형태일때 즉,

# 딕셔너리 형태로 parameter에 저장함
# 이때는 별2개


def print_info(**args):
    print(args)

    # for i,j in args.items():
    #     print(i,j)

print_info(kevin=1,john=2,bob=3)

#------------------------------------------------- 
#
# 그런데 굳이? 아래와 같이 많이 사용함
# 딕셔너리 선언하고 그냥 매개변수로 받으면 됨

di={'kevin':1,'john':2,'bob':3}

def print_info2(args):
    for i,j in args.items():
        print(i,j)

print_info2(di)


#-------------------------------------------------
#
# 변수 scope (범위)
# 지역변수

# 변수를 함수 안에 선언해 보겠습니다.

def abc():
    aa=3
    bb=5
    print(aa,bb)

abc()
#print(aa,bb) 버그

#-------------------------------------------------
#
# 변수를 함수 밖에 선언 / 그리고 함수 안에도 선언

aa=6
def abc():
    aa=3
    bb=5
    print(aa,bb)

abc()
#print(aa) 6출력


#-------------------------------------------------
#
#전역변수

aa=3
bb=5
def test():
    global aa,bb
    print(aa,bb)
    aa+=1
    bb+=1
    print(aa,bb)

test()
print(aa,bb)

#-------------------------------------------------

# 변수를 함수 안에서 선언하는 경우

def test():
    global aa,bb
    aa = 3
    bb = 5
    print(aa,bb)

test()
aa += 1
bb += 1
print(aa,bb)

#-------------------------------------------------

# 아래 코드는 버그
# kfc 함수안에 global 선언 안해줘서 버그남

# def kfc():
#     print(aa, bb)
#     aa += 1
#     bb += 1
#     print(aa, bb)

def test():
    global aa,bb
    aa = 3
    bb = 5
    print(aa,bb)

test()
# kfc()


#-------------------------------------------------
#-------------------------------------------------

#기타 자주쓰는 내장함수 map, zip, filter, lambda

# map
# 리스트나 튜플같은 순회가능한 데이터구조의 값들에 함수를 적용하고
# 적용후의 값을 map 이라는 객체로 반환 
# map(함수,iterebles)


# 문자의 숫자를 정수로 바꾼후 리스트에 담기

num=['1','2','3'] 
lst1=[]
for i in num:
    lst1.append(int(i))
print(lst1)

# map 함수 이용시
lst2=map(int,num)
print(lst2)
print(list(lst2))


# 여러개의 변수에 정수값 입력받기
# a,b,c=map(int,input().split())
# print(a,b,c)

# 리스트에 여러개의 정수값 입력받기
# lst = list(map(int, input().split()))
# print(lst)

# 리스트에 여러개의 문자를 리스트에 입력받기
lst=list(input().split())
print(lst)

#-------------------------------------------------

# zip

# zip()은 순회 가능한 객체를 인자로 받고 
# 각각의 요소를 잘라서 튜플을 원소로 하는 객체로 반환!!
# 예시>

a='12345'
b='qwert'

ret=zip(a,b)
print(ret)
print(list(ret))


a='12345'
b='qwert'
c='asdfg'

for i in zip(a,b,c):  # 튜플로 반환
    print(i)

for i in zip(a,b,c):   # 리스트로 출력
    print(list(i))

for y,x,z in zip(a,b,c):    # 값만 출력
    print(y,x,z)

#[주의] 함수로 넘기는 객채의 길이가 같아야 함. 더 길 것은 짤림

#-------------------------------------------------
# [퀴즈]

arr=[[1,2,3],
     [4,5,6],
     [7,8,9]]

# 1. 먼저 1 2 3
#         4 5 6
#         7 8 9   리스트를 가로 방향으로 탐색하며 출력해 보기

# 2. 1 4 7
#    2 5 8
#    7 8 9  세로 리스트를 탐색하며 출력해 보기

#-------------------------------------------------

arr=list(map(list,zip(*arr)))

for i in range(3):
    for j in range(3):
        print(arr[i][j],end=' ')
    print()

#-------------------------------------------------

for i in zip(arr[0],arr[1],arr[2]):
    print(list(i))

for i in zip(*arr):
    print(list(i))

ret=list(map(list,zip(*arr)))

print(ret)

#-------------------------------------------------

# filter
# 리스트나 튜플같은 순회가능한 데이터구조의 값들에 함수를 적용하고
# 적용후의 값이 True 인것만 
# filter 라는 객체로 반환

num=[1,2,3,4,5,6,7,8]

def get_even(value):
    if(value%2==0): return True
    else: return False
    
    # return True if value%2==0 else False

ret=filter(get_even,num)
print(list(ret))


#-------------------------------------------------

# lambda (이름도 리턴도 없는 익명함수)
# 함수를 조금더 간편하게 사용하기 위함

#예를들어 두수의 합을 리턴해주는 함수

def Sum(a,b):
    return a+b

result=Sum(3,5)
print(result)

result=(lambda a,b:a+b)(3,5)
print(result)

result=(lambda a,b:a+b)
print(result(3,5))

#-------------------------------------------------

#[연습문제]
# 두 리스트값을 세로로 더했을때 합을 각각 출력하기
lst1=[1,2,3,4,5]
lst2=[6,7,8,9,10]

#출력: 7 9 11 13 15 입니다.

# ver1
lst3=[0]*5
for i in range(5):
    lst3[i]=lst1[i]+lst2[i]
print(*lst3)

# ver2
result=(lambda x,y:x+y)
lst3=map(result,lst1,lst2)
print(*lst3)

# ver3 
lst3=map(lambda x,y:x+y,lst1,lst2)
print(*lst3)


# [연습문제]
# 0~100 사이의 정수중 짝수만 리스트에 담어서 출력해보기

lst=filter(lambda even:even%2==0,range(100))
print(*lst)


#-------------------------------------------------


# 재귀 (1 ~ 10 10 ~ 1) 출력해보기

for i in range(1,11):
    print(i,end=' ')
for i in range(10,0,-1):
    print(i, end=' ')

print()

def abc(level):
    
    if level==11:
        print()
        return
    print(level,end=' ')
    abc(level+1)
    print(level,end=' ')

abc(1)

print()


#-------------------------------------------------


#in not in 공부 후 정리