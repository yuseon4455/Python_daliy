"""
nico = {
  "name": "Nico",
  "XP": 1000,
  "team": "Team X",
}
"""
"""
def create_player(name, xp, team):
  return{
    "name": "Nico",
    "XP": 1500,
    "team": "Team X",
  }
# 데이터를 활용하는 함수
def introduce_player(player):
  name = player["name"]
  team = player["team"]
  print(f"Hello! My name is {name} and I play for {team}")

#introduce_player(nico)

nico = create_player("Nico", 1500, "Team X")
lynn = create_player("Lynn", 1500, "Team Blue")

teams = {
  "Team X": ["Nico"],
  "Team Blue": ["Lynn"], 
}
"""
"""
OOP(object-oriented programming)
1. 필요한 구조와 정신적 규칙과 모델을 줘서 더 확장 가능성 있도록 만듬
2. 데이터를 어떻게 구조화해야하는지 알려주고 그 데이터를 수정하기 위해 어디에 어떤 함수를 넣어야하는지 알려줌
3. 명확한 경계를 만들어줌
"""

# class 
# class 안에 있는 모든 method에 대해 자동적으로 항상 첫번째 argument를 받음
"""
class Puppy:

  def __init__(self):
    # print(self)
    # print("Puppy is born!")
    self.name = "Ruffus"
    self.age = 0.1
    self.breed = "Bulldog"

ruffus = Puppy()
bibi = Puppy()

1. puppy 객체를 같은 메모리 주소를 가짐
2. puppy라는 class에 있는 모든 method는 자기 자신에 대한 참조를 받고 있음
3. puupy라는 class에서의 method는 __init__뿐만 아니라 모든 밑줄을 사용하는 method와 우리가 만든 모든 method에 대해 항상 첫번째 argument를 받음(그들 자신을 참조)
4. ruffus와 self는 동일한 puppy 객체를 참조하고 있음

# print(ruffus)
print(ruffus.name, ruffus.age,ruffus.breed) 
"""
"""
# __init__() method가 호출되었을 때 어떻게 어떤 property를 커스텀 할 지-> 공간 만들어주면  
class Puppy:
  def __init__(self,name,breed):
    self.name = name
    self.age = 0.1
    self.breed = breed

  def __str__(self):
    # return "Hello!"
    # 데이터를 별도의 method에서 접근하여 활용
    return f"{self.breed} puppy named {self.name}, breed:{self.breed}"

# puppy의 청사진?을 활용하여 만들어진 object라는 뜻으로 instance라고 
ruffus = Puppy(
  name = "Ruffus",
  breed = "Bulldog"
)
bibi = Puppy(
  name = "Bibi",
  breed = "Maltese"
)

print(
  bibi,
  ruffus,
)
"""
# dictionary를 만들고 파일 제일 위에 함수들을 붙여넣는 것 보다 훨씬 나은 방
class Puppy:
  def __init__(self,name,breed):
    self.name = name
    self.age = 0.1
    self.breed = breed
    
  def __str__(self):
    return f"{self.breed} puppy named {self.name}, breed:{self.breed}"

  def woof_woof(self):
    print("woof woof")

  def introduce(self):
    self.woof_woof()
    print(f"My name is {self.name} and I am a baby {self.breed}")
    self.woof_woof()
    

ruffus = Puppy(
  name = "Ruffus",
  breed = "Bulldog"
)

bibi = Puppy(
  name = "Bibi",
  breed = "Maltese"
)

ruffus.introduce()
bibi.introduce()

# inheritance(상속)
class Dog:
  def __init__(self, name, breed, age):
    self.name = name
    self.breed = breed
    self.age = age

  def sleep(self):
    print("zzzzz")
  
class GuardDog(Dog):

  def __init__(self, name, breed):
    super().__init__(
        name, 
        breed, 
        5,
    )
    self.aggrestive = True
  
  def rrrrr(self):
    print("stay away!")

class Puppy(Dog):

  def __init__(self,name, breed):
    super().__init__(
      name, 
      breed, 
      0.1
    )
    self.spoiled = True
    
  def woof_woof(self):
    print("woof woof")

ruffus = Puppy(
  name = "Ruffus",
  breed = "Bulldog"
)

bibi = GuardDog(
  name = "Bibi",
  breed = "Maltese"
)

ruffus.woof_woof()
bibi.rrrrr()

ruffus.sleep()
bibi.sleep()