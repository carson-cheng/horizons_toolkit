#2022 Earth-Mars launch window calculator
from lamberthub import izzo2015
import math
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import animation
from plot_ephemeris import *
au = 149597870.7
mu = int(6.674e-11 * 1.989e+30)
#Position of Earth at 2022-10-01
start_date = "2024-Feb-25"
stop_date = "2024-Sep-25"
venus = read_ephemeris(get_object_ephemeris(2, start_date, stop_date), start_date, stop_date)
#print(earth_pos)
r1 = np.array([venus[0][0] * 1000, venus[1][0] * 1000, venus[2][0] * 1000])
#2020 launch opportunity
#r1 = np.array([9.162476184645234E+10, -1.194644807635267E+11, 1.600952775991708E+07])
#Position of Mars at 2023-04-13
apophis_ephemeris = get_object_ephemeris(99942, start_date, stop_date)
apophis = read_ephemeris(apophis_ephemeris, start_date, stop_date)
r2 = np.array([apophis[0][-1] * 1000, apophis[1][-1] * 1000, apophis[2][-1] * 1000])
#2020 launch opportunity
#r2 = np.array([-2.952973715050595E+09, 2.357856297591636E+11, 4.987398985809878E+09])
#time of flight (presumably in seconds, but if there is weird output, this one is the first to change)
tof = tof_time(start_date, stop_date)
#2020 launch opportunity
#tof = 17539200
v1, v2= izzo2015(mu, r1, r2, tof, M=0, prograde=True, low_path=True, maxiter=35, atol=1e-5, rtol=1e-7, full_output=False)
print(mu)
print(r1)
print(r2)
print(tof)
print("V1: " + str(v1))
# Initial Conditions
X_0 = r1[0] / 1000  # [km]
Y_0 = r1[1] / 1000  # [km]
Z_0 = r1[2] / 1000  # [km]
VX_0 = v1[0] / 1000  # [km/s]
VY_0 = v1[1] / 1000  # [km/s]
VZ_0 = v1[2] / 1000  # [km/s]
state_0 = [X_0, Y_0, Z_0, VX_0, VY_0, VZ_0]
#print(state_0)
#apophis_arrival_velocity = np.array([2.161802205251818E+01,-2.020234178745368E+01,1.588719385099676E+00])
#Get destination arrival velocity
velocity_str = apophis_ephemeris.split("$$EOE")[0].split("Z =")[-1]
#print(velocity_str)
vel_x = float(velocity_str.split("VX=")[1].split(" VY")[0])
vel_y = float(velocity_str.split("VY=")[1].split(" VZ")[0])
vel_z = float(velocity_str.split("VZ=")[1].split("\\n")[0])
apophis_arrival_velocity = [vel_x, vel_y, vel_z]
spacecraft_arrival_velocity = np.array([x / 1000 for x in v2])
rel = apophis_arrival_velocity - spacecraft_arrival_velocity
#print(rel)
print("Relative arrival velocity: " + str(distance(0, 0, 0, rel[0], rel[1], rel[2])) + " km/s")
# Time Array
t = np.linspace(0, tof, int(tof/86400))
# Solving ODE
sol = odeint(model_2BP, state_0, t)
print(state_0)
X_Sat = sol[:, 0]  # X-coord [km] of satellite over time interval
Y_Sat = sol[:, 1]  # Y-coord [km] of satellite over time interval
Z_Sat = sol[:, 2]  # Z-coord [km] of satellite over time interval
print(X_Sat[56])
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot3D(X_Sat, Y_Sat, Z_Sat, 'magenta')
ax.plot3D(apophis[0], apophis[1], apophis[2], 'green')
ax.plot3D(venus[0], venus[1], venus[2], 'gold')
frame_limits = 1
ax.set_xlim([-frame_limits * au, frame_limits * au])
ax.set_ylim([-frame_limits * au, frame_limits * au])
ax.set_zlim([-frame_limits * au, frame_limits * au])
ax.set_title("Apophis from Venus")
plt.show()
