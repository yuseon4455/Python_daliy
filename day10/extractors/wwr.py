import requests
from bs4 import BeautifulSoup

def extract_wwr_jobs(keyword):
    all_jobs = []
    url = f"https://weworkremotely.com/remote-jobs/search?term={keyword}"

    print(f"Scraping {url}...")

    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")

        jobs = soup.find("section", class_="jobs")
        if jobs:
            job_list = jobs.find_all("li")[1:-1]

            for job in job_list:
                title = job.find("span", class_="title").text.strip()
                company = job.find("span", class_="company").text.strip()
                region = job.find("span", class_="region").text.strip()
                job_url = job.find("a")["href"]

                job_data = {
                    "position": title,
                    "company": company,
                    "location": region,
                    "link": f"https://weworkremotely.com{job_url}",
                }
                all_jobs.append(job_data)
    except Exception as e:
        print(f"Error scraping weworkremotely: {e}")

    return all_jobs