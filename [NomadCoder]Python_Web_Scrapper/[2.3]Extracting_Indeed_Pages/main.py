import requests
from bs4 import BeautifulSoup

b_tag = []
for i in range(0, 901, 50):
    indeed_result = requests.get("https://kr.indeed.com/%EC%B7%A8%EC%97%85?as_and=python&limit=50&start={}".format(i))

    indeed_soup = BeautifulSoup(indeed_result.text, "html.parser")
    # print(indeed_soup)

    pagination = indeed_soup.find("div", {"class":"pagination"})
    # print(pagination)

    pages = pagination.find_all('li')
    # print(pages)
 
    for page in pages:
        current = page.find("b")
        if current != None:
            b_tag.append(current)

print(b_tag)

