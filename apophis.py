import numpy as np
import matplotlib.pyplot as plt
from plot_ephemeris import *
import requests, os
start_date = "2023-Apr-13"
stop_date = "2032-Apr-13"
au = 149597870.7
coordinate1 = read_ephemeris(get_object_ephemeris(3, start_date, stop_date), start_date, stop_date)
#The command parameter "3" represents Earth in the Horizons system
coordinate2 = read_ephemeris(get_object_ephemeris(99942, start_date, stop_date), start_date, stop_date)
coordinate3 = read_ephemeris(get_object_ephemeris(2, start_date, stop_date), start_date, stop_date)
data = [coordinate1, coordinate2, coordinate3]
print("object done")
#print(len(x1))
#days = len(x1) / 24
divisor = 15
color_list = ['blue', 'green', 'gold']
title = "Apophis"
image_name = "apophis.gif"
data_to_gif(data, divisor, color_list, title, image_name, 1)
