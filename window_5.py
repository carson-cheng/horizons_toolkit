from plot_ephemeris import *
dep = 3
arr = "'DES=2017 YE5'"
start_date = "2031-May-29"
stop_date = "2032-Apr-25"
stop_3 = "2032-Oct-01"
rev = 0
r = get_lambert_transfer(dep, arr, start_date, stop_date, rev)
frame_limits = 3
title = "Launch Window Simulator"
color_list = ['magenta', 'blue', 'green', 'brown']
#plot_lambert_transfer(r[0], r[1], r[2], r[3], r[4], r[5], r[-1], frame_limits, title)
stop_2 = "2034-May-29"
r1 = read_ephemeris(get_object_ephemeris(dep, start_date, stop_2), start_date, stop_3)
r2 = read_ephemeris(get_object_ephemeris(arr, start_date, stop_2), start_date, stop_3)
r3 = read_ephemeris(get_object_ephemeris(90001269, start_date, stop_2), start_date, stop_2)
tof_2 = tof_time(stop_3, stop_2)
tof_3 = tof_time(start_date, stop_3)
solution = plot_lambert_transfer(r1, r2, r[2], r[3], r[4], r[5], tof_3, frame_limits, title, color_list, 1, 1, plot=False, propagate=True)
dep = arr
arr = np.array([solution[0][-1], solution[1][-1], solution[2][-1]]) * 1000
rev = 0
r = get_lambert_transfer(dep, arr, stop_date, stop_3, rev)
before = r[3] #velocity vector just before the maneuver
dep = np.array([solution[0][-1], solution[1][-1], solution[2][-1]]) * 1000
arr = 3
rev = 1
r = get_lambert_transfer(dep, arr, stop_3, stop_2, rev)
after = r[2] #velocity vector just after the maneuver
solution = plot_lambert_transfer(r1, r2, r[2], r[3], r[4], r[5], tof_2, frame_limits, title, color_list, 1, 1, plot=True, propagate=True)
deltav = distance(before[0], before[1], before[2], after[0], after[1], after[2])
print("Delta-v: " + str(deltav) + " m/s")
