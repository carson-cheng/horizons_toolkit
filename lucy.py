from plot_ephemeris import *
obj1 = 5
obj2 = -49
obj3 = 3
obj4 = 52246
obj5 = 3548
obj6 = 15094
obj7 = 11351
obj8 = 21900
obj9 = "'DES=2000617'"
center = 0
start_date = "2021-Oct-17"
stop_date = "2033-Mar-24"
step_size = "16638m" #Jupiter's approximate orbital period divided by period
period = 0 #no rotation frame is specified.
e1 = read_ephemeris(get_object_ephemeris(obj1, start_date, stop_date, step_size=step_size, center=center), start_date, stop_date, period=period)
e2 = read_ephemeris(get_object_ephemeris(obj2, start_date, stop_date, step_size=step_size, center=center), start_date, stop_date, period=period)
e3 = read_ephemeris(get_object_ephemeris(obj3, start_date, stop_date, step_size=step_size, center=center), start_date, stop_date, period=period)
e4 = read_ephemeris(get_object_ephemeris(obj4, start_date, stop_date, step_size=step_size, center=center), start_date, stop_date, period=period)
e5 = read_ephemeris(get_object_ephemeris(obj5, start_date, stop_date, step_size=step_size, center=center), start_date, stop_date, period=period)
e6 = read_ephemeris(get_object_ephemeris(obj6, start_date, stop_date, step_size=step_size, center=center), start_date, stop_date, period=period)
e7 = read_ephemeris(get_object_ephemeris(obj7, start_date, stop_date, step_size=step_size, center=center), start_date, stop_date, period=period)
e8 = read_ephemeris(get_object_ephemeris(obj8, start_date, stop_date, step_size=step_size, center=center), start_date, stop_date, period=period)
e9 = read_ephemeris(get_object_ephemeris(obj9, start_date, stop_date, step_size=step_size, center=center), start_date, stop_date, period=period)
data = [e1, e2, e3, e4, e5, e6, e7, e8, e9]
frame_limits = 5.2
title = "Lucy"
color_list = ['brown', 'magenta', 'blue', 'green', 'grey', 'coral', 'lime', 'indigo', 'cyan']
divisor = 1
image_name = "lucy.gif"
data_to_gif(data, divisor, color_list, title, image_name, frame_limits, gif_divisor=1)
