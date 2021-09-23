Spotify Web Application - Project Milestone 1

APIs used : Genius, SpotifyWebAPI
Libraries used : spotipy, json, sys, re, lyricsgenius, render_template, url_for, random
Frameworks used : Flask
Programming languages used : Python, HTML, CSS 

Heroku URL : 

# A LITTLE BIT ABOUT THE APP :- 
This is a web application built using Flask framework. It uses Spotify's Web API to fetch top tracks for 3 different artists and their spotify links displayed and a 30-second clip to hear the music. You can also check out the lyrics of the music, which is fetched using Genius API. 

# HOW YOU CAN CLONE THIS APP :-
Simply fork/clone the app and in order to run it, you need the spotify and Genius API credentials. You can get by creating your developer account on their websites. 

Spotify -> https://developer.spotify.com/dashboard/login
Genius -> https://genius.com/api-clients

Once you generate these credentials, create a file named "api_key.py" in the same directory you cloned this app to. Paste your credentials like this :- 
clientID = "YOUR_CLIENT_ID"
clientSecret = "YOUR_SECRET_ID"
GENIUS_ACCESS_TOKEN = 'YOUR_GENIUS_TOKEN'

Save your files and now you can run the app from application.py

# THREE TECHNICAL ISSUES THAT I ENCOUNTERED WITH THIS APPLICATION :-
--> Some of the songs had "()" in their name, for example : Don’t Go (with Justin Bieber & Don Toliver) and when I passed this whole name into the genius API, it could not get its lyrics. My way to solve this problem was using a python library re which removes "(EVERTHING_IN_IT)" which gives just the song's name and not the version. This solved my problem and then I could fetch song's lyrics.

--> I was having all of my code in a single file and everytime I get any error with the API or want to debug, I had to scroll through a lot of code and use print statments tons of time. The best way to solve this was to create a new file called functions.py and give every get request its own function name. Now, running these all functions one by one in a different file like application.py would pin point the exact function which is causing error.

--> The third technical issue that I faced was that the Genius API was not returning me any data upon usage and would give an error 403, saying I do not have the permissions. After a lot of googling I found out that my API would hit "Not a Robot" section of the Genius page and that would block me from accessing it. My way around with this issue was using developer specific API calls that basically do not need high level access and through that I can finally fetch links for lyrics.

# EXISTING PROBLEMS WITH THE PAGE :-
There are no real problems that currently exist with the page apart from how html and css is laid out. It looks good when viewed on a PC or MAC but when you open it on a mobile phone, it doesn't have the appropriate layout. Also when you shink the webpage, the contents gets cluttered.

# MY PLANS FOR IMPROVEMENT :-
My first plan is to use jquery to dynamically scale the webpage when it is shinked on a PC/MAC or on a phone. My second plan is to add a separate template to display lyrics, instead of redirecting users to Genius page to view them. 

