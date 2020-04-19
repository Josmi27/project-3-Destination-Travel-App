import requests
import random
import json
import models

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

#genius music api
def music_from_jamaica():
    genius_search_jamaica = "https://api.genius.com/search?q=Sean%20Paul"
    my_headers = {"Authorization": "Bearer lEohxFMUgWxUa1e0TdNhdA79QSdKgPdW8qZ9RHGzbHThB-sDc8H-yEgsV9NkPPRi"}
    playlist = random.randint(0,8)
    response = requests.get(genius_search_jamaica, headers=my_headers)
    json_body = response.json()
    song = json_body["response"]["hits"][playlist]["result"]["full_title"]
    Jamaica_song_selection = ("Here you can find a song from/featuring a local Jamaican artist. Song:  " + song)
    return(Jamaica_song_selection)

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
    
#My Memory API - text translator 
def translate():
    api_url = "https://api.mymemory.translated.net/get?q=Hello! Welcome to Destination Travel!&langpair=en|es"
    response = requests.get(api_url)
    json_body = response.json()
    original_translation = json_body["responseData"]["translatedText"]
    api_url2 = "https://api.mymemory.translated.net/get?q=¡Hola! Bienvenido a Destination Travel!&langpair=es|en"
    response2 = requests.get(api_url2)
    json_body2 = response2.json()
    reverse_translation = json_body2["responseData"]["translatedText"]
    translated_sentence = (reverse_translation + " translated into Spanish is: "+ original_translation)
    return(translated_sentence)

#Airport API
def jamaica_airport(): 
    url = "https://cometari-airportsfinder-v1.p.rapidapi.com/api/airports/by-text"

    querystring = {"text":"Kingston"}

    headers = {
        'x-rapidapi-host': "cometari-airportsfinder-v1.p.rapidapi.com",
        'x-rapidapi-key': "e9030cc69cmsh46998fa37a68441p18e133jsne5b9847bff25"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    json_body = response.json()
    jamaica_airport = json.dumps(json_body[0]["code"])
    airport = ("The airport located in Kingston, Jamaica can be found under airport code " + jamaica_airport)
    return(airport)

def pr_airport():
    url = "https://cometari-airportsfinder-v1.p.rapidapi.com/api/airports/by-text"

    querystring = {"text":"Ponce"}

    headers = {
        'x-rapidapi-host': "cometari-airportsfinder-v1.p.rapidapi.com",
        'x-rapidapi-key': "e9030cc69cmsh46998fa37a68441p18e133jsne5b9847bff25"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    json_body = response.json()
    p_airport = json.dumps(json_body[0]["code"])
    airport = ("The airport located in San Juan, Puerto Rico can be found under airport code "+ p_airport)
    
    new_message = models.Currency(p_airport)
    models.db.session.add(new_message) 
    models.db.session.commit()
    
    return(airport)


#JAMAICA CURRENCY CONVERSION

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

def outdoor_activity():
    url = "https://trailapi-trailapi.p.rapidapi.com/"
    headers = {'x-rapidapi-host': "trailapi-trailapi.p.rapidapi.com",'x-rapidapi-key': "2bc8488dedmsh09812c800fb6b89p19fb19jsn6987dc57cdda"}
    querystring = {"location_id":"1","limit":"30","sort":"relevance","offset":"0","lang":"en_US","currency":"USD","units":"km","query":"pattaya"}
    response = requests.request("GET", url, headers=headers, params=querystring)
    json_body = response.json()
    activity = json_body["places"][3]["name"]
    outdoor_response = "In Puerto Rico, you should check out the activity called: " + activity
    return(outdoor_response)

def travel_advice():
    url = "https://www.reisewarnung.net/api?country=PR"
    Response = requests.get(url)
    json_body = Response.json()
    country_code = json_body["data"]["code"]["country"]
    danger_rating = json_body["data"]["situation"]["rating"]
    advice = json_body["data"]["lang"]["en"]["advice"]
    if country_code:
        response = "For country code {}, since the travel danger rating is {}/5.0, {}".format(country_code, danger_rating, advice)
    else:
        response = "No data found for specified country code. Please try country code PR."
    return(response)