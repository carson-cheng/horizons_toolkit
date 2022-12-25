import requests
import math
import matplotlib.pyplot as plt
import time
#orbital period in years
min = 5.999
#years to days
year = 365.24
#
x = []
y = []
def display_results(x, y):
    writefile = open("results_6auplus.txt", "w")
    writefile.write(str(x) + "\n" + str(y))
    plt.plot(x, y)
    plt.title("Distribution of the orbital periods of asteroids")
    plt.xlabel("Orbital period (years)")
    plt.ylabel("Number of asteroids")
    plt.savefig("asteroid_orbital_periods_6auplus.png")
    plt.show()
try:
    for item in range(3500):
        minimum, maximum = min * year, (min + 0.002) * year
        url = 'https://ssd-api.jpl.nasa.gov/sbdb_query.api?sb-cdata={"AND":["per|RG|' + str(minimum) + '|' + str(maximum) + '"]}'
        #print(url)
        data = requests.get(url).text
        #print(data)
        try:
            count = data.split('"count":')[1].split("}")[0]
            count = int(count)
            print(str(min) + " to " + str(round(min + 0.002, 3)) + ": " + str(count))
            x.append(min)
            y.append(count)
            min = round(min + 0.002, 3)
        except IndexError:
            print("Server error, retrying in 15 seconds...")
            time.sleep(15)

    display_results(x, y)
except KeyboardInterrupt:
    display_results(x, y)
