"""
# list 아님 나열
mon = "Mon"
tue = "Tue"
wed = "Wed"
thu = "Thu"
fri = "Fri"

# list
days_of_week = ["Mon", "Tue", "Wed", "Thu", "Fri"]

print(days_of_week)
"""
# method 사용
name = "nico"

# 대문자 upper method사용
print(name.upper())
# 첫글자만 대문자 capitalize method사용
print(name.capitalize())
# n으로 시작하는지 확인 True or False 반환
print(name.startswith("n"))
#  o을 😒로 변경 replace method사용
#  앞은 바꿀 문자, 뒤는 바뀐 문자
print(name.replace("o","😒"))
# o으로 끝나는지 확인 True or False 반환
print(name.endswith("o"))


days_of_week = ["Mon", "Tue", "Wed", "Thu", "Fri"]

# wed가 몇개 인지는 숫자 세기
print(days_of_week.count("Wed"))

# 반대로 출력  -modify(수정하다)
days_of_week.reverse()
print(days_of_week)

# list에 아이템 추가 -mutate(변화시키다)
days_of_week.append("Sat")
print(days_of_week)

days_of_week.append("Sun")
print(days_of_week)

# list에 있는 아이템 삭제 -mutate(변화시키다)
days_of_week.remove("Sun")
print(days_of_week)

# list에 있는 아이템 전체 삭제 -mutate(변화시키다)
days_of_week.clear()
print(days_of_week)

# list에는 어떤것도 올 수 있음
days_of_week = ["Mon", "Tue", "Wed", "Thu", "Fri"]
# Thu 나옴 - 컴퓨터는 숫자를 0부터 셈
print(days_of_week[3])

# tuple은 list와 비슷하지만 수정 불가 불변임
"""
days_of_week = ("Mon", "Tue", "Wed")
days_of_week =
"""

# [] 안에 -1,0,1,2 등 가능 위치 찾아줌
days_of_week = ("Mon", "Tue", "Wed")
print(days_of_week[2])

# dictionary는 {} 중괄호 사용
# key와 value로 구성
# key는 string, value는 string, number, boolean 등 가능
# key는 중복 불가 value는 중복 가능
# dictionary 안에 속성 만듬
player = {
  'name' : 'nico',
  'age' : 12,
  'alive' : True,
  'fav_food' : ["🍕", "🍔"]
}
print(player)

print(player.get('age'))
print(player.get('fav_food'))