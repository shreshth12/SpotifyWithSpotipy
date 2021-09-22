from api_key import *
import spotipy, json
from spotipy.oauth2 import SpotifyClientCredentials

songs_by_weekend = {}
filtered_songs = []

weekend_uri = 'https://open.spotify.com/artist/1Xyo4u8uXC1ZmMpatF05PJ?si=nDkuIe2zS2KGYbAVTLvHSQ&dl_branch=1'
spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id = f'{clientID}', client_secret = f'{clientSecret}'))

results = spotify.artist_top_tracks(weekend_uri)

for track in results['tracks'][:10]:
    print()
    print('track    : ' + track['name'])
    print()


print(json.dumps(results, indent = 2))