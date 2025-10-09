import requests
from bs4 import BeautifulSoup

def extract_berlinstartup_jobs(keyword):
    all_jobs = []
    url = f"https://berlinstartupjobs.com/skill-areas/{keyword}/"

    print(f"Scraping {url}...")
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }

    try:
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, "html.parser")
        jobs = soup.find_all("div", class_="bjs-jlid__wrapper")

        for job in jobs: 
            title = job.find("h4", class_="bjs-jlid__h").find("a").text.strip()
            company = job.find("a", class_="bjs-jlid__b").text.strip()
            region = "Berlin, Germany"
            job_url = job.find("h4", class_="bjs-jlid__h").find("a")["href"]

            job_data = {
                "position": title,
                "company": company,
                "location": region,
                "link": job_url,
            }
            all_jobs.append(job_data)
    except Exception as e:
        print(f"Error scraping berlinstartupjobs: {e}")

    return all_jobs