'''
* 문자열 인덱싱

- 파이썬은 문자열을 기본 타입으로 지정했을 뿐만 아니라
문자열을 관리하는 풍부한 명령을 가지고 있습니다.

- 문자열은 메모리상에 낱말(단일문자) 하나하나가
일렬로 늘어선 형태로 저장되는 시퀀스 구조입니다. (순차적 구조)

- 문자열의 각 문자들은 인덱스(index)로 관리되며
맨 앞글자부터 0번이 저장되며, 그 뒤로 1씩 순차적으로 증가합니다.
'''
s = 'python'
# [p, y, t, h, o, n]
print(s)
print(s[2])
print(s[5])
print(s[-1])
print(s[-5])

# 인덱스 범위를 초과한 값을 참조하면 에러가 발생합니다.
# print(s[6]) (x)

# 문자열도 리스트처럼 순차적 자료형이기 때문에
# 반복문 for를 통해 단일 문자 반복이 가능합니다.

for n in s:
    print(n, end='!')

print() # 단순 줄 개행

for day in '월화수목금토일':
    print(day + '요일')