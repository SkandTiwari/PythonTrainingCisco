from datetime import datetime
import time
import pytz
from geopy.geocoders import Nominatim

timeMap = {
    "new delhi" : "Asia/Kolkata",
    "new york" : "US/Eastern",
    "san jose" : "US/Pacific",
    "bengaluru" : "Asia/Kolkata"
}



def getCoordinates(location):
    geoLocator = Nominatim(user_agent="myApp")
    Coordinates = geoLocator.geocode(query)
    return f"Longitude : {Coordinates.longitude} Latitude : {Coordinates.latitude}"


query = input("Enter a place to track its correct time : ")

timezone = timeMap.get(query.lower(), "Not Found!")

homeTime = pytz.timezone(timezone)
localTime = datetime.now(homeTime)

exact = localTime.strftime("%Y %H:%M")


print(f"Location : {query}")
print(f"Current time and year : {exact}")

print(getCoordinates(query))



