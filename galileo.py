import numpy as np
import matplotlib.pyplot as plt
from plot_ephemeris import *
import requests, os
start_date = "1989-Oct-20"
stop_date = "1997-Dec-31"
au = 149597870.7
coordinate1 = read_ephemeris(get_object_ephemeris(3, start_date, stop_date), start_date, stop_date)
print(1)
coordinate2 = read_ephemeris(get_object_ephemeris(-77, start_date, stop_date), start_date, stop_date)
print(2)
coordinate3 = read_ephemeris(get_object_ephemeris(5, start_date, stop_date), start_date, stop_date)
print(3)
coordinate4 = read_ephemeris(get_object_ephemeris(243, start_date, stop_date), start_date, stop_date)
print(4)
coordinate5 = read_ephemeris(get_object_ephemeris(951, start_date, stop_date), start_date, stop_date)
print(5)
coordinate6 = read_ephemeris(get_object_ephemeris(2, start_date, stop_date), start_date, stop_date)
print(6)
data = [coordinate1, coordinate2, coordinate3, coordinate4, coordinate5, coordinate6]
print("object done")
#print(len(x1))
#days = len(x1) / 24
divisor = 15
color_list = ['blue', 'magenta', 'brown', 'red', 'green', 'gold']
title = "Galileo"
image_name = "galileo.gif"
frame_limits = 4
data_to_gif(data, divisor, color_list, title, image_name, frame_limits)