# string_number = '1'
# print(string_number+5)
# print(int(string_number)+5)
# name='홍길동'
# age=4
# % string
# print('제 이름은 %s 이고 %d 입니다.'%(name,age))

# str.format
# print('제 이름은 {0} 이고 {1} 입니다.'.format(name,age))

# f-string
# print(f'제 이름은 {name} 이고 {age} 입니다')


# my_list=['python','java','c++','html']
# print(my_list[0])
# my_list[0]='JS'
# print(my_list[0])
#리스트 길이
# print(len(my_list))

# 1번 인덱스~4번 전까지 == 1, 2, 3 출력
# print(my_list[1:4])

# foods=['토스트','햄버거','국밥']
# print(foods[0])
# foods[1]='초밥'
# print(foods[1])

#딕셔너리
# dic={'이름':'최민호','나이':39,'성별':'남'}
#      key : value
# print(dic['성별'])
# dic['나이']=29
# print(dic['나이'])

# my_info={'이름':'김정환','나이':29,'인사말':'안녕하세요'}
# print(my_info)
# print(my_info['나이'])

# phone_number={
#     '최':'010',
#     '민':'9353',
#     '호':'6698',
#     'studyterm':{'stcamp':'3days',
#                  'python':'2weeks',
#                  'algorithm':'6weeks'},
#     111:'굳굳'}

# print(phone_number['studyterm']['python'])

# movie = {
#     'movieInfo': {
#         'movieNm': '광해, 왕이 된 남자',
#         'movieNmEn': 'Masquerade',
#         'showTm': '131',
#         'prdtYear': '2012',
#         'openDt': '20120913',
#         'typeNm': '장편',
#         'nations': [{'nationNm': '한국'}],
#         'genres': [{'genreNm': '사극'}, {'genreNm': '드라마'}],
#         'directors': [{'peopleNm': '추창민', 'peopleNmEn': 'CHOO Chang-min'}],
#         'actors': [
#             {'peopleNm': '이병헌', 'peopleNmEn': 'LEE Byung-hun', 'cast': '광해/하선'},
#             {'peopleNm': '류승룡', 'peopleNmEn': 'RYU Seung-ryong', 'cast': '허균'},
#             {'peopleNm': '한효주', 'peopleNmEn': 'HAN Hyo-joo', 'cast': '중전'},
#         ],
#     }
# }

# 1. 영화의 제목을 출력하시오.
# print(movie['movieInfo']['movieNm'])

# 2. 다음 movie의 감독의 영어 이름을 출력하시오.
# print(movie['movieInfo']['directors'][0]['peopleNmEn'])

# 3. 다음 movie의 배우의 인원을 출력하시오.
# print(len(movie['movieInfo']['actors']))

# 조건문
# a = int(input())
# if a>3:
#     print('오삼')
# if a<1:
#     print('불고기')
# elif a>5:
#     print('냉면')
# else:
#     print('만세')

# a = int(input())
# if a%2==0:
#     print('짝수')
# else:
#     print('홀수')
# a = int(input())
# if a>0:
#     print('양수')
# elif a==0:
#     print('영')
# else:
#     print('음수')
# x=1
# while x <=7:
#     print('@',end='') #출력하고 공백없이 옆에 이어서 출력 하겠다
#     x+=1

# print()

# for x in range(10): # 0~ 10전까지 즉 9까지 10번 반복한다
#     print('*',end=' ') #출력하고 공백1개하고 옆에 이어서 출력 하겠다

# print()

# for x in range(1,11): #1~11전까지 즉 10까지 10번 반복
#     print('*',end=' ')


# number=[1,2,3,4,5,6,7,8,9]
# for x in range(len(number)):
#     if(number[x]%2 == 1):
#         print('%d은(는) 홀수 입니다.'%(number[x]))

# x=0
# while x < len(number):
#     if number[x]%2 ==1:
#         print(f'{number[x]}은(는) 홀수 입니다.')
#     x+=1

# for x in range(10):
#     print('*',end='')

# print()

# x=0
# while x < 10:
#     print('*',end='')
#     x+=1

# print()



# for x in range(33, 11,-1):
#     print(x,end=' ')

# print()



# y=33
# while y >=12:
#     print(y,end=' ')
#     y-=1

# print()

# test=[2,6,4,1,8,4,14,5,7]
# for x in range(len(test)):
#     if test[x]%2==1:
#         print(test[x],end=' ')

# print()

# for x in test:
#     if x%2==1:
#         print(x,end=' ')


# print()

# z = 0
# while  z < len(test):
#     if test[z]%2==1:
#         print(test[z],end=' ')
#     z+=1


# def abc():
#     print(' ()  ()')
#     print(' (  * * )')
#     print(' (      )')
#     print(' ()    ()')

# abc()
# print()
# abc()

#모듈 == 함수 또는 변수등을 이용해서 미리 만들어 놓은 코드(파일)
# import random
# menu=['새마을','영미','나정상회']
# select_lunch=random.choice(menu)
# print(select_lunch)

# select_lunch=random.choices(menu,k=2)
# print(select_lunch)

# select_lunch=random.sample(menu,k=2) # 중복없이 랜덤을 2개 뽑는다
# print(select_lunch)


# a, b = map(int,input().split())
# print(type(a))
# print(type(b))
# print(a+b)
# print(f'두 숫자의 차는 {a-b} 입니다.')

# a, b = map(int,input().split())
# print('%d+%d=%d'%(a,b,a+b))
# print(f'{a}*{b}={a*b}')
# print('{0}/{1}={2}'.format(a,b,a//b))
