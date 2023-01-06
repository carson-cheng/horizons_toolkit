import numpy as np
import matplotlib.pyplot as plt
from plot_ephemeris import *
import requests, os
start_date = "2023-Jan-01"
stop_date = "2223-Jan-01"
au = 149597870.7
coordinate1 = read_ephemeris(get_object_ephemeris(5, start_date, stop_date), start_date, stop_date)
print(1)
coordinate2 = read_ephemeris(get_object_ephemeris(6, start_date, stop_date), start_date, stop_date)
print(2)
coordinate3 = read_ephemeris(get_object_ephemeris(4, start_date, stop_date), start_date, stop_date)
print(3)
coordinate4 = read_ephemeris(get_object_ephemeris(3, start_date, stop_date), start_date, stop_date)
print(4)
coordinate5 = read_ephemeris(get_object_ephemeris(99942, start_date, stop_date), start_date, stop_date)
print(5)
data = [coordinate1, coordinate2, coordinate3, coordinate4, coordinate5]
for item in data:
    print(len(item[0]))
print("object done")
#print(len(x1))
#days = len(x1) / 24
divisor = 15
color_list = ['brown', 'gold', 'red', 'blue', 'magenta']
label_list = ['Jupiter', 'Saturn', 'Mars', 'Earth', '16P']
title = "99942"
image_name = "99942.png"
frame_limits = 8
plot_2d(data, color_list, frame_limits, title, image_name, show=True)
image_name = "99942_3d.png"
frame_limits = frame_limits / 1.5
plot_data(data, color_list, frame_limits, title, image_name, show=True)
