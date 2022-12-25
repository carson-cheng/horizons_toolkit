import numpy as np
import matplotlib.pyplot as plt
from plot_ephemeris import *
import requests, os
start_date = "2005-Jan-13"
stop_date = "2012-Mar-14"
au = 149597870.7
#The command parameter "3" represents Earth in the Horizons system
coordinate1 = read_ephemeris(get_object_ephemeris(3, start_date, stop_date), start_date, stop_date)
print(1)
coordinate2 = read_ephemeris(get_object_ephemeris(-140, start_date, stop_date), start_date, stop_date)
print(2)
coordinate3 = read_ephemeris(get_object_ephemeris(90000191, start_date, stop_date), start_date, stop_date)
print(3)
coordinate4 = read_ephemeris(open("103P/103P_ephemeris.txt").read(), start_date, stop_date)
print(4)
#The command parameter "Pallas" represents the asteroid Pallas in the Horizons system. It is one of the most massive asteroids, but is significantly inclined relative to the ecliptic.
data = [coordinate1, coordinate2, coordinate3, coordinate4]
print("object done")
#print(len(x1))
#days = len(x1) / 24
divisor = 15
color_list = ['blue', 'magenta', 'green', 'cyan']
title = "Deep Impact"
image_name = "deep_impact.gif"
frame_limits = 3.5
data_to_gif(data, divisor, color_list, title, image_name, frame_limits)
