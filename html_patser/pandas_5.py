import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np


def main():
    #url = "http://www.vybory.izbirkom.ru/region/izbirkom?action=show&root=1&tvd=100100084849070&vrn=100100084849062&prver=0&pronetvd=null&region=4&sub_region=4&type=227&report_mode=null"
    url = "https://ru.wikipedia.org/wiki/%D0%9C%D0%B5%D0%B6%D0%B4%D1%83%D0%BD%D0%B0%D1%80%D0%BE%D0%B4%D0%BD%D1%8B%D0%B9_%D0%B8%D0%BD%D0%B4%D0%B5%D0%BA%D1%81_%D1%81%D1%87%D0%B0%D1%81%D1%82%D1%8C%D1%8F"
    page = requests.get(url)

    text = page.text
    soup = BeautifulSoup(text, "html.parser")
    trs = soup.select('table.wikitable')[2]
    
    mass_Index = []
    mass_Country = []
    mass_HPI = []
    mass_Satis_Life = []
    mass_Long_Life = []
    mass_Eco = []

    
    c = 0
    while c < len(trs.find_all('span', {"class" : "wrap"})):
        mass_Country.append(trs.find_all('span', {"class" : "wrap"})[c].text)
        c += 1

    i = 2
    while i < len(trs.select('td')):
        mass_HPI.append(float(trs.select('td')[i].text))
        mass_Satis_Life.append(float(trs.select('td')[i+1].text))
        mass_Long_Life.append(float(trs.select('td')[i+2].text))
        mass_Eco.append(float(trs.select('td')[i+3].text.strip()))
        i += 6

    df = pd.DataFrame({'Страна' : mass_Country, 'HPI' : mass_HPI, 
    'Удовлетворенность жизнью' : mass_Satis_Life, 
    'Ожидаемая продолжительность жизни' : mass_Long_Life, 
    'Экологический след' : mass_Eco})

    df.index = np.arange(1, len(df)+1)
    print(df)
    df.to_csv(" html-Михайлов.csv")

if __name__ == "__main__":
    main()