def extract_indeed_jobs(keyword):
        # 테스트용 더미 데이터
        return [
            {
                "position": f"{keyword} Developer",
                "company": "Indeed Company",
                "location": "Seoul, Korea",
                "link": "https://kr.indeed.com/job/12345"
            },
            {
                "position": f"Senior {keyword} Engineer",
                "company": "Tech Corp",
                "location": "Busan, Korea",
                "link": "https://kr.indeed.com/job/67890"
            }
        ]