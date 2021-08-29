import requests
from bs4 import BeautifulSoup


def main():
    resp = requests.get('http://blog.castman.net/web-crawler-tutorial/ch1/connect.html')
    #print(resp.text)
    #input()
    soup = BeautifulSoup(resp.text, 'html.parser')
    #print(soup)
    print(soup.find('p').text)


if __name__ == '__main__':
    main()
