class SMS: 
  def send(self, from_number, to_number, body):
    print(f"{from_number}에서 {to_number}로 {body}가 왔습니다")
    
  def ping(self, to_number):
    print(f"{to_number}로 핑을 보냈습니다")