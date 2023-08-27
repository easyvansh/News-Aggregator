# from requests_html import HTMLSession
# # Creating a session
# session = HTMLSession()
# # Storing URl
# url = "https://news.google.com/showcase?hl=en-IN&gl=IN&ceid=IN%3Aen"

# # Storing reqeust of url
# r = session.get(url)


# # Open Chrome to access info
# r.html.render(sleep=1)

# articles = r.html.find('article')
# newslist = []
# for item in articles:
#     newsitem = item.find('a',first=True)
#     newsarticle = {

#    "link" : newsitem.absolute_links}
#     newslist.append(newsarticle)

# print(newslist[0])

# from django.shortcuts import render
import requests
# from django.shortcuts import render, redirect
from bs4 import BeautifulSoup as BSoup
# from news.models import Headline

# Create your views here.


def scrape():
    session = requests.Session()
    session.headers = {
        "User-Agent": "Googlebot/2.1 (+http://www.google.com/bot.html)"}
    url = "https://www.theonion.com/"

    content = session.get(url, verify=False).content
    soup = BSoup(content, "html.parser")
    News = soup.find_all('article')
    for article in News:
        main = article.find_all('a')[0]
        # link = main['href']
        title = main['title']
        # image_src = str(main.find('source'))
        # image_src = image_src
        print(title)


scrape()
