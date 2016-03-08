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
    if type == 0:
        fetchWeather(data)
    elif type == 1:
        fetchNews(data)
    elif type == 2:
        fetchStock(data) 
    
def fetchWeather(data):
    "This function fetches weather details for the client requested location"
    city = data[0]
    lookup = pywapi.get_location_ids(city)
 
    #workaround to access last item of dictionary
    for i in lookup:
        location_id = i
    #location_id now contains the city's code
    weatherResult = pywapi.get_weather_from_weather_com(location_id , units = 'metric')
    print "Current Temperature in " + weatherResult["location"]["name"] + " is " + weatherResult["current_conditions"]["temperature"] + u"\u00B0" + "C"
    print "It is " + weatherResult["current_conditions"]["text"]
    print "Humidity is " + weatherResult["current_conditions"]["humidity"] + "%"
    print "\nForecasts "
    for days in weatherResult["forecasts"]:
        print days["day_of_week"] + " High " + days["high"] +  u"\u00B0" +"C  Low " + days["low"] +  u"\u00B0" + "C"
    
    

def fetchNews(data):
    "This function fetches top news stories"
    response = urllib2.urlopen(config.newsLink)
    htmlPage = response.read()

    soup = BeautifulSoup(htmlPage,"html.parser")
    topStories = soup.find(class_ = "section-content")
    #print topStories
    # First Story
    story = topStories.find(class_="blended-wrapper blended-wrapper-first esc-wrapper")
    print "Headline " + topStories.find(class_= "titletext").text
    print "Story " + story.find(class_ = "esc-lead-snippet-wrapper").text
    print "\n\n"
    
    story = topStories.find(class_ = "blended-wrapper esc-wrapper")
    print story
    while(story):
       print "Headline " + story.find(class_= "titletext").text
       print "Story " + story.find(class_ = "esc-lead-snippet-wrapper").text
       print "\n\n"
       story = topStories.find_next(class_="blended-wrapper esc-wrapper")
    
   
        
        
    
    
def fetchStock(data):
    print "Stock"    

data = ["New Delhi"]
dataFetcher(1,data)

  