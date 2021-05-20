'''
pyWeather.py Created by Richa D Created date: 05:20:21
'''

import requests
import re
import bs4

while True:
    print("What is your Zipcode?")
    zipCode = input()
    zipCodeRegex = re.compile(r'^\d{5}$')
    mo = zipCodeRegex.search(zipCode)

    if mo == None:
        print("Hmm... I don't recognize " + zipCode + " as a proper Zipcode. Use digit like 90210.")
        continue
    break

res = requests.get("https://weather.com/weather/today/l/" + zipCode)
weatherSoup = bs4.BeautifulSoup(res.text, features="html.parser")
mydivs = weatherSoup.findAll("div", {"class": "CurrentConditions--primary--3xWnK"})
weather = mydivs[0].getText()

locationdivs = weatherSoup.findAll("h1", {"class": "CurrentConditions--location--1Ayv3"})
mylocation = locationdivs[0].getText()


print("The "+ mylocation +" is "+ weather +'.')