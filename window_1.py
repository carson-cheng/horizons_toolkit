from plot_ephemeris import *
dep = 1866
arr = 3
start_date = "2025-Jan-04"
stop_date = "2026-May-29"
rev = 0
r = get_lambert_transfer(dep, arr, start_date, stop_date, rev)
frame_limits = 4
title = "Launch Window Simulator"
color_list = ['magenta', 'blue', 'green']
#plot_lambert_transfer(r[0], r[1], r[2], r[3], r[4], r[5], r[-1], frame_limits, title)
solution = plot_lambert_transfer(r[0], r[1], r[2], r[3], r[4], r[5], r[-1], frame_limits, title, color_list, 3000, 0.9756110228429035, plot=True)
print("Trajectory ephemeris length")
#print(len(solution[0]))
image_name = "window.gif"
divisor = 3
#data_to_gif(data, divisor, color_list, title, image_name, frame_limits)
print(closest_approach(4, solution, start_date, stop_date))
