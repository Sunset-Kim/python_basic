# 반복문
# print('Hello World')

# for loop
# range(n) => 0 부터 n-1까지의 숫자를 차례대로 만드는 함수
for x in range(5): 
  print(x)
  print('Hello World')
  
# while loop
x = 0
while x < 5:
  print('Hello World2')
  x += 1
  
  
# 무한루프 경험하기
import time
while 1 > 0:
  print('무한 루프 경험중')
  time.sleep(1)
  