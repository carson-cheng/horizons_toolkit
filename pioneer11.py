import numpy as np
import matplotlib.pyplot as plt
from plot_ephemeris import *
import requests, os
start_date = "1973-Apr-11"
stop_date = "1980-Dec-31"
au = 149597870.7
#The command parameter "3" represents Earth in the Horizons system
coordinate1 = read_ephemeris(get_object_ephemeris(3, start_date, stop_date), start_date, stop_date)
print(1)
coordinate2 = read_ephemeris(get_object_ephemeris(-24, start_date, stop_date), start_date, stop_date)
print(2)
coordinate3 = read_ephemeris(get_object_ephemeris(5, start_date, stop_date), start_date, stop_date)
print(3)
coordinate4 = read_ephemeris(get_object_ephemeris(6, start_date, stop_date), start_date, stop_date)
print(4)
data = [coordinate1, coordinate2, coordinate3, coordinate4]
print("object done")
#print(len(x1))
#days = len(x1) / 24
divisor = 22
color_list = ['blue', 'magenta', 'brown', 'gold']
title = "Pioneer 11"
image_name = "pioneer11.gif"
frame_limits = 6
data_to_gif(data, divisor, color_list, title, image_name, frame_limits)
