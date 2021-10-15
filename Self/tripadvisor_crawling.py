import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import numpy as np
import csv

print('Start Crawling')   

ID_data_list = []
Title_data_list = []
Review_date_list = []
DOE_list = []
Review_text_list = []

for r in range(15):
    print("page {} crawling".format(r))
    url_main= "https://www.tripadvisor.com/Attraction_Review-g187497-d190166-Reviews-Basilica_of_the_Sagrada_Familia-Barcelona_Catalonia.html"
    if r == 0:
      url = url_main
    else:
      page =r*10
      url = "https://www.tripadvisor.com/Attraction_Review-g187497-d190166-Reviews-or{}-Basilica_of_the_Sagrada_Familia-Barcelona_Catalonia.html".format(page)

    req = requests.get(url, headers={'UserAgent':""})
    if req.status_code == 200:  
        print("{} page access successfully".format(r))
        res = req.content
        soup = BeautifulSoup(res,'html.parser') 
        blog_items = soup.find('div', 'bPhtn')  
    else:
        print("link erreor")
        break     
    
    #ID 
    ID_items = blog_items.find_all('span',{'class':'WlYyy cPsXC dTqpp'})
    count = 0
    for ID_item in ID_items: 
        ID = ID_item.text
        # print(ID)
        ID_data_list.append(ID) 
                        
    #Title
    Title_items = blog_items.find_all('div',{'class':'WlYyy cPsXC bLFSo cspKb dTqpp'})
    count = 0
    for Title_item in Title_items:  
        Title = Title_item.text
        # print(Title)
        Title_data_list.append(Title)    
        

    #Review_Date
    Review_date_items = blog_items.find_all('div',{'class':'WlYyy diXIH cspKb bQCoY'})
    for Review_date_item in Review_date_items:
        Review_date_contents = Review_date_item.text
        # print(Review_date_contents)
        Review_date_list.append(Review_date_contents)

    #Date of experience
    DOE_items = blog_items.find_all('div', {'class':'fEDvV'})
    for DOE_item in DOE_items:
        DOE = DOE_item.text
        # print(DOE[:8])
        DOE_list.append(DOE[:8])

    #Review_text
    Review_text_items = blog_items.find_all('div', {'class':'WlYyy diXIH dDKKM'})
    for Review_text_item in Review_text_items:
        Review_text = Review_text_item.text
        # print(Review_text)
        Review_text_list.append(Review_text)


    time.sleep(np.random.rand()*20)

mydict = {'ID': ID_data_list,
          'Review_date': Review_date_list,
          'Date_of_experience': DOE_list,
          'Title': Title_data_list,
          'Review_text': Review_text_list}
dataframe = pd.DataFrame.from_dict(mydict, orient='index')
dataframe = dataframe.transpose()
# dataframe = pd.DataFrame({'ID': ID_data_list,
#                           'Review_date': Review_date_list,
#                           'Date_of_experience': DOE_list,
#                           'Title': Title_data_list,
#                           'Review_text': Review_text_list})

# print(dataframe)
dataframe.to_csv('tripadvisor_crawling.csv', index=False, encoding='utf-8')