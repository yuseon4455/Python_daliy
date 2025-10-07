"""
letters = ["a", "b", "c"]
a, b, c = letters  --> ! 반드시 갯수에 맞는 variable 이름을 작성해야함
a -> 'a'
b -> 'b'
c -> 'c'
"""
"""
# beautifulsoup4 설치
import requests
from bs4 import BeautifulSoup

all_jobs = []

def scrape_page(url):
  print(f"Scraping {url}...")
  response = requests.get(url)
  soup = BeautifulSoup(
    response.content,
    "html.parser",
  )
url = "https://weworkremotely.com/categories/remote-full-stack-programming-jobs"

response = requests.get(url)

# print(response.content)
soup = BeautifulSoup(
    response.content,
    "html.parser",
  )
# 전체구조확인 -> html 코드 수정됨
# jobs_section = soup.find("section", class_="jobs")
# print(jobs_section)

# jobs = soup.find("section", id = "category-2")
# class는 파이썬에서 예약어라서 class_로 써야함
jobs = soup.find("section", class_ = "jobs").find_all("li")[1:-1]

for job in jobs:
  # title = job.find("span", class_="title")
  title = job.find("h3", class_="new-listing__header__title").text
  region = job.find("p", class_="new-listing__company-headquarters").text
  company = job.find("p", class_="new-listing__company-name").text
  tooltip = job.find("div", class_="tooltip--flag-logo")
  url = tooltip.next_sibling["href"]
  print(title, company, region, "----\n")
  # dictionary로
  job_data = {
    "title" : title,
    "company" : company,
    "region" : region,
    "url": f"https://weworkremotely.com{url}",
  }
  all_jobs.append(job_data)
  print(job_data)

# pagination
response = requests.get("https://weworkremotely.com/remote-full-time-jobs?page=1")
soup = BeautifulSoup(response.content, "html.parser")

buttons = len(soup.find("div", class_="pagination").find_all("span",class_="page"))
print(buttons)

def get_pages(url):
  response = requests.get(url)
  soup = BeautifulSoup(response.content, "html.parser")
  return len(soup.find("div",class_="pagination").find_all("span",class_="page"))

total_pages = get_pages("https://weworkremotely.com/remote-full-time-jobs?page-1")

# pagination은 1부터 시작--> {x+1}
for x in range(total_pages):
  url = f"https://weworkremotely.com/remote-full-time-jobs?page={x+1}"
  # print("request page",x+1)
  scrape_page(url)

print(len(all_jobs))



import requests
from bs4 import BeautifulSoup

# code_change_ex
keywords = [
  "flutter",
  "python",
  "golang"
]

r = requests.get("https://remoteok.com/remote-flutter-jobs",headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0."})

# print(r.status_code)
# print(r.content)
"""

# code_change
import requests
from bs4 import BeautifulSoup

all_jobs = []

def scrape_page(url):
    print(f"Scraping {url}...")
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")

    jobs = soup.find_all("div", class_="bjs-jlid__wrapper")

    for job in jobs:
        title = job.find("h4", class_="bjs-jlid__h").find("a").text.strip()
        company = job.find("a", class_="bjs-jlid__b").text.strip()
        region = "Berlin, Germany"
        url = job.find("h4", class_="bjs-jlid__h").find("a")["href"]

        job_data = {
            "title": title,
            "company": company,
            "region": region,
            "url": url,
        }
        all_jobs.append(job_data)

def get_pages(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")

    pagination = soup.find("nav", class_="pagination")
    if pagination:
        return len(pagination.find_all("a", class_="page-numbers"))
    return 1

# URL 리스트
urls = [
    "https://berlinstartupjobs.com/engineering/",
    "https://berlinstartupjobs.com/skill-areas/python/",
    "https://berlinstartupjobs.com/skill-areas/typescript/",
    "https://berlinstartupjobs.com/skill-areas/javascript/"
]

for url in urls:
    total_pages = get_pages(url)
    for x in range(total_pages):
        page_url = f"{url}page/{x+1}/" if x > 0 else url
        scrape_page(page_url)

print(len(all_jobs))