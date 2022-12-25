from plot_ephemeris import *
dep = 3
arr = 4
start_date = "2022-Oct-1"
stop_date = "2023-Apr-13"
rev = 0
r = get_lambert_transfer(dep, arr, start_date, stop_date, rev)
frame_limits = 1.5
title = "Earth-Mars 2022 launch window"
color_list = ['magenta', 'blue', 'red']
#plot_lambert_transfer(r[0], r[1], r[2], r[3], r[4], r[5], r[-1], frame_limits, title)
solution = plot_lambert_transfer(r[0], r[1], r[2], r[3], r[4], r[5], r[-1], frame_limits, title, color_list, plot=True)
data = [solution, r[0], r[1]]
print("Trajectory ephemeris length")
#print(len(solution[0]))
image_name = "mml.gif"
divisor = 3
labels = ['Transfer orbit', 'Earth', 'Mars']
data_to_gif(data, divisor, color_list, title, image_name, frame_limits, labels)
