import numpy as np
import matplotlib.pyplot as plt
from plot_ephemeris import *
import requests, os
start_date = "2024-Oct-11"
stop_date = "2030-Apr-11"
au = 149597870.7
coordinate1 = read_ephemeris(get_object_ephemeris(3, start_date, stop_date), start_date, stop_date)
print(1)
#The command parameter "3" represents Earth in the Horizons system
coordinate2 = read_ephemeris(get_object_ephemeris(-159, start_date, stop_date), start_date, stop_date)
print(2)
coordinate3 = read_ephemeris(get_object_ephemeris(4, start_date, stop_date), start_date, stop_date)
print(3)
coordinate4 = read_ephemeris(get_object_ephemeris(5, start_date, stop_date), start_date, stop_date)
print(4)
#coordinate5 = read_ephemeris(get_object_ephemeris(1602, start_date, stop_date), start_date, stop_date)
#print(5)
coordinate6 = read_ephemeris(get_object_ephemeris(3375, start_date, stop_date), start_date, stop_date)
print(6)
coordinate7 = read_ephemeris(get_object_ephemeris(6265, start_date, stop_date), start_date, stop_date)
print(7)
coordinate8 = read_ephemeris(get_object_ephemeris(3253, start_date, stop_date), start_date, stop_date)
print(8)
#The command parameter "Pallas" represents the asteroid Pallas in the Horizons system. It is one of the most massive asteroids, but is significantly inclined relative to the ecliptic.
data = [coordinate1, coordinate2, coordinate3, coordinate4, coordinate6, coordinate7, coordinate8]
print("object done")
#print(len(x1))
#days = len(x1) / 24
divisor = 15
color_list = ['blue', 'magenta', 'red', 'brown', 'green', 'violet', 'pink']
title = "Europa clipper"
image_name = "europa_clipper.gif"
frame_limits = 4
data_to_gif(data, divisor, color_list, title, image_name, frame_limits)
