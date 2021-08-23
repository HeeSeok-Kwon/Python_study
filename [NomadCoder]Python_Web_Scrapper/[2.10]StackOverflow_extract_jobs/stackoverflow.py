import re
import requests
from bs4 import BeautifulSoup
# https://www.whatismybrowser.com/detect/what-is-my-user-agent
SO_URL = f"https://stackoverflow.com/jobs?q=python&pg=1"

def extract_so_pages():
    result = requests.get(SO_URL, headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"})
    soup = BeautifulSoup(result.text, "html.parser")
    # print(soup)
    pages = soup.find("div", {"class":"s-pagination"}).find_all("a")
    last_page = pages[-2].get_text(strip=True)
    # print(last_page)
    return int(last_page)

def extract_jobs(last_page):
    jobs = []
    for page in range(1, last_page+1):
        # print(page)
        result = requests.get(f"{SO_URL}&pg={page}")
        # print(result.status_code)
        soup = BeautifulSoup(result.text, "html.parser")
        results = soup.find_all("div",{"class":"-job"})
        for result in results:
            print(result['data-jobid'])

def get_jobs():
    last_so_pages = extract_so_pages()
    # print(last_so_pages)
    jobs = extract_jobs(last_so_pages)
    return jobs
    
