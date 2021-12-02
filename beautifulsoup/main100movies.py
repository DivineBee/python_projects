from bs4 import BeautifulSoup
import lxml
import requests

URL = "https://www.imdb.com/list/ls055592025/"
response = requests.get(URL)

movie_page = response.text
soup = BeautifulSoup(movie_page, "html.parser")

movies = soup.find_all(name="h3", class_="lister-item-header")

movie_list = []
with open('movies.txt', 'a') as f:
    for movie in movies:
        title = movie.getText()
        f.write(' '.join(title.splitlines())+'\n')
