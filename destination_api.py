import requests
import random
import json
import models
import config

#WEATHERBIT API
def current_temperature():
    response = requests.post('https://api.weatherbit.io/v2.0/current?city=Baltimore,MD&units=I&key=dfa4efd664ce43b4a69c1da82f70e9b8')
    json_body = response.json()
    temperature = (json_body["data"][0]["temp"])
    state = (json_body["data"][0]["state_code"])
    city = (json_body["data"][0]["city_name"])
    local_weather_temp = ("The temperature in your current location of  " + city + ", " + state + " is " + str(temperature) + " degrees Fahrenheit.")
    return(local_weather_temp)

def current_timezone():
    response = requests.post('https://api.weatherbit.io/v2.0/current?city=Baltimore,MD&units=I&key=dfa4efd664ce43b4a69c1da82f70e9b8')
    json_body = response.json()
    timezone = (json_body["data"][0]["timezone"])
    city = (json_body["data"][0]["city_name"])
    local_timezone = ("Your current city of " + city + " is in the " + timezone + " timezone.")
    return(local_timezone)

# #genius music api
def music_from_jamaica():
    genius_search_jamaica = "https://api.genius.com/search?q=Sean%20Paul"
    my_headers = {"Authorization": "Bearer lEohxFMUgWxUa1e0TdNhdA79QSdKgPdW8qZ9RHGzbHThB-sDc8H-yEgsV9NkPPRi"}
    playlist = random.randint(0,8)
    response = requests.get(genius_search_jamaica, headers=my_headers)
    json_body = response.json()
    song = json_body["response"]["hits"][playlist]["result"]["full_title"]
    Jamaica_song_selection = ("Here you can find a song from/featuring a local Jamaican artist. Song:  " + song)
    return(Jamaica_song_selection)

def twilio_texts():

    from twilio.rest import Client

    account = config.api_account
    token = config.api_token
    client = Client(account, token)
    message = client.messages.create(to="+13017528277", from_="+14792551230",body="It's Destination Travel App saying HELLO!")

def music_from_pr():
    genius_search_pr = "https://api.genius.com/search?q=Bad%20Bunny"
    my_headers = {"Authorization": "Bearer lEohxFMUgWxUa1e0TdNhdA79QSdKgPdW8qZ9RHGzbHThB-sDc8H-yEgsV9NkPPRi"}
    playlist = random.randint(0,8)
    response = requests.get(genius_search_pr, headers=my_headers)
    json_body = response.json()
    song = json_body["response"]["hits"][playlist]["result"]["full_title"]
    pr_song_selection = ("Here you can find a song from/featuring a local Puerto Rican artist. Song:  " + song)
    new_message = models.Genius(song)
    models.db.session.add(new_message) 
    models.db.session.commit()
    return(pr_song_selection)
    
# #My Memory API - text translator 
def translate():
    api_url = "https://api.mymemory.translated.net/get?q=Hello! Welcome to Destination Travel!&langpair=en|es"
    response = requests.get(api_url)
    json_body = response.json()
    original_translation = json_body["responseData"]["translatedText"]
    api_url2 = "https://api.mymemory.translated.net/get?q=¡Hola! Bienvenido a Destination Travel!&langpair=es|en"
    response2 = requests.get(api_url2)
    json_body2 = response2.json()
    reverse_translation = json_body2["responseData"]["translatedText"]
    translated_sentence = ('"' + reverse_translation +'"' + " translated into Spanish is: "+ original_translation)
    print(translated_sentence)
    
#Airport API
def airport(city): 
    url = "https://cometari-airportsfinder-v1.p.rapidapi.com/api/airports/by-text"

    querystring = {"text":str(city)}

    headers = {
        'x-rapidapi-host': "cometari-airportsfinder-v1.p.rapidapi.com",
        'x-rapidapi-key': "e9030cc69cmsh46998fa37a68441p18e133jsne5b9847bff25"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    json_body = response.json()
    airport_code = json.dumps(json_body[0]["code"])
    airport = "The airport located in {} can be found under airport code {} ".format(str(city),airport_code )
    
    new_message = models.Currency(airport)
    models.db.session.add(new_message) 
    models.db.session.commit()
    return(airport)



# #JAMAICA CURRENCY CONVERSION

def currency_conversion():
    currency_url = "https://currency-converter5.p.rapidapi.com/currency/convert"
    querystring = {"format":"json","from":"USD","to":"JMD","amount":"1"}
    headers = {
        'x-rapidapi-host': "currency-converter5.p.rapidapi.com",
        'x-rapidapi-key': "8258d9474bmshc76a1b383e354d4p11989bjsn988778d9991f"
        }
    response = requests.request("GET", currency_url, headers=headers, params=querystring)
    json_body = response.json()
    conversion = json.dumps(json_body["rates"]["JMD"]["rate"], indent=2)
    jamaica_conversion = ("The currency conversion from the US dollar to the Jamaican Dollar is: $"+ conversion)
    return(jamaica_conversion)


def outdoor_activity(country_name):
    url = "https://trailapi-trailapi.p.rapidapi.com/"
    headers = {'x-rapidapi-host': "trailapi-trailapi.p.rapidapi.com",'x-rapidapi-key': "2bc8488dedmsh09812c800fb6b89p19fb19jsn6987dc57cdda"}
    querystring = {"q-activities_activity_type_name_eq":"hiking","radius":"100000","q-country_cont":"Egypt","limit":"25"}
    resp = requests.request("GET", url, headers=headers, params=querystring)
    json_body = resp.json()
   
    au = json_body["places"][0]["country"]
    au_activity = json_body["places"][0]["activities"][0]["activity_type_name"]
    us = json_body["places"][1]["country"]
    us_activity = json_body["places"][1]["activities"][0]["activity_type_name"]
    ca = json_body["places"][18]["country"]
    ca_activity = json_body["places"][18]["name"]
    
    if country_name == au:
        outdoor_response = "In {}, you should check out the activity- {}".format(country_name, au_activity)
        new_message = models.Activity(au_activity)
        models.db.session.add(new_message) 
        models.db.session.commit()
    elif country_name == ca:
        outdoor_response = "In {}, you should walk in a place called- {}".format(country_name, ca_activity)
        new_message = models.Activity(ca_activity)
        models.db.session.add(new_message) 
        models.db.session.commit()
    elif country_name == us:
        outdoor_response = "In the {}, you should check out the activity- {}".format(country_name, us_activity)
        new_message = models.Activity(us_activity)
        models.db.session.add(new_message) 
        models.db.session.commit()
    else:
        outdoor_response = "Invalid country input! Please try 'Australia', 'Canada', or 'United States'." 

    return(outdoor_response)

def travel_advice(country_code):
    url = "https://www.reisewarnung.net/api"
    Response = requests.get(url)
    json_body = Response.json()
    country_name = json_body["data"][str(country_code)]["lang"]["de"]["country"]
    danger_rating = json_body["data"][str(country_code)]["situation"]["rating"]
    advice = json_body["data"][str(country_code)]["lang"]["en"]["advice"]
    if country_name:
        response = "For {}, since the travel danger rating is {}/5.0, {}".format(country_name, danger_rating, advice)
    else:
        response = "The country code that you entered is invalid. Please try again!"
    
    return(response)