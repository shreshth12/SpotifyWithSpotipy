#Spotify Web Application - Project Milestone 1 and 2

* APIs used : Genius, SpotifyWebAPI
* Libraries used : spotipy, json, sys, re, lyricsgenius, render_template, url_for, random, flask_login, wtforms, SQLAlchemy 
*Frameworks used : Flask
*Programming languages used : Python, HTML, CSS 

[Heroku URL for milestone-1:](https://radiant-harbor-14713.herokuapp.com)

[Heroku URL for milestone-2:](https://nameless-dawn-00696.herokuapp.com/login)

# A LITTLE BIT ABOUT THE APP :- 
This is a web application built using Flask framework. It uses Spotify's Web API to fetch top 10 tracks for added artists of a particular user, their spotify song links displayed and a 30-second clip to hear the music. You can also check out the lyrics of the music, which is fetched using Genius API. You can make your own account and login to save favourite artists.This app uses wtforms to perform validation checks like :-
* Check if a user already exist in database
* Check if password is equal to confirm password
* Make HTML forms and fetch data from them

And SQLAlchemy to translate python code to communicate with sql/postgresQL databases.


# HOW YOU CAN CLONE THIS APP :-
Simply fork/clone the app and in order to run it, you need the spotify and Genius API credentials. You can get by creating your developer account on their websites. 

*Spotify -> https://developer.spotify.com/dashboard/login
*Genius -> https://genius.com/api-clients

Once you generate these credentials, create a file named .env in the same directory you cloned this app to. Paste your credentials like this :- 
*clientID = "YOUR_CLIENT_ID"
*clientSecret = "YOUR_SECRET_ID"
*GENIUS_ACCESS_TOKEN = 'YOUR_GENIUS_TOKEN'

Save your files, make sure you have all the packages and libraries installed from requirements.txt and now you can run the app from application.py

# SOME TECHNICAL ISSUES THAT I ENCOUNTERED WITH THIS APPLICATION :-
## Milestone - 1
* Some of the songs had "()" in their name, for example : Don’t Go (with Justin Bieber & Don Toliver) and when I passed this whole name into the genius API, it could not get its lyrics. My way to solve this problem was using a python library re which removes "(EVERTHING_IN_IT)" which gives just the song's name and not the version. This solved my problem and then I could fetch song's lyrics.

* I was having all of my code in a single file and everytime I get any error with the API or want to debug, I had to scroll through a lot of code and use print statments tons of time. The best way to solve this was to create a new file called functions.py and give every get request its own function name. Now, running these all functions one by one in a different file like application.py would pin point the exact function which is causing error.

* The third technical issue that I faced was that the Genius API was not returning me any data upon usage and would give an error 403, saying I do not have the permissions. After a lot of googling I found out that my API would hit "Not a Robot" section of the Genius page and that would block me from accessing it. My way around with this issue was using developer specific API calls that basically do not need high level access and through that I can finally fetch links for lyrics.

## Milestone - 2
* Validation of the forms is not easy. I wanted this application to have username and password both as validations but doing it the standard if else statement way would be very complicated and would look very cluttered. I found out a library called wtforms which does all the validations with just one like of code for each field in a HTML form.

* One of the issues with my project was to figure out how to know if a value like username or an artist is already added to the database. wtforms has a very neat way of doing this. You can make a small function inside the forms python file which does these kinds of validation checks and if any error arries, it will throw an exception and not add it to database. 

* Not sure if it counts as a technical problem but since I had all my code in single file, it was super hard to debug if any kind of issue occurs. made separete files for everything. Example - a forms.py file for wtforms, routes.py file for all the rounting, functions.py file for all the spotify functions. This made the debugging very easy.

# EXISTING PROBLEMS WITH THE PAGE :-

For some reason, the artist's picture does not display when my app is hosted on heroku. I am not able to figure out what's causing that. I tried to check if any package or library is missing or if API is not working but everything was fine. Apart from this, this project is mostly good to go with a small exception being, It looks good when viewed on a PC or MAC but when you open it on a mobile phone, it doesn't have the appropriate layout. Also when you shink the webpage, the contents gets cluttered.

# MY PLANS FOR IMPROVEMENT :-
My first plan is to use jquery to dynamically scale the webpage when it is shinked on a PC/MAC or on a phone. My second plan is to add a separate template to display lyrics, instead of redirecting users to Genius page to view them. And debug why the app is not able to fetch artist's picture when hosted on heroku. 

# WHAT DIFFERED IN THIS MILESTONE :-
To be completely honest, it went almost like I planned it to be. Something that was hard was figuring out the login and logout funtionality but it wasn't very hard because I have previously worked with flask-login before. I knew about wtforms so validation was also easy to implement. This milestone was relatively easy since I knew all the technologies beforehand. In the first milestone, working with APIs was a first hand experience and hence took time to figure out. 