# 클래스 => 오브젝트를 만드는 함수
# 오브젝트 클래스로 만든 각각의 오브젝트
# def __init__(self)
# __init__() 함수는 constructor 로써 클래스를 이요해서 만들어지는 오브젝트가 가져야하는 속성들은 지정해줘야 한다.
# self 자기자신에게 접근할때
class Person: 
  # consturctor : 생성자
  def __init__(self,name,age, hometown):
    self.name = name
    self.age = age
    self.homtown = hometown
  
  def say_hello(self):
    print("안녕 나는" + self.name + '이고 나는' + str(self.age) + '살이야')
    

p1 = Person('춘식1',16,'카카오')
p2 = Person('춘식2',18,'네이버')
p3 = Person('춘식3',20,'카카오게임즈')

p1.say_hello()

# 상속
# Programmer는 person 을 상속한다
class Programmer(Person):
  def code(self):
    print('나는 코딩을 한다 타닥타닥')
    
class Chef(Person):
  def cook(self):
    print("나는 요리를 한다 보글보글")
    
p4 = Programmer('프로그래머 춘식', 16, '대구')
c1 = Chef('쉐프 춘식', 20, '서울')

p4.say_hello()
p4.code()

