from api_key import *
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

songs_by_weekend = {}
filtered_songs = []

weekend_uri = 'https://open.spotify.com/artist/1Xyo4u8uXC1ZmMpatF05PJ?si=nDkuIe2zS2KGYbAVTLvHSQ&dl_branch=1'
spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id = f'{clientID}', client_secret = f'{clientSecret}'))

results = spotify.artist_albums(weekend_uri, album_type='album')
albums = results['items']
while results['next']:
    results = spotify.next(results)
    albums.extend(results['items'])

for album in albums:
    if(album['name'] in songs_by_weekend):
        continue
    else:
        songs_by_weekend[album['name']] = 1
        filtered_songs.append(album['name'])
    
for song in filtered_songs:
    print(song)