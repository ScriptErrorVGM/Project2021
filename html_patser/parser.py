from pyrsistent import b
import requests
from bs4 import BeautifulSoup
from time import sleep
import pandas as pd
import numpy as np
import urllib.parse
import json



def main():
    url = "https://nplus1.ru/"
    page = requests.get(url)
    coverpage = page.content

    soup = BeautifulSoup(coverpage, 'html5lib')
    #print(soup)
    coverpage_news = soup.find_all('a')
    number_of_articles = 109
    list_Links = []
    list_Title = []
    list_Author = []
    list_Time = []
    list_Rubric = []
    list_Diff = []
    list_Text = []

    #List of links and List of titles
    for n in np.arange(0, number_of_articles) :
        if coverpage_news[n]['href'].startswith('/news/') :
            link = coverpage_news[n]['href']
            list_Links.append(link)

            #if coverpage_news[n].find('h3') != None :
            #    title = coverpage_news[n].find('h3')
            #    list_Title.append(title)

    
    #Name of author of articles
    #url1 = urllib.parse.urljoin(url, list_Links[1])
    #page2 = requests.get(url1)
    #coverpage1 = page2.content
    #soup1 = BeautifulSoup(coverpage1, 'html5lib')
    #text_A = soup1.find('h1').text
    #text_B = text_A.find_all('p', {'class' : None})


    for i in np.arange(0, len(list_Links)):
        url1 = urllib.parse.urljoin(url, list_Links[i])
        page2 = requests.get(url1)
        coverpage1 = page2.content
        soup1 = BeautifulSoup(coverpage1, 'html5lib')

        #find title of article
        title = soup1.find('h1').text
        list_Title.append(title)

        #find text of article
        text_A = soup1.find('div', {'class' : 'body js-mediator-article'})
        text_B = text_A.text
        lines = (line.strip() for line in text_B.splitlines())
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        text_C = '\n'.join(chunk for chunk in chunks if chunk)
        list_Text.append(text_C)

        #find difficulty of article
        diff_article = soup1.find('span', {'class' : 'difficult-value'})
        list_Diff.append(diff_article.text)

        #find rubric of title
        rubric = soup1.find('div', {'class' : 'tables'})
        rubric1 = rubric.find_all('a')[0]
        list_Rubric.append(rubric1.text)
        
        #find date of title
        time_Get = soup1.find('time')
        time_Date = time_Get.find_all('span')[1]
        list_Time.append(time_Date.text)    
    
        #find author of title
        author_Get = json.loads(soup1.find('script', type='application/ld+json').string)
        author = (author_Get.get('author')).get('name')
        list_Author.append(author)
    

    #print(list_Title)
    #print(list_Title)
    #print(len(list_Author))
    #print(len(list_Time))
    #print(len(list_Rubric))
    #print(len(list_Diff))
    #print(len(list_Text))
    df = pd.DataFrame({'link' : list_Links, 'date' : list_Time, 
    'author' : list_Author, 'title' : list_Title, 'text' : list_Text,
    'rubric' : list_Rubric, 'diff' : list_Diff})

    df.index = np.arange(1, len(df)+1)
    print(df)
    df.to_csv("info_html.csv", encoding= 'utf-8')
    """url = "https://nplus1.ru/"
    page = requests.get(url)

    text = page.text
    soup = BeautifulSoup(text, "html.parser")
    trs = soup.find_all('h3')
    #print(len(soup.find_all('h3')))
    mass_Link = []

    i = 0
    while i < len(soup.find_all('h3')):
        mass_Link.append(soup.find_all('h3')[i].text)
        i += 1
    
    df = pd.DataFrame({'link' : mass_Link})

    df.index = np.arange(1, len(df)+1)
    #print(df)
    #print(mass_Link)
    print(soup)"""





    """url = "http://nplus1.ru/"
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")
    urls = [x.get('href') for x in soup.find_all("a") if (x.get('href').startswith("/news/")) or 
    (x.get('href').startswith("/blog/"))]
    urls_1 = soup.find_all('div', {"class": "lead"})

    for u in urls:
        print(u.text)"""


    #print(urls_1.text)
    """for u in urls:
        print("Parsing url:", u)
        url_page = requests.get(url + u)
        url_soup = BeautifulSoup(url_page.text, "html.parser")

        with open("output.txt", "w", encoding="UTF-8") as f:
            f.write(url_soup.prettify())
        """


if __name__ == "__main__":
    main()
