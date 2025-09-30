print(True)
print("hello")
print(12)

# function 생성 ->정의
# 공백 주의!
# 파이썬에서는 코드를 두카나 들여써줘야 그 코드가 어떤 것 안에 들어있다는걸 알 수 있다.
# function을 호출할 때 function이 실행될 코드를 작성해야한다.
def say_hello():
  print("hello how r u?")

# 함수 안에 넣으면 say_hello()가 실행이 안된다.
def say_bye():
  print("bye bye")
  # say_hello()

say_hello()
# 코드 재사용 가능
say_hello()
say_hello()

say_bye()

# 괄호()
print("hello world")

# 함수 안 데이터
# user_name, 즉 플레이스홀더는 parameter
# parameter는 함수에 있는 변수
def say_hi(user_name, user_age):
  print("hello", user_name," how r u?") 
  print("you are", user_age, "years old")

# argument는 함수에 있는 데이터
# 데이터 순서 중요!
say_hi("nico",30)
# 필요 데이터를 전부 보내지 않아 나는 에
# say_hi("lynn")
say_hi("lewis",31)
say_hi("risa",32)

# 마무리
def tax_calculator(money):
  print(money * 0.35)
  
tax_calculator(1500)
tax_calculator(1500000000)