from bs4 import BeautifulSoup
import requests

URL = "https://www.empireonline.com/movies/features/best-movies-2/"
response = requests.get(URL)
response.raise_for_status()
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")
movie_titles = soup.find_all(name="h3", class_="listicleItem_listicle-item__title__hW_Kn")

movie_titles_list = [title_name.getText() for title_name in movie_titles]
movie_titles_list.reverse()
print(movie_titles_list)

with open("movie.txt", "w") as file:
    for movie_title in movie_titles_list:
        result = file.write(movie_title + "\n")
