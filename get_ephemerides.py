#A program that requests 1985 to 2034 ephemerides of minor planets, planets, and moons, and stores them in a directory called "ephemerides"
#Filename_format: object_id + _ephemerides.txt
#The command variable is the object id
import requests
from plot_ephemeris import *
start_date = "2023-Jan-01"
stop_date = "2045-Dec-31"
def return_filename(command):
    return "ephemerides/" + str(command) + "_ephemeris.txt"
def check_existing_ephemeris(command):
    #When reading a non-existent file, it causes a FileNotFoundError. To prevent expensive error-catching processes, we just use the append mode to create a file if necessary, and then see if its contents are blank.
    append_file = open(return_filename(command), "a")
    readfile = open(return_filename(command)).read()
    return bool(readfile)
#Planets
#Covers all planets from Mercury to Neptune
list = [199, 299, 399, 499, 599, 699, 799, 899]
#Items in the list correspond to Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, and Neptune, respectively.
#Planets done
#Asteroids
for item in range(2000001, 2001001):
    if check_existing_ephemeris(item) == False:
        ephemeris = get_object_ephemeris("'DES=" + str(item) + "'", start_date, stop_date)
        filename = return_filename(item)
        writefile = open(filename, "w")
        writefile.write(ephemeris)
        writefile.close()
        print(item)
#so far the range is to 20001000 (asteroid 1000), but there is a lot of room for expansion (particularly to the 10000 range)
#Moons
#e.g., Earth's moon is 301,
#Comets
#It's a little more complex because we need to analyze the content of the page and choose the right id for the ephemerides. (due to the number of different epochs)
#If direct output is present (i.e., the comet does not have different epochs), the file size should be larger than 1 MB. Likewise, if options are chosen, the length of the file string should not be larger than a million.


