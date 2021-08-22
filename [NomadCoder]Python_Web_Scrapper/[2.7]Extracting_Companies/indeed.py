import re
import requests
from bs4 import BeautifulSoup

LIMIT = 50
# INDEED_URL = f"https://kr.indeed.com/%EC%B7%A8%EC%97%85?as_and=python&limit={LIMIT}&start="
INDEED_URL = f"https://kr.indeed.com/%EC%B7%A8%EC%97%85?q=python&limit={LIMIT}&filter=0"

# 현재 페이지를 루프를 돌며 리스트에 담기
# def extract_indeed_pages():
#     b_tag = []
#     for i in range(0, 901, 50):
#         result = requests.get(INDEED_URL+"{}".format(i))

#         soup = BeautifulSoup(result.text, "html.parser")
#         # print(indeed_soup)

#         pagination = soup.find("div", {"class":"pagination"})
#         # print(pagination)

#         pages = pagination.find_all('li')
#         # print(pages)
        
#         for page in pages:
#             current = page.find("b")
#             if current != None:
#                 b_tag.append(int(current.string))

#     # print(b_tag[-1])
#     max_page = b_tag[-1]
#     # print(range(max_page))
#     # for n in range(max_page):
#     #     print(f"start={n*50}")
#     return max_page

def extract_indeed_pages():
    result = requests.get(INDEED_URL)

    soup = BeautifulSoup(result.text, "html.parser")

    searchCountPages = soup.find("div",{"id":"searchCountPages"})

    searchCountPages = searchCountPages.string.strip()
    numbers = re.sub(r'[^0-9]', '', searchCountPages[1:])
    if (int(numbers)%LIMIT) != 0:
        countpages = int(numbers)//LIMIT + 1
    else:
        countpages = int(numbers)//LIMIT
    return countpages

def extract_indeed_jobs(last_pages):
    jobs = []
    # for page in range(last_pages):
    #     # print(f"&start={page*LIMIT}")
    #     result = requests.get(f"{INDEED_URL}&start={page*LIMIT}")
    #     # print(result.status_code)
    #     soup = BeautifulSoup(result.text, "html.parser")
    #     results = soup.find_all("div", {"class":"job_seen_beacon"})
    #     print(results)
    
    # Test Code
    result = requests.get(f"{INDEED_URL}&start={0*LIMIT}")
    soup = BeautifulSoup(result.text, "html.parser")
    results = soup.find_all("div", {"class":"slider_container"})
    # print(results)
    for res in results:
        title = res.find("span", title=True).string
        company = res.find("span", {"class":"companyName"})
        if company is not None:
            company = company.string
        else:
            company = None
        print(title, company)
    return jobs
        
