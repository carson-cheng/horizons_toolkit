from plot_ephemeris import *
dep = 3
arr = 5
start_date = "2024-Aug-17"
stop_date = "2027-Sep-27"
rev = 0
r = get_lambert_transfer(dep, arr, start_date, stop_date, rev)
frame_limits = 4
title = "Launch Window Simulator"
color_list = ['magenta', 'blue', 'green', 'brown']
#plot_lambert_transfer(r[0], r[1], r[2], r[3], r[4], r[5], r[-1], frame_limits, title)
stop_2 = "2027-Sep-17"
r1 = read_ephemeris(get_object_ephemeris(dep, start_date, stop_2), start_date, stop_2)
r2 = read_ephemeris(get_object_ephemeris(arr, start_date, stop_2), start_date, stop_2)
r3 = read_ephemeris(get_object_ephemeris(182, start_date, stop_2), start_date, stop_2)
tof_t = tof_time(start_date, stop_2)
solution = plot_lambert_transfer(r1, r2, r[2], r[3], r[4], r[5], tof_t, frame_limits, title, color_list, 1, 1, plot=True, propagate=True)
data = [solution, r1, r2, r3]
print("Trajectory ephemeris length")
#print(len(solution[0]))
image_name = "window.gif"
divisor = 6
data_to_gif(data, divisor, color_list, title, image_name, frame_limits)
print("Closest")
for item in range(2000001, 2001000):
    try:
        try:
            if item > 2000000:
                command = "'DES=" + str(item) + "'"
            else:
                command = "'DES=" + str(2000000 + item) + "'"
        except:
            command = item
        closest_approach(command, solution, start_date, stop_2)
    except:
        pass
