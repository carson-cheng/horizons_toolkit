import numpy as np
import matplotlib.pyplot as plt
from plot_ephemeris import *
import requests, os
start_date = "2019-Jan-1"
stop_date = "2023-Jan-1"
au = 149597870.7
coordinate1 = read_ephemeris(get_object_ephemeris(3, start_date, stop_date), start_date, stop_date)
#The command parameter "3" represents Earth in the Horizons system
coordinate2 = read_ephemeris(get_object_ephemeris("Pallas", start_date, stop_date), start_date, stop_date)
#The command parameter "Pallas" represents the asteroid Pallas in the Horizons system. It is one of the most massive asteroids, but is significantly inclined relative to the ecliptic.
data = [coordinate1]
print("object done")
#print(len(x1))
#days = len(x1) / 24
divisor = 15
color_list = ['blue']
title = "Earth"
image_name = "earth.gif"
data_to_gif(data, divisor, color_list, title, image_name, 1)
