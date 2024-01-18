# 딕셔너리 값 출력시 get method 사용

st={'kevin':1, 'john':2, 'bob':3}

print(st['kevin'])
print(st.get('kevin'))
print(st.get('keeeeevin'))
print(st.get('keeeeevin', '없음'))


#print(st['kate']) 버그

print(st.get('kate','없음'))