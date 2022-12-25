import numpy as np
import matplotlib.pyplot as plt
from plot_ephemeris import *
import requests, os
def get_object_ephemeris(command, start_date, stop_date):
    #Gets the object's ephemeris vectors from the Horizons system
    #The command variable can be a number or a name. Most of the time, the command number will point you to the asteroid bearing that number, but sometimes it points to a major planet, a barycenter or a moon instead.
    url = "https://ssd.jpl.nasa.gov/api/horizons.api?command=" + str(command) + "&obj_data=no&make_ephem=yes&ephem_type=vectors&start_time=" + str(start_date) + "&stop_time=" + str(stop_date) + "&center=@6"
    return requests.get(url).text
start_date = "2006-Jul-1"
stop_date = "2007-Nov-1"
au = 149597870.7
#The command parameter "3" represents Earth in the Horizons system
coordinate1 = read_ephemeris(get_object_ephemeris(-82, start_date, stop_date), start_date, stop_date)
print(1)
coordinate2 = read_ephemeris(get_object_ephemeris(602, start_date, stop_date), start_date, stop_date)
print(2)
coordinate3 = read_ephemeris(get_object_ephemeris(606, start_date, stop_date), start_date, stop_date)
print(3)
#The command parameter "Pallas" represents the asteroid Pallas in the Horizons system. It is one of the most massive asteroids, but is significantly inclined relative to the ecliptic.
data = [coordinate1, coordinate2, coordinate3]
print("object done")
#print(len(x1))
#days = len(x1) / 24
divisor = 2
color_list = ['magenta', 'cyan', 'gold']
title = "Cassini (saturn)"
image_name = "cassini_saturn.gif"
frame_limits = 0.01
data_to_gif(data, divisor, color_list, title, image_name, frame_limits)
