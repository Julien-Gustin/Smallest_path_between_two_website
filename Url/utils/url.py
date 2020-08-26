from bs4 import BeautifulSoup, SoupStrainer
import requests
""" get_urls
    @bref: get all url from a website

    @param url: url of the website
    @return urls: a list of all the url from the website
"""
def get_urls(url):
    urls = []
    url_splited = url.split("/")
    previous_url = "/".join(url_splited[0:len(url_splited)-2])
    home_url = "/".join(url_splited[0:3])
    try:
        page = requests.get(url)
        data = page.text
        soup = BeautifulSoup(data, features="lxml")

        for link in soup.find_all('a'):
            new_url = str(link.get('href'))
            new_url = new_url.replace('..', previous_url)
            if len(new_url) > 0 and new_url[0] == "/":
                new_url = home_url + new_url

            if "www." in new_url and new_url[len(new_url)-4:] != ".pdf":
                urls.append(new_url)

    except UnicodeDecodeError:
        print("erreur de decodage")
    except:
        print("erreur")

    return urls
