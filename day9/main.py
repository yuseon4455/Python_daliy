"""
from extractors.indeed import extract_indeed_jobs
from extractors.wwr import extract_wwr_jobs
from file import save_to_file

keyword = input("What do you want to search for?")

indeed = extract_indeed_jobs(keyword)
wwr = extract_wwr_jobs(keyword)
jobs = indeed + wwr

save_to_file(keyword,jobs)

# flask를 이용한 웹사이트 만들기
from flask import Flask, render_template

# flask를 실행하기 위한 코드이며 Flask("JobScrapper")로 하니까 home.html을 찾을 수 없었다. -> Flask에서는 jobscrapper라는 이름만 알고 어디서 실행되는지 모른다.
# Flask(__name__)은 파일 정보를 주고 Flask는 main.py의 위치를 알고 그 위치 기준으로 templates 폴더를 찾는다.
app = Flask(__name__)

# @app.route("/")랑 def home():은 home이라는 함수를 /에 연결하겠다는 의미라서 붙어있어야
@app.route("/")
def home():
  # return 'hey there!'
  # return "<h1>Hey there</h1><a href='/hello'>go to hello</a>"
  return render_template("home.html", name="nico")

# @app.route("/hello")
# def hello():
#   return "hello you"
@app.route("/search")
def hello():
  return render_template("search.html")

app.run("0.0.0.0")

from flask import Flask, render_template,request

app = Flask(__name__)

@app.route("/")
def home():
  return render_template("home.html", name="nico")

# search.html에서 keyword를 받아서 search.html에 keyword를 보내준다.(변수명을 받아서 보내주는 것)
# reqeust의 args에서 keyword를 가져와서(url의 물음표 뒤에 있는 arguments에서 keyword를 가져와서 keyword를 search.html에 보내고 search.html은 UI에 받은 keyword를 사용한다. Flask는 {{변수이름}}를 실제 변수의 값으로 대체하고 있음)
@app.route("/search")
def search():
  keyword = request.args.get("keyword")
  return render_template("search.html",keyword=keyword)

app.run("0.0.0.0")

search.html에 넣고 싶은데 오류나서 여기에 씀
{{}} and {% %} 차이
<!-- 변수랑 같은 이름을 사용해야함 -->
<!-- Flask template 안에서 job 안의 link에 접근하는 방법임 -->
<!-- 
  {{}}는 안에 variable을 넣으면 Flask가 이 variable을 값으로 변환해줌
{% %} 안에는 우리가 실행하고 싶은 python코드를 넣음
    -->

# keyword를 사용해서 extrator를 호출
from flask import Flask, render_template,request
from extractors.indeed import extract_indeed_jobs
from extractors.wwr import extract_wwr_jobs

app = Flask(__name__)

@app.route("/")
def home():
  return render_template("home.html", name="nico")

@app.route("/search")
def search():
  keyword = request.args.get("keyword")
  indeed = extract_indeed_jobs(keyword)
  wwr = extract_wwr_jobs(keyword)
  jobs = indeed + wwr
  return render_template("search.html",keyword=keyword, jobs=jobs)

app.run("0.0.0.0")
"""
# Cache
from flask import Flask, render_template,request
from extractors.indeed import extract_indeed_jobs
from extractors.wwr import extract_wwr_jobs

app = Flask(__name__)

@app.route("/")
def home():
  return render_template("home.html", name="nico")

# 가짜 데이터베이스, 서버가 켜져있을때만 메모리에 있음
db = {}

@app.route("/search")
def search():
  keyword = request.args.get("keyword")
  if keyword in db:
    jobs = db[keyword]
  else:
    indeed = extract_indeed_jobs(keyword)
    wwr = extract_wwr_jobs(keyword)
    jobs = indeed + wwr
    db[keyword] = jobs
  return render_template("search.html",keyword=keyword, jobs=jobs)

app.run("0.0.0.0")

