from plot_ephemeris import *
obj1 = 5
obj2 = "'DES=2000624'"
start_date = "1600-Jan-01"
stop_date = "2500-Jan-01"
step_size = "17573m" #Jupiter's approximate orbital period divided by period
period = 355 #the number of frames that correspond to one period of the primary object
e1 = read_ephemeris(get_object_ephemeris(obj1, start_date, stop_date, step_size=step_size), start_date, stop_date, period=period)
e2 = read_ephemeris(get_object_ephemeris(obj2, start_date, stop_date, step_size=step_size), start_date, stop_date, period=period)
data = [e1, e2]
frame_limits = 5.2
title = "Rotating frame simulator"
color_list = ['brown', 'magenta']
divisor = 71
image_name = "rotating.gif"
data_to_gif(data, divisor, color_list, title, image_name, frame_limits, gif_divisor=1)
