#### 1. list 배열
# 사용법
from traceback import print_tb


x = list()
x = [1,2,3]

x.append(4)
x.pop()
print(x)

# 사용용도
# 1. 여러개의 엘레먼트를 담을때
# 2. 엘레멘트를 순서대로 담고 싶을때
# 3. 변수 안에 있는 내용물을 바꿀것 같을때


##### 2. tuple - 안에 있는 내용물을 바꿀 수 없음
x = tuple()
x = (1,2,3);
# x[0] = '민수'  이렇게 할 수 없다

print(x)

# list- 내용물을 바꿀 수 있는 자료구조: mutable (값이 변할 수 있음)
# tuple - 내용물을 바꿀 수 없는 자료구죠 immutable (불변)

##### 3. Set - 세트 (immutable)
# - 순서가 뒤죽박죽이 될 수 있다.
# - Set는 immutable - 내용물을 바꿀 수 없음
# - 어떤 내용이 있는지 확인하는게 편하다

x = set((1,2,3,4))


y = {1, 2}

print(x,y)

# in은 왼쪽에 있는 값이 오른쪽에 있는 자료구조 안에 들어있는지 확인할 때 쓰는 연산자
print(1 in x)
print(1 in y)


#### 4. dictionary (딕셔너리 | 해쉬 테이블 | 사전)
x = {}
x = dict()
print(x)

# key value
x["이름"] = "민수"
x["나이"] = 20
print(x)

# - 순서가 뒤죽박줄일 수 있다.
# - key에 해당하는 값을 나중에 불러오고 싶을때
# - 어떤 엘레먼트가 자료 구조안에 들어있는지 빨리 알고 싶을때


# 정리
# list vs tuple
# mutable : immutable

# set vs dictionary
# set: kye-value 가 필요없고 value만 필요할때
# dictionary key-value가 필요할때

# list + tuple vs dictionary + set
# list + tuple
# 1)  순서가 정해져있다 (ordered)
# 2) 맴버쉽 검색이 느리다
# dictionary + set
# 1) 순서가 정해져 있지 않다. (unordered)
# 2) 맵버쉽 검색이 빠르다

