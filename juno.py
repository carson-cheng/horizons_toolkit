import numpy as np
import matplotlib.pyplot as plt
from plot_ephemeris import *
import requests, os
start_date = "2011-Aug-06"
stop_date = "2017-Dec-31"
au = 149597870.7
#The command parameter "3" represents Earth in the Horizons system
coordinate1 = read_ephemeris(get_object_ephemeris(3, start_date, stop_date), start_date, stop_date)
print(1)
coordinate2 = read_ephemeris(get_object_ephemeris(-61, start_date, stop_date), start_date, stop_date)
print(2)
coordinate3 = read_ephemeris(get_object_ephemeris(5, start_date, stop_date), start_date, stop_date)
print(3)
coordinate4 = read_ephemeris(get_object_ephemeris(27, start_date, stop_date), start_date, stop_date)
print(4)
coordinate5 = read_ephemeris(get_object_ephemeris(415, start_date, stop_date), start_date, stop_date)
print(5)
#The command parameter "Pallas" represents the asteroid Pallas in the Horizons system. It is one of the most massive asteroids, but is significantly inclined relative to the ecliptic.
data = [coordinate1, coordinate2, coordinate3, coordinate4, coordinate5]
print("object done")
#print(len(x1))
#days = len(x1) / 24
divisor = 15
color_list = ['blue', 'magenta', 'brown', 'green', 'red']
title = "Juno"
image_name = "juno.gif"
frame_limits = 4
data_to_gif(data, divisor, color_list, title, image_name, frame_limits)
