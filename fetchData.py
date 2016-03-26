# config Library
import config

#urlParser libraries
import urllib2
#from lxml import html

# weatherAPI Library
import pywapi

#webPage parsing
from bs4 import BeautifulSoup


def dataFetcher(type,data):
    "This function acts as a switch case for switching between type of data to be fetched"
    rData = "No Data"
    if type == '0':
        rData = fetchWeather(data)
    elif type == '1':
        rData = fetchNews()
    return rData

def fetchWeather(data):
    "This function fetches weather details for the client requested location"
    city = str(data)
    lookup = pywapi.get_location_ids(city)
    #workaround to access last item of dictionary
    #print lookup
    for i in lookup:
        location_id = i
    #location_id now contains the city's code
    try:
        weatherResult = pywapi.get_weather_from_weather_com(location_id , units = 'metric')
        returnedData = weatherResult["current_conditions"]["temperature"] + u"\u00B0" + "C$" + "It is " + weatherResult["current_conditions"]["text"] + "$" + weatherResult["current_conditions"]["humidity"] + "%" + "$\nForecasts "
        for days in weatherResult["forecasts"]:
            returnedData = returnedData + days["day_of_week"] + "^" + days["high"] +  u"\u00B0" +"C^" + days["low"] +  u"\u00B0" + "C$"

        return returnedData
    except UnboundLocalError:
        print "City does not exist"
        return "0"
    except KeyError:
        print "Key Error Exception caught"
        return "0"
        # + str(UnboundLocalError) + "\n"




def fetchNews():
    "This function fetches top 3 news stories"
    response = urllib2.urlopen(config.newsLink)
    htmlPage = response.read()

    soup = BeautifulSoup(htmlPage,"html.parser")
    topStories = (soup.find(class_="section-content")).find_all_next(class_="blended-wrapper",limit = 3)
    for data in topStories:
        print "HEADLINE\n" + data.find(class_ = "titletext").text
        returnedData = str(data.find(class_ = "titletext").text)
        print "STORY\n" + data.find(class_ = "esc-lead-snippet-wrapper").text + "\n"
        returnedData = returnedData + str(data.find(class_ = "esc-lead-snippet-wrapper").text) + "$"
    return returnedData


#city = raw_input("Enter the name of the city\n") #for weather
#print dataFetcher('0',city)
