# 절차 : 공격한다(전사가)
# 객체 : 전자가 베기를 한다 

# 절차
# -데이터와 해당 데이터를 처리하는 함수(절차)가 분리
# -함수의 호출 흐름이 중요
# -소프트웨어 위기
# -하드웨어의 발전으로 컴퓨터의 계산용량과 문제의 복잡성이
# -급격히 증가함에 따라 소프트웨어에 발생한 충격


# 객체
# -데이터와 해당 데이터를 처리하는 메서드(메시지)를 하나의 객체(클래스)로 묶음

# -객체 간 상화작용과 메시지 전달이 중요



# 클래스: 파이써에서 타입을 표현하는 방법
# -객체를 생성하기 위한 설계도
# -데이터와 기능을 함께 묶는 방법을 제공
# -클래스도 객체다

# 객체(object)
# -클래스에서 정의한 것을 토대로 메모리에 할당된 것(클래스에서 정의한 것이 아니더라도 객체)
# -속성과 행동으로 구성된 모든 것
# -클래스로 만든 객체는 인스턴스라고 함(class 필요)

# 클래스(가수)와 객체(아이유)
# 타입(list)                                  
# 클래스를 만든다 == 타입을 만든다

# 문자열 변수는 str클래스의 인스턴스이다
# 따라서 type찍어보면 class 'str' 이라고 나온다
# help함수 사용해보면 그 클래스 정보가 나온다

# 우리가 문자열에 .upper()이런거 사용 가능한 이유는 클래스 안에 저 어퍼가 있다
# 클래스 안에 존재하는 함수 == 메서드
# 사용법 == 인스턴스.메서드()
# ex) [1,2,3].sort()
#     리스트.정렬해()
#     객체.행동()
#     인스턴스.메서드()

# 파이썬에서 객체는 속성과 기능의 개념
# 클래스는 class로 시작하고 이름이 대문자로 시작하고 옆에 괄호가 생략 가능
# 대문자로 시작 == 이건 클래스구나!
# #클래스 정의
# class Person:
#     pass

# #인스턴스 생성
# iu = Person()

# #메서드 호출
# iu.메서드()

# #속성(변수) 접근
# iu.attribute


# # class Person:
# #     blood_color = 'red'

# #     def __init__(self, name):
# #         self.name = name

# #     def singing(self):
# #         return f'{self.name}가 노래합니다.'
    
# # #인스턴스 생성
# # singer1 = Person('iu')

# # #메서드 호출
# # singer2 = Person('bts')
# # print(singer2.singing())
# # print(singer2.blood_color)
# # print(singer1.singing())
# # print(singer1.blood_color)
# # singer1.blood_color = 'blue'
# # print(singer1.blood_color)
# # Person.blood_color = 'yellow'
# # print(Person.blood_color) # yellow
# # print(singer1.blood_color) # blue

# # class Person:
# #     name = 'unKnown'

# #     def talk(self):
# #         print(self.name)

# # p1 = Person()
# # p1.talk()
# # p2 = Person()
# # p2.name = 'kim'
# # p2.talk()
# # print(Person.name)
# # print(p1.name)
# # print(p2.name)

# # p2.ssafy = 21
# # print(p2.ssafy)

# # #서로 독립적으로 동작이 가능하다~~~!
# # 공통된 매직 매서드? 그걸 응용해서 생성 수나 비슷한 작업 가능

# class Circle():
#     pi = 3.14

#     def __init__(self, r):
#         self.r = r

# c1 = Circle(5)
# c2 = Circle(10)

# print(Circle.pi)
# print(c1.pi)
# print(c2.pi)
# Circle.pi = 5
# print(c1.pi)
# print(c2.pi)
# Circle.pi = 3.14
# c2.pi = 7   #c2인스턴스 변수 pi를 만들고 할당했다 == 
# # 앞으로 pi 찾으면 본인 pi 찾지  클래스 pi 찾지 않음
# print(Circle.pi)
# print(c1.pi)
# print(c2.pi)

# 메서드의 종류
# -인스턴스 메서드
#   클래스로부터 생성된 각 인스턴스에서 호출할 수 있는 메서드
#   인스턴스의 상태를 조작하거나 동작을 수행
#   반드시 첫 번재 매개변수로 인스턴스 자신(self)을 전달받음
#       self의 동작 원리
#           우리는 'hello'.upper()
#           파이썬은 str.upper('hello')
#           *인스턴스 메서드의 첫번째 매개변수가 반드시 자기자신인 이유*

#-생성자 메서드 
#   인스턴스 객체가 생성될때 자동으로 호출되는 메서드
#       인스턴스 변수들의 초기값을 설정
#           이것도 자기자신이 첫 인자로 들어옴
#   __init__

# -클래스 메서드
#   클래스가 호출하는 메서드
#       클래스 변수를 조작하거나 클래스 래벨의 동작을 수행
#           @classmethod 데코레이터를 사용해서 정의 (이거 없으면 인스턴스 메서드가 됨)
#               호출 시 , 첫번째 인자로 호출하는 클래스가 전달됨(cls)
class Person:
    cout = 0
    
    def __init__(self, name):
        self.name = name
        Person.cout += 1

    @classmethod
    def number_of_population(cls):
        print(f'인구수는 {cls.cout}입니다')
    # Person.cout 써도 이상은 없지만 자식 클래스가 있다면 자식이 계속 자신이 아니라 부모 찾음
person1= Person('iu')
Person2 = Person('BTS')
Person.number_of_population()



# -정적 메서드(스태틱)
#   클래스와 인스턴스 상관없이 독립적으로 동작하는 메서드
#       주로 클래스와 관련이 있지만 인스턴스와 상호작용이 필요하지 않을경우(일반적인 기능)
#       @staticmethod 데코레이터 사용해서 정의
#       호출시 필수적으로 작성해야 할 매개변수가 없음
#       즉,객체 상태나 클래스 상태를 수정할 수 없으며 단지 기능(행동)만을 위한 메서드로 사용
#       스태틱메서드는 클래스가 호출함 ex) Person.abc(d)



# 클래스가 쓰는거 클래스 메서드, 스태틱 메서드 (but 인스턴스 호출 가능하긴 함)
# 인스턴스가 쓰는거 인스턴스 메서드(but 인스턴스가 자기 없음 class 찾으니 가능하긴 함)
# 다 호출 가능하지만 규칙 지키자!
# 할수있다 != 써도된다


#매직 메서드
# 인스턴스 메서드 (즉 자기자신을 첫 변수로 가져옴 self)
# '__' 던더 스코어 (더블언더스코어)
# ex) __str__ : 인스턴스 자체 출력할때 자동 사용

#데코레이터
# @붙이고 등장
# 다른 함수의 코드를 유지한 채로 수정하거나 확장히기 위해 사용되는 함수





# 1. 인스턴스 메서드
# 2. 정적메서드 (클래스 변수나 인스턴스변수를 사용하지 않는 메서드)
# 3. 클래스메서드 (데코레이터 사용해서 정의하고, 호출시 첫번쨰 인자로 클래스가 전달이 되는 매서드)

# 데코레이터??
# 데코- 함수를 하나 만드는데 그 함수를 수정하지 않고 함수에 특정 기능을 부여할때 사용!!!

def deco(func):     # 1 파라메터로 함수를 받는다.
    def wrapping(value): # 3 함수 안에 새로운 함수 선언
        print('뉴진스'*5)  # 4 꾸미기
        func(value)       # 5 원래 함수를 호출
        print('하입보이요'*3) # 6

    return wrapping   # 2 wrapping 함수 리턴 !!!

@deco
def callname(name):
    print(name)

@deco
def callage(age):
    print(age)

callname('최민호')
callage('39')


# def abc():
#     print('asdf')

# def kfc(edf):
#     edf()

# kfc(abc)

# 인스턴스 메서드 ()
# 정적메서드(클래스 변수나 인스턴스변수를 사용하지 않는 메서드)
# 클래스메서드(데코레이터 사용해서 정의하고, 호출시 첫인자로 클래스다 전달)

# class car:
#     @staticmethod #영향을 미치지 않는 메서드 사용시...
#     def add_price(one,another):
#         print(one+another)

# car.add_price(400, 800)

# class method
class Make_pie:
    cnt=0
    def __init__(self, name):
        self.name = name
        Make_pie.cnt+=1

    @classmethod
    def numberofpie(cls):
        #cls.cnt처럼 cls(클래스) 속성 cnt에 접근할 수 있다.
        print(f'파이를 {cls.cnt}명이 만들고 있습니다.')

a=Make_pie('아아')
b=Make_pie('오이')
c=Make_pie('비둘기')
Make_pie.numberofpie()
a.numberofpie()#사용금지!
