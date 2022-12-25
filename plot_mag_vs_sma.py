import requests
import math
import matplotlib.pyplot as plt
import time
#semi-major axis in au
min = 0.5
#years to days
year = 365.24
#
x = []
y = []
def sma_to_period(sma, year=365.24):
    #Returns orbital period (days) from the semi-major axis (au)
    return year * (sma ** 1.5)
def display_results(x, y):
    writefile = open("mag_vs_sma.txt", "w")
    writefile.write(str(x) + "\n" + str(y))
    plt.plot(x, y)
    plt.title("Distribution of the absolute magnitude (H) of asteroids vs semi-major axes")
    plt.xlabel("Semi-major axis (au)")
    plt.ylabel("Average absolute magnitude of asteroids (H)")
    plt.savefig("asteroid_orbital_periods_6auplus.png")
    plt.show()
try:
    for item in range(1000):
        url = 'https://ssd-api.jpl.nasa.gov/sbdb_query.api?sb-cdata={"AND":["per|RG|' + str(sma_to_period(min)) + '|' + str(sma_to_period(min+0.01)) + '"]}&fields=H'
        #print(url)
        data = requests.get(url).text
        #print(data)
        try:
            maglist_data = data.split('"data":[')[1].split('],"count')[0]
            maglist_data = maglist_data.split(']],[[')
            maglist = []
            for item in maglist_data:
                if item != "null" and bool(item) == True:
                    maglist.append(float(item[1:-1]))
            if len(maglist) != 0:
                count = sum(maglist) / len(maglist)
                print(str(min) + " to " + str(round(min + 0.01, 2)) + ": " + str(count))
                x.append(min)
                y.append(count)
                min = round(min + 0.01, 2)
        except IndexError:
            print("Server error, retrying in 15 seconds...")
            time.sleep(15)

    display_results(x, y)
except KeyboardInterrupt:
    display_results(x, y)
