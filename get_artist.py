from api_key import *
import spotipy, json, sys
from spotipy.oauth2 import SpotifyClientCredentials

index = 0
songs_by_weekend = {}
songs_by_Justin = {}


weekend_uri = 'https://open.spotify.com/artist/1Xyo4u8uXC1ZmMpatF05PJ?si=nDkuIe2zS2KGYbAVTLvHSQ&dl_branch=1'

justin_uri = 'https://open.spotify.com/artist/1uNFoZAHBGtllmzznpCI3s?si=rJS9ztGXSTSpdrVpBL08mg&dl_branch=1'

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id = f'{clientID}', client_secret = f'{clientSecret}'))

results = spotify.artist_top_tracks(weekend_uri)

results_justin = spotify.artist_top_tracks(justin_uri)

#This is the part where I fetch weekend's songs 
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

#This is the part where I fetch justin's songs 
index = 0

for track in results_justin['tracks'][:10]:
    Values = {}
    Values['link_to_song'] = results_justin['tracks'][index]['external_urls']['spotify']
    Values['link_to_displayPhoto'] = results_justin['tracks'][index]['album']['images'][1]['url']
    Values['preview'] = track['preview_url']

    songs_by_Justin[track['name']] = Values
    # print()
    # print('track    : ' + track['name'])
    # print()
    index += 1

def print_songs(artist_name):
    for track in artist_name:
        print(track)
        linkToSong = artist_name[track]['link_to_song']
        DP = artist_name[track]['link_to_displayPhoto']
        TrackPreview = artist_name[track]['preview']
        print(f'LinkToSong: {linkToSong}')
        print(f'DP: {DP}')
        print(f'TrackPreview: {TrackPreview}')
        print()


# print_songs(songs_by_weekend)


#-----------------------------------

#print(json.dumps(results, indent = 2))