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


#사술 연산자






