### 합집합
# 아래 함수를 수정하시오.
def union_sets(s1,s2):
    return s1|s2


result = union_sets({1, 2, 3}, {3, 4, 5})
print(result)

#################################
### 세트와 딕셔너리

my_set = {'가', '나', (0, 0)}
my_dict = {
        '가': 1, 
        (0, 0): '튜플도 키값으로 사용가능'
    }

# 아래에 코드를 작성하시오.
for key in my_set:
    print(my_dict.get(key))
var=(1,2,3,'A')
my_dict[var]='변수로도 키 설정 가능'
print(my_dict)

#################################
### Dict.get()

# 아래 함수를 수정하시오.
def get_value_from_dict(dict,key):
    return dict[key]


my_dict = {'name': 'Alice', 'age': 25}
result = get_value_from_dict(my_dict, 'name')
print(result)  # Alice

#################################
### 딕셔너리 메서드1
data = {
    '이름': '키위',
    '종류': '새',
    '원산지': '호주' 
}

plus_data = {
    '종류': '과일',
    '가격': 30000
}
# 1. data가 가진 모든 키와 벨류 목록을 출력한다.
print(data.items())

# 2. data가 가진 벨류 목록들만 모아서 출력한다.
print(data.values())
# 3. data에서 'without' 키가 가진 value를 출력한다.
    # 해당하는 키가 data에 없다면, 'unknown' 문자열을 출력한다.
print(data.get('without','unknown'))
# 4. plus_data가 가진 모든 키와 벨류를 data에 추가한다.
data.update(plus_data)
# 5. 변경된 data를 출력한다.
print(data)


#################################
### 교집합 Set.intersection()

# 아래 함수를 수정하시오.
def intersection_sets(s1,s2):
    return s1&s2


result = intersection_sets({1, 2, 3}, {3, 4, 5})
print(result)

#################################
### 딕셔너리 메서드2

# 아래에 코드를 작성하시오.
for phone in data:
    for key in key_list:
        if not phone.get(key):
            phone.setdefault(key,'unknown')
        print(f'{key} 은/는 {phone[key]}입니다.')
    print()

#################################
### Dict.keys()

# 아래 함수를 수정하시오.
def get_keys_from_dict(dict2):
    return list(dict2.keys())


my_dict = {'name': 'Alice', 'age': 25}
result = get_keys_from_dict(my_dict)
print(result)  # ['name', 'age']

#################################
### 차집합 Set,difference()

# 아래 함수를 수정하시오.
def difference_sets(s1,s2):
    return s1-s2


result = difference_sets({1, 2, 3}, {3, 4, 5})
print(result)


#-------------------------------------------------------------------

# 1. set 관련 메서드를 확인해 보자

# set (중복을 허용하지 않는 데이터들의 묶음)

# 값 추가
s={1,2,3,4,5}
s.add(6) #1개 추가
s.update([11,12,8,7,6]) # 리스트 안의 원소를 여러개 추가

# 값 삭제
s.remove(16) # 삭제하는 값이 없으면 버그남!!
print(s)
s.discard(16) # discard는 값 없어도 버그 안남!!
print(s)
s.clear() # 다 삭제
print(s)

# 집합
s1={1,2,3,4,5}
s2={2,4,6,8}

#교집합 
print(s1&s2)
print(s1.intersection(s2))

#합집합
print(s1|s2)
print(s1.union(s2)) # union함수 이용하는법도 있음

#차집합
print(s1-s2)
print(s1.difference(s2))

# 부분집합
# s1의 항목이 모두 s2에 들어있으면 True를 반환
print(s1<=s2)
print(s1.issubset(s2))

#부분집합
# s1가 s2의 항목을 모두 포함하면 True를 반환
print(s1>=s2)
print(s1.issuperset(s2))


#-------------------------------------------------------------------

# 2. dictionary 관련 메서드를 확인해 보자

st={'kevin':1,'john':2,'bob':[3,4,5]}

#딕셔너리 값 출력하기

print(st['kevin'])
print(st.get('kevin')) # 1 출력됨
print(st.get('keein')) # none 출력
print(st.get('keein','없음')) #default값을 '없음'으로 셋팅했을 경우


st={'kevin':1,'john':2,'bob':[3,4,5]}

# 딕셔너리 원소 추가하기

# 방법1.
st['kate']='hi' # key 가 없을 시 새로운 key:value 추가
print(st)
st['kevin']=11  # key 가 있다면 기존의 data를 update 
print(st)       # 딕셔너리는 중복된 key값을 가질 수 없음 (중요)

#-------------------------------------------------------------------

# 방법 2.
st.update(camel=11) # key 가 없을 시 새로운 key:value 추가
print(st)          
st.update(kevin=200) # key 가 있다면 기존의 data를 update 

# update 메서드로 여러개의 key value 쌍을 업데이트 가능
# 예시1 > 
st.update(even=200,dandy=300)
# 예시2 >
dict2={'fly':321, 'game':123}
st.update(dict2)
print(st)

#-------------------------------------------------------------------

# 방법 3.
st.setdefault('amy','KOREA') # key 가 없을 시 새로운 key:value 추가
st.setdefault('kevin','KOREA') # key 가 있다면 기존의 data를 update 안함!!!!
                               # 기존 데이터를 보호!!!!

#-------------------------------------------------------------------

#딕셔너리 삭제 (default값 반드시 설정해야 함)
st={'kevin':1,'john':2,'bob':[3,4,5]}

# 방법1.
del st['kevin']  # 없는키를 삭제할 때 key error 난다 !!
print(st)

# 방법2.
st.pop('kevin','없음') # 없는키를 삭제할 때 default 값을 설정 안하면 버그 날 수 있음
print(st)

# * del 그리고 pop의 차이점
# 1. del이 pop 보다 수행속도가 조금 더 빠르다. 

# 2. 삭제 하려는 key가 없다면
#    del은 key error가 나지만 
#    pop은 key error를 방지할 수 있다.

# 3. del은 반환하는 값이 없지만
#    pop은 딕서너리 원소 삭제 후 값을 반환을 한다.

st={'kevin':1,'john':2,'bob':[3,4,5]}
a=st.pop('john','없음')
print(st) 
print(a) # 2가 출력 됨

#-------------------------------------------------------------------

st={'kevin':1,'john':2,'bob':[3,4,5]}

# 키만 가지고 리스트 만들기
lst=st.keys()
print(lst)
print(list(lst)) #리스트형으로 바꿔줘야 함

lst=st.values()
print(list(lst))

lst=st.items()
print(list(lst)) # 리스트 안에 튜플의 형태로 key:value 형태로 저장


#-------------------------------------------------------------------

# [참고만 할 것] _ 수업중에는 안할꺼임
#  (딕셔너리는 순서가 없는 자료형으로 정렬이 의미가 없음)
#  (그냥 재미삼아 해보려면 해보세용)

# lambda 사용해서 딕셔너리 정렬하기

st={'kevin':27,'john':22,'bob':35}

# 나이가 적은순으로 (오름차순) 딕셔너리를 재정렬한다면? 
ret=dict(sorted(st.items(),key=lambda x:x[1]))
print(ret)

print(*ret.keys()) # 나이가 어린 순으로 이름을 출력

# --------------------------------------------------------