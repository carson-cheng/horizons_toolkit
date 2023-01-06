from plot_ephemeris import *
obj1 = 3
obj2 = 419624
start_date = "1600-Jan-01"
stop_date = "2500-Jan-01"
step_size = "8766m" #Earth's approximate orbital period divided by period
period = 60 #the number of frames that correspond to one period of the primary object
e1 = read_ephemeris(get_object_ephemeris(obj1, start_date, stop_date, step_size=step_size), start_date, stop_date, period=period)
e2 = read_ephemeris(get_object_ephemeris(obj2, start_date, stop_date, step_size=step_size), start_date, stop_date, period=period)
data = [e1, e2]
frame_limits = 1
title = "Rotating frame simulator"
color_list = ['brown', 'magenta']
divisor = 120
image_name = "rotating.gif"
data_to_gif(data, divisor, color_list, title, image_name, frame_limits, gif_divisor=1)
