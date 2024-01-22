# 할당 // 얕은복사 // 깊은복사
# a=5
# b=5
# a=3

# lst=[1,2,3]
# lst2=lst
# lst[0]=100
# print(lst2[0])

# 얕은복사 (1차원 리스트)
# lst=[1,2,3]
# lst2=lst[:]
# lst[0]=100
# print(lst2[0]) # 1

# 얕은복사 (2차원 리스트)
# lst=[[1,2],[3,4]]
# lst2=lst[:]
# lst[0][0]=100
# print(lst2[0][0]) # 100 출력

# 이차원 리스트 값 복사시->깊은복사
import copy
lst=[[1,2],[3,4]]
lst2=copy.deepcopy(lst)
lst[0][0]=100
print(lst2[0][0])

#  즉 일차원 까지는 [:] 사용해서 복사 가능
#  2차원 부터는 deepcopy 사용!!