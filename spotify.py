import requests 
from secrets import *
import base64, json

authUrl = "https://accounts.spotify.com/api/token"

authHeader = {}

authData = {}

def getAccessToken(clientID, clientSecret):

    message = f"{clientID}:{clientSecret}"
    message_bytes = message.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('ascii')

    # print(base64_message)

    authHeader['Authorization'] = "Basic " + base64_message  
    authData['grant_type'] = "client_credentials"
    res = requests.post(authUrl, headers = authHeader, data = authData)

    # print(res)

    responseObject = res.json()
    # print(json.dumps(responseObject, indent = 2))

    accessToken = responseObject['access_token'] 

    return accessToken


def getlatest(token):

    latestID = "https://api.spotify.com/v1/browse/new-releases"

    getHeader = {
        "Authorization" : "Bearer " + token
    }

    res = requests.get(latestID, headers = getHeader)

    latestObject = res.json()

    return latestObject

token = getAccessToken(clientID, clientSecret)
sol = getlatest(token)

for i in range(0,10):
    print(sol['albums']['items'][i]['name'])

# print(sol['albums']['items'][10]['release_date'])
# print(json.dumps(sol, indent = 4))