import requests
from bs4 import BeautifulSoup

def main():
    url = "http://nplus1.ru/"
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")
    urls = [x.get('href') for x in soup.find_all("a") if (x.get('href').startswith("/news/")) or 
    (x.get('href').startswith("/blog/"))]
    urls_1 = soup.find_all('div', {"class": "lead"})

    for u in urls_1:
        print(u.text)
   
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