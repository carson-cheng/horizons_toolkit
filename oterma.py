import numpy as np
import matplotlib.pyplot as plt
from plot_ephemeris import *
import requests, os
start_date = "1920-Jan-01"
stop_date = "1994-Jul-16"
au = 149597870.7
coordinate1 = read_ephemeris(get_object_ephemeris(5, start_date, stop_date), start_date, stop_date)
print(1)
coordinate2 = read_ephemeris(get_object_ephemeris(6, start_date, stop_date), start_date, stop_date)
print(2)
coordinate3 = read_ephemeris(get_object_ephemeris(4, start_date, stop_date), start_date, stop_date)
print(3)
coordinate4 = read_ephemeris(get_object_ephemeris(3, start_date, stop_date), start_date, stop_date)
print(4)
coordinate5 = read_ephemeris(get_object_ephemeris("'DES=1000181'", start_date, stop_date), start_date, stop_date)
print(5)
data = [coordinate1, coordinate2, coordinate3, coordinate4, coordinate5]
print("object done")
#print(len(x1))
#days = len(x1) / 24
divisor = 15
color_list = ['brown', 'gold', 'red', 'blue', 'magenta']
label_list = ['Jupiter', 'Saturn', 'Mars', 'Earth', '81P/Wild 2']
title = "81P/Wild 2"
image_name = "wild2.png"
frame_limits = 10
plot_2d(data, color_list, label_list, frame_limits, title, image_name)
