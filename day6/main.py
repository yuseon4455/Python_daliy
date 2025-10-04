from requests import get
websties = (
  "https://google.com",
  "airbnb.com",
  "twitter.com",
  "facebook.com",
  "https://instagram.com"
)

# for x in websties:
#   print("hello")

# for each in websties:
#   print("hello")

# for potato in websties:
#   print("ptato is equals to " + potato)

# startswith() True or False 반환
for website in websties:
  if website.startswith("https://"):
    print("good to go")
  else:
    print("we have to fix it")

for website in websties:
  if not website.startswith("https://"):
    print("have to fix")

# string 안에 변수 넣는 방법 f"string {변수}"
for website in websties:
  if not website.startswith("https://"):
    website = f"https://{website}"
    response = get(website)
    # print(response)
    # print(response.status_code)
    if response.status_code == 200:
      print(f"{website} is OK")
    else:
      print(f"{website} not OK")

results = {}

for website in websties:
  if not website.startswith("https://"):
    website = f"https://{website}"
    response = get(website)
    # print(response)
    # print(response.status_code)
    if response.status_code == 200:
      results[website] = "OK"
    else:
      results[website] = "FAILED"

print(results)



# 오늘 과제
# BLUEPRINT | DONT EDIT

import requests

movie_ids = [
    238, 680, 550, 185, 641, 515042, 152532, 120467, 872585, 906126, 840430
]

# /BLUEPRINT

# 👇🏻 YOUR CODE 👇🏻:
for movie_id in movie_ids:
  response = requests.get(f"https://nomad-movies.nomadcoders.workers.dev/movies/{movie_id}")
  data = response.json()

  print(data['title'])
  print(data['overview'])
  print(data['vote_average'])
# /YOUR CODE