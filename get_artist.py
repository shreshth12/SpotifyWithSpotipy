from api_key import *
from functions import *
import spotipy, json, sys
from spotipy.oauth2 import SpotifyClientCredentials
import json

weekend_uri = 'https://open.spotify.com/artist/1Xyo4u8uXC1ZmMpatF05PJ?si=nDkuIe2zS2KGYbAVTLvHSQ&dl_branch=1'

justin_uri = 'https://open.spotify.com/artist/1uNFoZAHBGtllmzznpCI3s?si=rJS9ztGXSTSpdrVpBL08mg&dl_branch=1'

taylor_uri = 'https://open.spotify.com/artist/06HL4z0CvFAxyc27GXpf02?si=U1pUI152TlCmbrYtz-n6tg&dl_branch=1'

def check_artist_url(url):
    try:
        get_artist_data(url)
        return True
    except:
        return False

# print(get_artist_name(weekend_uri))

# songs_by_weekend = get_artist_data(weekend_uri)
# weekend_image = get_artist_picture('The Weekend')

# songs_by_Justin = get_artist_data(justin_uri)
# justin_image = get_artist_picture('Justin Bieber')

# songs_by_Taylor = get_artist_data(taylor_uri)
# taylor_image = get_artist_picture('Taylor Swift')

# Justin = [songs_by_Justin, justin_image]
# Weekend = [songs_by_weekend, weekend_image]
# Taylor = [songs_by_Taylor, taylor_image]

# artists = [Justin, Weekend, Taylor]

# print_songs_data(songs_by_Justin)
#-----------------------------------

#print(json.dumps(results, indent = 2))