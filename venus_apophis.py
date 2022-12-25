from plot_ephemeris import *
dep = 2
arr = 99942
start_date = "2024-Feb-25"
stop_date = "2024-Sep-25"
rev = 0
r = get_lambert_transfer(dep, arr, start_date, stop_date, rev)
frame_limits = 1.2
title = "Venus-Apophis 2024 launch window"
color_list = ['magenta', 'gold', 'green']
#plot_lambert_transfer(r[0], r[1], r[2], r[3], r[4], r[5], r[-1], frame_limits, title)
solution = plot_lambert_transfer(r[0], r[1], r[2], r[3], r[4], r[5], r[-1], frame_limits, title, color_list, plot=False)
data = [solution, r[0], r[1]]
image_name = "apophis_venus.gif"
divisor = 3
data_to_gif(data, divisor, color_list, title, image_name, frame_limits)
