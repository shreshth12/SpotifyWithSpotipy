from api_key import *
import spotipy, json, sys
from spotipy.oauth2 import SpotifyClientCredentials


spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id = f'{clientID}', client_secret = f'{clientSecret}'))

weekend_image = ''
Justin_image = ''
#Get the artist's picture by his name 
#This is to get weekend's picture
if len(sys.argv) > 1:
    name = ' '.join(sys.argv[1:])
else:
    name = 'The Weekend'

results = spotify.search(q='artist:' + name, type='artist')
items = results['artists']['items']
if len(items) > 0:
    artist = items[0]
    weekend_image = artist['images'][0]['url']

#This is to get Justin's picture
if len(sys.argv) > 1:
    name = ' '.join(sys.argv[1:])
else:
    name = 'Justin Bieber'

results = spotify.search(q='artist:' + name, type='artist')
items = results['artists']['items']
if len(items) > 0:
    artist = items[0]
    Justin_image = artist['images'][0]['url']

print(f'Justin: {Justin_image}')
print(f'Weekend: {weekend_image}')