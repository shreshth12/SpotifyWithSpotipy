from api_key import *
from functions import *
import spotipy, json, sys
from spotipy.oauth2 import SpotifyClientCredentials

weekend_uri = 'https://open.spotify.com/artist/1Xyo4u8uXC1ZmMpatF05PJ?si=nDkuIe2zS2KGYbAVTLvHSQ&dl_branch=1'

justin_uri = 'https://open.spotify.com/artist/1uNFoZAHBGtllmzznpCI3s?si=rJS9ztGXSTSpdrVpBL08mg&dl_branch=1'

songs_by_weekend = get_artist_data(weekend_uri)
print_songs_data(songs_by_weekend)
#-----------------------------------

#print(json.dumps(results, indent = 2))