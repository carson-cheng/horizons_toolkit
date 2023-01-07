from plot_ephemeris import *
obj1 = 3
obj2 = "Rosetta"
obj3 = 90000698
obj4 = 4
obj5 = 21
obj6 = 2867
center = 0
start_date = "2004-Mar-03"
stop_date = "2016-Sep-29"
step_size = "16638m"
period = 0 #no rotation frame is specified.
e1 = read_ephemeris(get_object_ephemeris(obj1, start_date, stop_date, step_size=step_size, center=center), start_date, stop_date, period=period)
e2 = read_ephemeris(get_object_ephemeris(obj2, start_date, stop_date, step_size=step_size, center=center), start_date, stop_date, period=period)
e3 = read_ephemeris(get_object_ephemeris(obj3, start_date, stop_date, step_size=step_size, center=center), start_date, stop_date, period=period)
e4 = read_ephemeris(get_object_ephemeris(obj4, start_date, stop_date, step_size=step_size, center=center), start_date, stop_date, period=period)
e5 = read_ephemeris(get_object_ephemeris(obj5, start_date, stop_date, step_size=step_size, center=center), start_date, stop_date, period=period)
e6 = read_ephemeris(get_object_ephemeris(obj6, start_date, stop_date, step_size=step_size, center=center), start_date, stop_date, period=period)
data = [e1, e2, e3, e4, e5, e6]
frame_limits = 4
title = "Rosetta"
color_list = ['blue', 'magenta', 'green', 'red', 'cyan', 'gold']
divisor = 1
image_name = "rosetta.gif"
data_to_gif(data, divisor, color_list, title, image_name, frame_limits, gif_divisor=1)

