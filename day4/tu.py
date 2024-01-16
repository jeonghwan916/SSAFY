x, y = (10, 20)
print(x)
print(y)
x, y = 1, 2
print(x,y)

my_range = range(5)
print(my_range)

print(list(my_range))

# 키를 통해서 value에 접근 (인덱스 아님!! 순서 존재 X)
my_dict = {}
my_dict2 = {'key': 'value'}
my_dict3 = {'apple': 12, 'list': [1, 2, 3]}
# 키는 불변 자료형 == 변경 불가 but value는 변경 가능하다
print(my_dict3['apple'])  # 12
print(my_dict2['key']) # 'value'
print(my_dict3['list'])

my_dict3['apple'] = 100
print(my_dict3['apple']) # 100

#키는 중복이 안됨 + value값은 마지막에 넣은 값으로 갱신

#set (집합 자료형) 중괄호({})로 표기
my_set_1 = set()
my_set_2 = {1, 2, 3} #순서가 아니다
my_set_3 = {1, 1, 1} 

print(my_set_1)
print(my_set_2)
print(my_set_3)
print()

#합집합
print(my_set_1 | my_set_2) #123

#차집합
print(my_set_2 - my_set_3) #23

#교집합
print(my_set_3 & my_set_2) #1


#None 타입
variable = None
print(variable)

#bool 타입
bool_1 = True
bool_2 = False
print(bool_1)
print(bool_2)
print(3 > 1)
print('3' != 3)
print(3 < 1)

#collection

#여러 개의 항목 또는 요소를 담는 자료 구조

# 컬렉션  변경 가능 || 순서 여부
# str        x            o
# list       o            o
# tuple      x            o
# set        o            x
# dict       o            x


# 형변환
# 암시적 형변환
print(5 + 3.0)
print(True)
print(True + 3)
print(True + False)
print(True + True)
# 명시적 형변환
# str => int : 형식에 맞는 숫자만 가능
# int => str : 모두 가능
print(int('1'))
print(str(1)+'등')
print(float('3.5'))
print(int(3.5))
print(int(4.0))

# print(int('3.5')) 에러
print(int(float('3.5'))) #가능


 # not (결과를 부정)
print(not True)
print(not False)


num = 15
name = '123'

#and에서 앞 조건 틀림 그냥 넘어감
#or에서는 앞 조건 참이면 그냥 넘어감
#단축평가
print("단축평가")
vowels = 'aeiou'
print(('a' and 'b') in vowels) # 'a' and 'b' == true >> b in.. >>false 
print(('b' and 'a') in vowels) # 'b' and 'a' == true >> a in.. >>true 
print()
print(3 and 5)
print(3 and 0)
print(0 and 3)
print(0 and 0)
print()
print(5 or 3)
print(3 or 0)
print(0 or 3)
print(0 or 0)

#맴버십 연산자
#in : 왼쪽 피연산자가 오른쪽 피연산자의 시퀀스에 있는지 
#not in 반대로 없는지

#시퀀스형 연산자 (시퀀스 연산자 스퀀스)
# + 결합 연산자
# * 반복 연산자



a = '"100%"'
print(f'오늘 컨디션은 {a} 입니다')
print('오늘 컨디션은 "100%" 입니다')

a = 3.12523
b = 2.72495

# 매우 작은 수를 더해준다(부동 소숫점 오류 해결)
print(round(a+1e-8,2))
print(round(b+1e-8,2))

import math
print(math.floor(a+0.5))


s='abcdefg'
print(s[:3]) #abc
print(s[3:]) # defg
print(s[2:5]) # cde
print(s[5:2:-1]) #def
print(s[1:6:2]) #bdf
print(s[-2]) #f
print(s[:-1]) #abcdef

print(s+'ABC')

s+="KFC"
print(s)
print(s*2)

lst = [1, 2, 3, 4]
print(lst[1])
lst[1] = 100

s="abcdefg"
print(s[0])
print(s[1])
#s[1] = 'K' 이런거 불가능

ret=s.replace(s[1],'K')
#리플레이스 변수를 사용해서 변경
print(ret)

lst = [1, 2, 3, 4]
print(type(lst))
print(len(lst))
print(lst*3)

print(lst+[9, 8, 7])

lst = [1, 2, 3, 4, [5, 6, 7], 9]
print(lst[4][0])
print(lst[-2][-3])

tp=(1,2,3,4,5)
print(tp)
print(type(tp))
print(tp[1])
print(len(tp))
print(tp[-1])

# tp[1] = 1 튜플 값 변경 불가능


di = {1:3, 2:{4:5}, '학':6, '교':[7,8,9]}
print(di)
print(type(di))
print(di[1])
print(di[2][4])
print(di['교'][2])
#딕셔너리 값 변경
di[2]="여름에는 민어를 먹어야지"
print(di)

#팝 메서드 사용
di['test']=di.pop(1)
print(di)



#set ==> 중복값 제거에 사용

s={1, 2, 3, 4, 5}
print(s)
print(type(s))

lst=[1, 1, 2, 2, 3, 3, 3, 1, 2, 12, 1]
lst=list(set(lst))
print(lst)


s1 = {1, 2, 3}
s2 = {3, 6, 9}

print(s1 | s2)
print(s1 - s2)
print(s1 & s2)  #엠퍼센트 라고 읽음
##############
# 순서의 개념이 있는것 중 인덱스로 접근해서 바꿀수 없는거
# 문자열, 튜플
# 순서의 개념이 없는 자료형 = dic,set

a = True
b = False
c = True
d = False

print(a and b)
print(a and c)
print(a or c)


a, b = 0, -1
a, b = bool(a), bool(b)
print(a,b)

a1 = bool('a')
b1 = bool('0')
c1 = bool('')
print(a1,b1,c1)

print('a'and'b') # b
print(''and'a') # ''
print(0 and 1) # 0

print(1 or 0) # 1
print(0 or -1) # 0
print(-1 or 1) # -1

#연산자 우선순위
result = 10 % 3 + 2 ** 2
result = (10 % 3) + (2 ** 2)
#소괄호 잘 쓰기
print(result)

result = -3**2
print(result)

result = (-3)**2
print(result)

#비교연산자 > < <= >= == != is 
a=2
b=2.0

if a == b:
    print('정답')
else:
    print('오답')

if a is b: #이건 값이 아니라 주소값을 비교함
    print('정답')
else:
    print('오답')