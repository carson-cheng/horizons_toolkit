import requests
from plot_ephemeris import *
objects = small_body_query([("sb-kind", "=", "a"), ("q", "<", "0.5")], ["pdes"])
max_dist = 0.005    #au
body = "Merc"
#print(objects)
for item in objects:
    command = item[0]
    url = "https://ssd-api.jpl.nasa.gov/cad.api?des=" + str(command) + "&date-min=1700-01-01&date-max=2200-01-01&dist-max=" + str(max_dist) + "&body=" + body
    #print(url)
    approaches = requests.get(url).text
    count = approaches.split('count":"')[1].split('"')[0]
    if int(count) > 0:
        print("\u001b[32;1m\u001b[1m" + command + "\u001b[0m" + " will approach " + body)
    else:
        print(command)
