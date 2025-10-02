# age = input("How old are you?")
# print(type(age))

# 음주 나 계산기
# age = int(input("How old are you?"))

# if age < 18:
#   print("You can't drink.")
# elif age >=18 and age <=35:
#   print("You drink beer.")
# elif age ==60 or age ==70:
#   print("Birthday party!")
# else:
#   print("Go ahead.")

#True and True == True
#False and True == False
#True and False == False
#False and False == False

#True or True == True
#True or False == True
#False or True == True
#False or False == False

# 카지노
# 큰 주석 """
"""
from random import randint

user_choice = int(input("Choose number: "))
pc_choice = randint(1,50)

if user_choice == pc_choice:
  print("You won!")
elif user_choice > pc_choice:
  print("Lower! Computer chose", pc_choice)
elif user_choice < pc_choice:
  print("Higher! Computer chose", pc_choice)
"""

# 한번만 실행
# if True:
#   print("Hi im True")
  
# 무한 반복
# while True:
#   print("Hi im True")

# 한번도 실행 안됨
# while False:
#   print("Hi im False")

# false가 될 때 까지 실행
"""
distance =0 

while distance < 20:
  print("I'm running:", distance, "km")
  distance = distance + 1
"""
"""
from random import randint

print("Welcome to Python Casino")
pc_choice = randint(1,50)

playing = True

while playing:
  user_choice = int(input("Choose number(1-100): "))
  
  if user_choice == pc_choice:
    print("You won!")
    playing = False
  elif user_choice > pc_choice:
      print("Lower!")
  elif user_choice < pc_choice:
      print("Higher!")
"""
# 과제
playing = True

while playing:
  num1 = input("Choose number: ")
  if num1.lower() == "exit":
    break
    
  num2 = input("Choose another one: ")
  if num2.lower() == "exit":
    break

  operation = input("Choose an operation ( +, -, *, /) or 'exit' to finsh: ")
  if operation.lower() == "exit":
    break

  num1 = int(num1)
  num2 = int(num2)
  
  if operation == "+":
    result = num1 + num2
  elif operation == "-":
    result = num1 -num2
  elif operation == "*":
    result = num1 * num2
  elif operation == "/":
    result = num1 / num2
  else:
    print("Unknown operation!")

  print("Result: ", result)