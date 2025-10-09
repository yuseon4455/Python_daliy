# final
from flask import Flask, render_template, request
from extractors.berlinstartup import extract_berlinstartup_jobs
from extractors.web3 import extract_web3_jobs
from extractors.wwr import extract_wwr_jobs

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

# 가짜 데이터베이스
db = {}

@app.route("/search")
def search():
    keyword = request.args.get("keyword")

    if keyword in db:
        jobs = db[keyword]
    else:
        # 3개 사이트에서 모두 검색
        berlinstartup = extract_berlinstartup_jobs(keyword)
        web3 = extract_web3_jobs(keyword)
        wwr = extract_wwr_jobs(keyword)

        jobs = berlinstartup + web3 + wwr

        # 캐시에 저장
        db[keyword] = jobs

    return render_template("search.html", keyword=keyword, jobs=jobs)

app.run("0.0.0.0")