st= 'apple, banana, mango'
index = st.find('a',1)
#    (내가 찾을 문자, n번 인덱스 부터)
print(index)

index = st.find('z',1)
# 찾는 문자 없을 시 -1로 반환
print(index)

alpha = st.index('p')
print(alpha)

alpha = st.index('p',1,len(st))
# 인덱스로 찾는 문자가 없으면 버그
print(alpha)

print(st.isupper()) #전부 대문자냐?
print(st.islower()) #전부 소문자냐?
print(st.isalpha()) #전부 알파뱃이냐?
print(st.count('a')) #'x' 는 몇개냐?
#join (문자열 리스트의 값 합치기)
st = ['a', 'b', 'c', 'd']
str2 = "*".join(st)
print(str2)

st = ['apple', 'banana', 'mango']
str2 = ','.join(st)
print(str2)


str2 = st.upper()
print(str2)
str2 = st.lower()
print(str2)

st=input().lower().split()
#대소문자 전부 다 소문자로 변환
print(st)
st = '   apple   '
#공백 없애기 (스페이스바도 하나의 문자열)
str2 = st.lstrip() #왼쪽 공백 없에기 rstrip은 오른쪽
print(str2)
str2 = st.strip() #왼오 공백 없에기
#replace 문자 바꿔치기
str = 'apple'
str2 = str.replace('a','M')
print(str2)