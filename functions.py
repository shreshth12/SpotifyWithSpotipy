from lyricsgenius.api.public_methods import artist
from api_key import *
import spotipy, json, sys
from spotipy.oauth2 import SpotifyClientCredentials
import lyricsgenius
from lyricsgenius import Genius

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id = f'{clientID}', client_secret = f'{clientSecret}'))


genius = Genius(GENIUS_ACCESS_TOKEN)
songs = genius.search_songs("You Need To Calm Down",per_page=1)
x = json.dumps(songs, indent = 2)
print(songs['hits'][0]['result']['url'])


#Use this function to get an artist's picture
def get_artist_picture(Aname):
    if len(sys.argv) > 1:
        name = ' '.join(sys.argv[1:])
    else:
        name = Aname

    results = spotify.search(q='artist:' + name, type='artist')
    items = results['artists']['items']
    if len(items) > 0:
        artist = items[0]
        return artist['images'][0]['url']

#Use this function to get artist's top ten songs, cover pictures, song url, preview url.
def get_artist_data(artist_uri):
    index = 0
    artist_results = {}
    results = spotify.artist_top_tracks(artist_uri)
    
    for track in results['tracks'][:10]:
        Values = {}
        Values['link_to_song'] = results['tracks'][index]['external_urls']['spotify']
        Values['link_to_displayPhoto'] = results['tracks'][index]['album']['images'][1]['url']
        Values['preview'] = track['preview_url'] 
        artist_results[track['name']] = Values
        index += 1
    
    return artist_results

#This function is to prints all the necessary data for an artist. Input the result from get_artist_data here.
def print_songs_data(artist_data):
    for track in artist_data:
        print(track)
        linkToSong = artist_data[track]['link_to_song']
        DP = artist_data[track]['link_to_displayPhoto']
        TrackPreview = artist_data[track]['preview']
        print(f'LinkToSong: {linkToSong}')
        print(f'DP: {DP}')
        print(f'TrackPreview: {TrackPreview}')
        print()

# print(get_artist_DP('Justin Bieber'))
# print_songs_data(get_artist_data(justin_uri))

