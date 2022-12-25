import numpy as np
import matplotlib.pyplot as plt
from plot_ephemeris import *
import requests, os
start_date = "2021-Nov-25"
stop_date = "2022-Sep-26"
au = 149597870.7
#The command parameter "3" represents Earth in the Horizons system
coordinate1 = read_ephemeris(get_object_ephemeris(3, start_date, stop_date), start_date, stop_date)
print(1)
coordinate2 = read_ephemeris(get_object_ephemeris("DART", start_date, stop_date), start_date, stop_date)
print(2)
coordinate3 = read_ephemeris(get_object_ephemeris(65803, start_date, stop_date), start_date, stop_date)
print(3)
#The command parameter "Pallas" represents the asteroid Pallas in the Horizons system. It is one of the most massive asteroids, but is significantly inclined relative to the ecliptic.
data = [coordinate1, coordinate2, coordinate3]
print("object done")
#print(len(x1))
#days = len(x1) / 24
divisor = 5
color_list = ['blue', 'magenta', 'green']
title = "DART"
image_name = "dart.gif"
frame_limits = 2
data_to_gif(data, divisor, color_list, title, image_name, frame_limits)
