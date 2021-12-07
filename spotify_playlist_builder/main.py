from bs4 import BeautifulSoup
import lxml
import requests
import spotipy
from spotipy import SpotifyOAuth

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

URL = f"https://www.billboard.com/charts/hot-100/{date}/"
response = requests.get(URL)

webpage = response.text
soup = BeautifulSoup(webpage, "html.parser")

CLIENT_ID = ""
CLIENT_SECRET = ""

songs_list = []
# titles = soup.find(name="h3", id="title-of-a-story")
titles = soup.select("li > ul > li > h3[id=title-of-a-story]")
for title in titles:
    print(title.get_text())
    songs_list.append(title.get_text().strip("\n"))

print(songs_list)

spotify = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://localhost:4040",
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt"
    )
)

user_id = spotify.current_user()["id"]

song_uris = []
for song in songs_list:
    result = spotify.search(q=f"track:{song}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"The {song} is not found in Spotify. Skipping...")
year = date.split("-")[0]
playlist = spotify.user_playlist_create(user=user_id, name=f"{year} Billboard 100", public=False)
print(playlist)
spotify.playlist_add_items(playlist_id=playlist["id"], items=song_uris)