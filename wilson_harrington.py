from plot_ephemeris import *
dep = 3
arr = 4015
start_date = "2029-Apr-13"
stop_date = "2030-Dec-20"
rev = 1
r = get_lambert_transfer(dep, arr, start_date, stop_date, rev)
frame_limits = 1.5
title = "Launch Window Simulator"
color_list = ['magenta', 'blue', 'green']
#plot_lambert_transfer(r[0], r[1], r[2], r[3], r[4], r[5], r[-1], frame_limits, title)
solution = plot_lambert_transfer(r[0], r[1], r[2], r[3], r[4], r[5], r[-1], frame_limits, title, color_list, 1000, 0.89266623291, plot=True)
data = [solution, r[0], r[1]]
print("Trajectory ephemeris length")
#print(len(solution[0]))
image_name = "4015.gif"
divisor = 3
labels = ['Transfer orbit', 'Earth', '4015 Wilson-Harrington']
data_to_gif(data, divisor, color_list, title, image_name, frame_limits)
