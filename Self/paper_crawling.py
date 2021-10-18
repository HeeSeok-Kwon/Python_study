from bs4 import BeautifulSoup
import pandas as pd
import time
import numpy as np
import csv
import urllib # 한글 - 유니코드 인코딩
import re
from selenium import webdriver
import urllib.request


Author = []
Title_kor = []
Title_eng = []
Book = []
Keyword = []
Txt_kor= []
Txt_eng = []
Url = []

def get_URL(page, word):
    word = urllib.parse.quote(word)
    url_before_page="http://www.riss.kr/search/Search.do?isDetailSearch=N&searchGubun=true&viewYn=OP&queryText=&strQuery="+word+"&exQuery=&exQueryText=&order=%2FDESC&onHanja=false&strSort=RANK&p_year1=&p_year2=&iStartCount="
    url_after_page="&orderBy=&mat_type=&mat_subtype=&fulltext_kind=&t_gubun=&learning_type=&ccl_code=&inside_outside=&fric_yn=&image_yn=&gubun=&kdc=&ttsUseYn=&l_sub_code=&fsearchMethod=search&sflag=1&isFDetailSearch=N&pageNumber=1&resultKeyword=%EB%B9%84%ED%8A%B8%EC%BD%94%EC%9D%B8&fsearchSort=&fsearchOrder=&limiterList=&limiterListText=&facetList=&facetListText=&fsearchDB=&icate=re_a_kor&colName=re_a_kor&pageScale=10&isTab=Y&regnm=&dorg_storage=&language=&language_code=&clickKeyword=&relationKeyword=&query="+word
    url=url_before_page+page+url_after_page
    return url

def get_link(search_word, page_num):
    for i in range(page_num):
        current_page=i*10
        url=get_URL(str(current_page), search_word)
        source_code_from_URL = urllib.request.urlopen(url)
        soup=BeautifulSoup(source_code_from_URL, 'lxml', from_encoding='utf-8')
        try: 
            page_link = soup.select("li > div.cont > p.title > a") 
        except:
            page_link = ""
        
        if i != 0 and i%2 == 0: 
            print("Waiting...for get URL") 
            time.sleep(10) 

        print("crawling start page {}".format(i))
        for j in range(10):
            try:
                page_url = "http://riss.or.kr"+page_link[j].attrs['href'] 
            except:
                print("Index error!")
                break
            # print(page_url)
            reference_data = get_reference(page_url)

            Author.append(reference_data[0])
            Title_kor.append(reference_data[1])
            Title_eng.append(reference_data[2])
            Book.append(reference_data[3])
            Keyword.append(reference_data[4])
            Txt_kor.append(reference_data[5])
            Txt_eng.append(reference_data[6])
            Url.append(reference_data[7])

        print("crawling done page {}".format(i))

    mydict = {'저자': Author,
              '국문제목': Title_kor,
              '영문제목': Title_eng,
              '수록지': Book,
              '핵심어': Keyword,
              '국문 요약':Txt_kor,
              '영문 요약':Txt_eng,
              '링크': Url}
    
    save_csv(mydict, search_word)

def get_reference(url):
    option = webdriver.ChromeOptions()
    option.add_argument("headless")
    driver = webdriver.Chrome("./chromedriver", options=option) 
    driver.get(url) 
    time.sleep(2)

    html = driver.page_source
    soup = BeautifulSoup(html, "lxml")
    title = soup.find("h3",{"class":"title"})
    
    title_txt = title.get_text("", strip=True).split('=')
    
    title_kor = re.sub("\n\b", "", str(title_txt[0]).strip())
    try:
      title_eng = str(title_txt[1]).strip()
    except:
      title_eng = "None"
    
    txt_box = []
    
    for text in soup.find_all("div", {"class":"text"}):
        txt = text.get_text("", strip=True)
        txt_box.append(txt)
    
    try:
      txt_kor=txt_box[1]
    except:
      txt_kor = "None"
    try:
      txt_eng=txt_box[3]
    except:
      txt_eng = "None"
    
    author = "None"
    book = "None"
    keyword = "None"
    detail_box = []
    detail_info = soup.select("#soptionview > div > div > div.infoDetail.on > div.infoDetailL > ul > li > div > p") 
    
    for detail in detail_info:
        detail_concept=detail.get_text("", strip=True)
        
        detail_wrap=[]
        detail_wrap.append(detail_concept)
        
        detail_box.append(detail_wrap)
        
    author = ",".join(detail_box[0])
    
    book=(
        "".join(detail_box[2]+detail_box[3]).replace("\n", "").replace("\t","").replace(" ","")
        + "p."
        +"".join(detail_box[-2])
    )
    
    keyword=",".join(detail_box[6])
        
    reference_data = [
        author,
        title_kor,
        title_eng,
        book,
        keyword,
        txt_kor,
        txt_eng,
        url,
    ]

    driver.close()
    return reference_data

def save_csv(mydict, search_word):
    dataframe = pd.DataFrame.from_dict(mydict, orient='index')
    dataframe = dataframe.transpose()
    dataframe.to_csv(search_word+'_paper_crawling.csv', index=False, encoding='utf-8')

search_word = '블록체인'
page_num = 10
get_link(search_word, page_num)

# install selenium : https://chancoding.tistory.com/136 
