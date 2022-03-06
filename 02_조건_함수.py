#조건문, 함수
if (1 + 1 == 2):
  print("1+1은 2가 맞아");
  
if (1 + 1 != 3):
  print("1 + 1은 3이 맞아");

## 미성년자인지 확인을 하려면?
bard_age = 19
if(bard_age >= 19):
  print('브레드는 성인입니다')
else:
  print('브레드는 미성년자 입니다')

  
chuck_age = 19
if(chuck_age >= 30):
  print('척은 아재입니다')
elif (chuck_age >= 19):
  print('척은 성인입니다')
else: 
  print('척은 미성년자입니다.')

#함수


print('안녕 영희야 잘지내니?')
print('안녕 철수야 잘지내니?')
#인풋을 맏아서 아웃풋을 내는것
def greet(name):
  print(f'안녕 {name}아 잘지내니?')
  
greet('춘식')

def hello_world():
  print('Hello world!')
  
hello_world()

#인자를 순서대로 받는게 헷갈릴 경우
def greet(name, age, location):
  print(f"안녕 {name}야! 넌 {age}살이고 {location}에 사는구나")

# 잘 사용한 예
greet('춘식', 16, '서울')

# 잘못 사용된 예 - 버그
greet('춘식','서울', 20)

# 키워드 아규먼트(kwarg) 함수 생성시 의도된 파라미터의 타입에 맞게 입력을 전달하기위해 사용한다,
greet(name="춘식", location='대구', age=31)


