from bs4 import BeautifulSoup
import lxml
import requests

response = requests.get("https://news.ycombinator.com")
# print(response.text)

yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")

articles = soup.find_all(name="a", class_="titlelink")
articles_text = []
articles_links =[]

for article in articles:
    text = article.getText()
    link = article.get("href")
    articles_text.append(text)
    articles_links.append(link)

article_upvote = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

largest_number = max(article_upvote)
largest_index = article_upvote.index(largest_number)
print(articles_text[largest_index])
print(articles_links[largest_index])

sorted(article_upvote)

print(articles_text)
print(articles_links)
print(article_upvote)




















# with open("website.html") as file:
#     contents = file.read()
#
#
# soup = BeautifulSoup(contents, 'lxml')
# anchor_tags=soup.find_all(name="a")
#
# for tag in anchor_tags:
#     print(tag.getText())
#     print(tag.get("href"))
#
# heading = soup.find(name="h1", id="name")
# section_heading = soup.find(name="h1", class_re="heading")
#
# company_url = soup.select_one(selector="#name")
# print(company_url)
