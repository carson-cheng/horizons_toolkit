import numpy as np
import matplotlib.pyplot as plt
from plot_ephemeris import *
import requests, os
start_date = "2021-Oct-17"
stop_date = "2033-Apr-02"
au = 149597870.7
coordinate1 = read_ephemeris(get_object_ephemeris(3, start_date, stop_date), start_date, stop_date)
print(1)
coordinate2 = read_ephemeris(get_object_ephemeris(-49, start_date, stop_date), start_date, stop_date)
print(2)
coordinate3 = read_ephemeris(get_object_ephemeris("Patroclus", start_date, stop_date), start_date, stop_date)
print(3)
coordinate4 = read_ephemeris(get_object_ephemeris(3548, start_date, stop_date), start_date, stop_date)
print(4)
coordinate5 = read_ephemeris(get_object_ephemeris(21900, start_date, stop_date), start_date, stop_date)
print(5)
coordinate6 = read_ephemeris(get_object_ephemeris(11351, start_date, stop_date), start_date, stop_date)
print(6)
coordinate7 = read_ephemeris(get_object_ephemeris(52246, start_date, stop_date), start_date, stop_date)
print(7)
coordinate8 = read_ephemeris(get_object_ephemeris(15094, start_date, stop_date), start_date, stop_date)
print(8)
coordinate9 = read_ephemeris(get_object_ephemeris(5, start_date, stop_date), start_date, stop_date)
print(9)
#The command parameter "Pallas" represents the asteroid Pallas in the Horizons system. It is one of the most massive asteroids, but is significantly inclined relative to the ecliptic.
data = [coordinate1, coordinate2, coordinate3, coordinate4, coordinate5, coordinate6, coordinate7, coordinate8, coordinate9]
print("object done")
print(len(data[0][1]))
#print(len(x1))
#days = len(x1) / 24
divisor = 22
color_list = ['blue', 'magenta', 'yellow', 'cyan', 'green', 'tan', 'pink', 'violet', 'brown']
title = "Lucy"
image_name = "lucy.gif"
frame_limits = 6
data_to_gif(data, divisor, color_list, title, image_name, frame_limits)
