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