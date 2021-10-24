import phonenumbers

import folium

from myNumber import number

from phonenumbers import geocoder

Key = "581f68f7f36b4592813a22d551f80aa3"

personNumber = phonenumbers.parse(number)

yourLocation = geocoder.description_for_number(personNumber, "en")
print(yourLocation)

## finding the service provider

from phonenumbers import carrier

service_provider = phonenumbers.parse(number)
print(carrier.name_for_number(service_provider, "en"))

from opencage.geocoder import OpenCageGeocode

geocoder = OpenCageGeocode(Key)

query = str(yourLocation)

results = geocoder.geocode(query)
##print(results)

lat = results[0]['geometry']['lat']

lng = results[0]['geometry']['lat']

print(lat,lng)

myMap = folium.Map(location=[lat, lng], zoom_start = 5)

folium.Marker([lat, lng],popup=yourLocation).add_to((myMap))

#Map will be saved in a HTML file

myMap.save("myLocation.html")