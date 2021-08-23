import re
import requests
from bs4 import BeautifulSoup

SO_URL = f"https://stackoverflow.com/jobs?q=python&pg=1"

def extract_so_pages():
    result = requests.get(SO_URL)
    soup = BeautifulSoup(result.text, "html.parser")
    # print(soup)
    pages = soup.find("div", {"class":"s-pagination"}).find_all("a")
    print(pages)

def get_jobs():
    last_so_pages = extract_so_pages()
    return []
    
