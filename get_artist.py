from api_key import *
import spotipy, json, sys
from spotipy.oauth2 import SpotifyClientCredentials

index = 0
songs_by_weekend = {}
weekend_image = ''

weekend_uri = 'https://open.spotify.com/artist/1Xyo4u8uXC1ZmMpatF05PJ?si=nDkuIe2zS2KGYbAVTLvHSQ&dl_branch=1'
spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id = f'{clientID}', client_secret = f'{clientSecret}'))

results = spotify.artist_top_tracks(weekend_uri)


for track in results['tracks'][:10]:
    Values = {}
    Values['link_to_song'] = results['tracks'][index]['external_urls']['spotify']
    Values['link_to_displayPhoto'] = results['tracks'][index]['album']['images'][1]['url']
    Values['preview'] = track['preview_url']

    songs_by_weekend[track['name']] = Values
    # print()
    # print('track    : ' + track['name'])
    # print()
    index += 1

def print_songs():
    for track in songs_by_weekend:
        print(track)
        print(songs_by_weekend[track]['link_to_song'])
        print(songs_by_weekend[track]['link_to_displayPhoto'])
        print(songs_by_weekend[track]['preview'])
        print()

#Get the artist's picture by his name 

if len(sys.argv) > 1:
    name = ' '.join(sys.argv[1:])
else:
    name = 'The Weekend'

results = spotify.search(q='artist:' + name, type='artist')
items = results['artists']['items']
if len(items) > 0:
    artist = items[0]
    weekend_image = artist['images'][0]['url']

all_pairs = list(songs_by_weekend.items())
print_songs()



#-----------------------------------

#print(json.dumps(results, indent = 2))