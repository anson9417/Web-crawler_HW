import requests
from bs4 import BeautifulSoup

def main():
    url = 'http://blog.castman.net/web-crawler-tutorial/ch1/connect.html'
    h1 = get_head_text(url, 'button')
    print(h1)
    print('')
    h2 = get_head_text(url, 'title')
    print(h2)
    print('')
    h3 = get_head_text(url, 'p')
    print(h3)

def get_head_text(url, head_tag):
    try:
        resp = requests.get(url)
        if resp.status_code == 200:
            soup = BeautifulSoup(resp.text, 'html.parser')
            return soup.find(head_tag).text
    except Exception as e:
        return None


if __name__ == '__main__':
    main()
    print('Finish!')