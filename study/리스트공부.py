#리스트 관련 메소드
st = ['apple', 'banana','mango']
#맨뒤에 추가
st.append('orange')
print(st)

#중간에 추가
st.insert(1, 'orange') # 1번 인덱스에 오랜지 추가
print(st)
a=st.index('orange',2)
print(a)
# 인설트는 위치먼저 지정
# 인덱스는 위치 나중에 지정
st=[1,2,3]
str2=[4,5]
st.extend(str2)
print(st)
st+=str2
print(st)

#a맨뒤 원소 삭제
st.pop()
print(st)

#지정 위치 삭제
st.remove(4)
#앞에서 부터 탐색하다 지정 문자 나오면  삭제&종료

st.clear() #리스트 항목 삭제
print(st)

#리스트 순서 뒤집기
st=[1,2,3,4,5]
st.reverse()
print(st)

st=st[::-1]
print(st)


#sort로 리스트 정렬하기 = 원본 데이터의 값이 정렬됨
a1 = [6,3,9]
a1.sort()
print(a1)

a1.sort(reverse=True)
print(a1) #내림차순 정렬


a1=[6,3,9]
ret=sorted(a1)
print(a1, reverse = True)
print(ret)

#문자열도 가능할까?
a1 = 'asdf'
# a1.sort()
# print(a1) 버그

a1 = ''.join(a1)
print(a1)

#sort 는 리스트객체만 사용하는 리스트용 메서드
# sorted는 순회가능한 객체
#join 리스트 튜플 문자열을 딕셔너리를 위한 메서드

ret = sorted(st,reverse=True)
ret = sorted(st, key= lambda x:x,reverse=True)
ret = sorted(st, key=lambda x:-x)
print(ret)
# 버그 ret = sorted(ldt,key==lambda x:-x) 
lst = [(3,'banana'),(2,'apple'),(1,'carrot')]
ret = sorted(lst,key=lambda x:x[1], reverse=True)
print(ret)

