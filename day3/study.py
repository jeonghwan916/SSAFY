x=3
y=1 #할당

#swap 변수 내용을 교대함
y,x = x,y

a=3
print(type(a))

a=3.14
print(type(a))

#정수로 출력
print(round(a,1))

#문자로 출력
print(f'{a:1f}')

a=3.15
print(type(a))

#정수로 출력
print(round(a,1))

a=1.2-1.1
print(a)


#5초과일때 반올림, 5미만일때 버림
#5일경우 5앞에 있는 수가 짝수면 버림, 홀수면 올림
print(round(0.4)) #0
print(round(0.6)) #1

print(round(0.5)) #0
print(round(1.5)) #2
print(round(2.5)) #2
print(round(3.5)) #4
print(round(4.5)) #4

#부동소숫점 오류로 잘 작동이 안됨
print(round(0.15,1)) #0.1
print(round(0.25,1)) #0.2
print(round(0.35,1)) #0.3
print(round(0.45,1)) #0.5
print(round(0.55,1)) #0.6

#끝에 작은 수를 더해주면 해결
print(round(0.5+0.001,1)) #0.5
print(round(1.5+0.001,1)) #1.5
print(round(2.5+0.001,1)) #2.5
print(round(3.5+0.001,1)) #3.5
print(round(4.5+0.001,1)) #4.5

#지수 표기법
print(round(0.5+1e-8,1)) # == 1*10^-8 == 0.00000001


# math 모듈 사용하기 (느려짐)
import math
print(math.floor(0.5+0.5)) #1
print(math.floor(1.5+0.5)) #2
print(math.floor(2.5+0.5)) #3
print(math.floor(3.5+0.5)) #4
print(math.floor(4.5+0.5)) #5
print(math.floor(5.5+0.5)) #6