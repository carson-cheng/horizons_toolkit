from plot_ephemeris import *
dep = 3
arr = 90000742
start_date = "2026-May-29"
stop_date = "2032-Apr-26"
rev = 0
r = get_lambert_transfer(3, 90000742, "2026-May-29", "2027-Nov-30", 0)
r1 = get_lambert_transfer(90000742, 3, "2027-Nov-30", "2029-May-29", 1)
r2 = get_lambert_transfer(3, "311P", "2029-May-29", "2030-Oct-01", 0)
r3 = get_lambert_transfer("311P", 3, "2030-Oct-01", "2031-May-29", 0)
r4 = get_lambert_transfer(3, "'DES=2017 YE5'", "2031-May-29", "2032-Apr-26", 0)
frame_limits = 2
title = "Launch Window Simulator"
color_list = ['magenta', 'blue', 'green', 'brown', 'red']
#plot_lambert_transfer(r[0], r[1], r[2], r[3], r[4], r[5], r[-1], frame_limits, title)
stop_2 = "2033-Apr-26"
f1 = read_ephemeris(get_object_ephemeris(3, start_date, stop_2), start_date, stop_2)
f2 = read_ephemeris(get_object_ephemeris(90000742, start_date, stop_2), start_date, stop_2)
f3 = read_ephemeris(get_object_ephemeris("311P", start_date, stop_2), start_date, stop_2)
f4 = read_ephemeris(get_object_ephemeris("'DES=2017 YE5'", start_date, stop_2), start_date, stop_2)
e1 = read_ephemeris(get_object_ephemeris(3, "2026-May-29", "2027-Nov-30"), "2026-May-29", "2027-Nov-30")
e2 = read_ephemeris(get_object_ephemeris(90000742, "2026-May-29", "2027-Nov-30"), "2026-May-29", "2027-Nov-30")
e3 = read_ephemeris(get_object_ephemeris(90000742, "2027-Nov-30", "2029-May-29"), "2027-Nov-30", "2029-May-29")
e4 = read_ephemeris(get_object_ephemeris(3, "2027-Nov-30", "2029-May-29"), "2027-Nov-30", "2029-May-29")
e5 = read_ephemeris(get_object_ephemeris(3, "2029-May-29", "2030-Oct-01"), "2029-May-29", "2030-Oct-01")
e6 = read_ephemeris(get_object_ephemeris("311P", "2029-May-29", "2030-Oct-01"), "2029-May-29", "2030-Oct-01")
e7 = read_ephemeris(get_object_ephemeris("311P", "2030-Oct-01", "2031-May-29"), "2030-Oct-01", "2031-May-29")
e8 = read_ephemeris(get_object_ephemeris(3, "2030-Oct-01", "2031-May-29"), "2030-Oct-01", "2031-May-29")
e9 = read_ephemeris(get_object_ephemeris(3, "2031-May-29", "2033-Apr-26"), "2031-May-29", "2033-Apr-26")
e10 = read_ephemeris(get_object_ephemeris("'DES=2017 YE5'", "2031-May-29", "2033-Apr-26"), "2031-May-29", "2033-Apr-26")
solution = plot_lambert_transfer(e1, e2, r[2], r[3], r[4], r[5], tof_time("2026-May-29", "2027-Nov-30"), frame_limits, title, color_list, 1, 1, plot=True, propagate=True)
solution1 = plot_lambert_transfer(e3, e4, r1[2], r1[3], r1[4], r1[5], tof_time("2027-Nov-30", "2029-May-29"), frame_limits, title, color_list, 1, 1, plot=True, propagate=True)
solution2 = plot_lambert_transfer(e5, e6, r2[2], r2[3], r2[4], r2[5], tof_time("2029-May-29", "2030-Oct-01"), frame_limits, title, color_list, 1, 1, plot=True, propagate=True)
solution3 = plot_lambert_transfer(e7, e8, r3[2], r3[3], r3[4], r3[5], tof_time("2030-Oct-01", "2031-May-29"), frame_limits, title, color_list, 1, 1, plot=True, propagate=True)
solution4 = plot_lambert_transfer(e9, e10, r4[2], r4[3], r4[4], r4[5], tof_time("2031-May-29", "2033-Apr-26"), frame_limits, title, color_list, 1, 1, plot=True, propagate=True)
coordinates = [solution, solution1, solution2, solution3, solution4]
#coordinates = [solution, solution1, solution2, solution3]
x = []
y = []
z = []
print(len(solution[0]))
for item in range(len(coordinates)):
    x = np.concatenate([x, coordinates[item][0]])
    y = np.concatenate([y, coordinates[item][1]])
    z = np.concatenate([z, coordinates[item][2]])
'''x_new = []
y_new = []
z_new = []
for item in range(len(x)):
    if item % len(coordinates) == 0:
        x_new.append(x[item])
        y_new.append(y[item])
        z_new.append(z[item])
sol = [x_new, y_new, z_new]
print(len(sol[0]))'''
sol = [x, y, z]
data = [sol, f1, f2, f3, f4]
print("Trajectory ephemeris length")
#print(len(solution[0]))
image_name = "window.gif"
divisor = 11
data_to_gif(data, divisor, color_list, title, image_name, frame_limits)
print("Closest")
'''for item in range(350):
    try:
        closest_approach(get_comet_ephemeris(item, start_date, stop_2), solution, start_date, stop_2)
    except:
        pass'''
