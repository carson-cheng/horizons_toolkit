import numpy as np
import matplotlib.pyplot as plt
from plot_ephemeris import *
import requests, os
start_date = "2016-Sep-09"
stop_date = "2023-Sep-24"
au = 149597870.7
#The command parameter "3" represents Earth in the Horizons system
coordinate1 = read_ephemeris(get_object_ephemeris(3, start_date, stop_date), start_date, stop_date)
print(1)
coordinate2 = read_ephemeris(get_object_ephemeris("OSIRIS-REx", start_date, stop_date), start_date, stop_date)
print(2)
coordinate3 = read_ephemeris(get_object_ephemeris(101955, start_date, stop_date), start_date, stop_date)
print(3)
data = [coordinate1, coordinate2, coordinate3]
print("object done")
#print(len(x1))
#days = len(x1) / 24
divisor = 15
color_list = ['blue', 'magenta', 'green']
title = "OSIRIS-REx"
image_name = "orx.gif"
frame_limits = 1.2
data_to_gif(data, divisor, color_list, title, image_name, frame_limits)
