import requests
from bs4 import BeautifulSoup
# https://www.whatismybrowser.com/detect/what-is-my-user-agent
SO_URL = f"https://stackoverflow.com/jobs?q=python&pg=1"

def extract_so_pages():
    result = requests.get(SO_URL, headers={"User-Agent":""})
    soup = BeautifulSoup(result.text, "html.parser")
    # print(soup)
    pages = soup.find("div", {"class":"s-pagination"}).find_all("a")
    last_page = pages[-2].get_text(strip=True)
    # print(last_page)
    return int(last_page)

def extract_job(html):
    title = html.find("h2",{"class":"mb4"}).find("a")['title']
    # print(title.string)
    # print(title)
    company = html.find("h3",{"class":"fc-black-700"}).find("span").string.strip()
    # print(company)
    location = html.find("h3",{"class":"fc-black-700"}).find("span",{"class":"fc-black-500"}).string.strip()
    # print(location)
    job_id = html['data-jobid']
    return {
        "title":title, 
        "company":company, 
        "location":location, 
        "apply-link":f"https://stackoverflow.com/jobs/{job_id}"
    }

def extract_jobs(last_page):
    jobs = []
    for page in range(1, last_page+1):
        # print(page)
        print(f"Scrapping SO page {page}")
        result = requests.get(f"{SO_URL}&pg={page}")
        # print(result.status_code)
        soup = BeautifulSoup(result.text, "html.parser")
        results = soup.find_all("div",{"class":"-job"})
        for result in results:
            # print(result['data-jobid'])
            job = extract_job(result)
            # print(job)
            jobs.append(job)
    return jobs

def get_jobs():
    last_so_pages = extract_so_pages()
    # print(last_so_pages)
    jobs = extract_jobs(last_so_pages)
    return jobs
    
