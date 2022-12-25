#2022 Earth-Mars launch window calculator
from lamberthub import izzo2015
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import animation
from plot_ephemeris import *
au = 149597870.7
mu = int(6.674e-11 * 1.989e+30)
start_date = "2005-Mar-2"
stop_date = "2007-Feb-25"
earth = read_ephemeris(get_object_ephemeris(3, start_date, stop_date), start_date, stop_date)
mars = read_ephemeris(get_object_ephemeris(4, start_date, stop_date), start_date, stop_date)
r1 = np.array([earth[0][0]*1000, earth[1][0]*1000, earth[2][0]*1000])
r2 = np.array([mars[0][-1]*1000, mars[1][-1]*1000, mars[2][-1]*1000])
tof = tof_time(start_date, stop_date)
#2020 launch opportunity
#tof = 17539200
v1, v2= izzo2015(mu, r1, r2, tof, M=1, prograde=True, low_path=True, maxiter=35, atol=1e-5, rtol=1e-7, full_output=False)
print(v1, v2)
def model_2BP(state, t):
    mu = int(6.674e-11 * 1.989e+30)/10**9  # Sun's gravitational parameter
                          # [km^3/s^2]
    x = state[0]
    y = state[1]
    z = state[2]
    x_dot = state[3]
    y_dot = state[4]
    z_dot = state[5]
    x_ddot = -mu * x / (x ** 2 + y ** 2 + z ** 2) ** (3 / 2)
    y_ddot = -mu * y / (x ** 2 + y ** 2 + z ** 2) ** (3 / 2)
    z_ddot = -mu * z / (x ** 2 + y ** 2 + z ** 2) ** (3 / 2)
    dstate_dt = [x_dot, y_dot, z_dot, x_ddot, y_ddot, z_ddot]
    return dstate_dt
# Initial Conditions
X_0 = r1[0] / 1000  # [km]
Y_0 = r1[1] / 1000  # [km]
Z_0 = r1[2] / 1000  # [km]
VX_0 = v1[0] / 1000  # [km/s]
VY_0 = v1[1] / 1000  # [km/s]
VZ_0 = v1[2] / 1000  # [km/s]
state_0 = [X_0, Y_0, Z_0, VX_0, VY_0, VZ_0]
title = "Rosetta trajectory to Mars gravity assist"
frame_limits = 1.5
# Time Array
t = np.linspace(0, tof, int(tof/86400))
# Solving ODE
sol = odeint(model_2BP, state_0, t)
X_Sat = sol[:, 0]  # X-coord [km] of satellite over time interval
Y_Sat = sol[:, 1]  # Y-coord [km] of satellite over time interval
Z_Sat = sol[:, 2]  # Z-coord [km] of satellite over time interval
solution = np.array([X_Sat, Y_Sat, Z_Sat])
print(Y_Sat[-1])
print(mars[1][-1])
fig = plt.figure()
ax = plt.axes(projection = '3d')
ax.set_xlim([-frame_limits * au, frame_limits * au])
ax.set_ylim([-frame_limits * au, frame_limits * au])
ax.set_zlim([-frame_limits * au, frame_limits * au])
color_count = 0
ax.plot3D(solution[0][-1], solution[1][-1], solution[2][-1], "magenta")
ax.scatter3D(solution[0][-1], solution[1][-1], solution[2][-1], s=8, linewidth=1, color="magenta")
ax.plot3D(earth[0][-1], earth[1][-1], earth[2][-1], "blue")
ax.scatter3D(earth[0][-1], earth[1][-1], earth[2][-1], s=8, linewidth=1, color="blue")
ax.plot3D(mars[0][-1], mars[1][-1], mars[2][-1], "red")
ax.scatter3D(mars[0][-1], mars[1][-1], mars[2][-1], s=8, linewidth=1, color="red")
ax.set_title(title)
plt.show()
'''for item in len(X_Sat):
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    ax.plot3D(X_Sat, Y_Sat, Z_Sat, 'magenta')
    ax.plot3D(mars[0], mars[1], mars[2], 'red')
    ax.plot3D(earth[0], earth[1], earth[2], 'blue')
    frame_limits = 1.5
    ax.set_xlim([-frame_limits * au, frame_limits * au])
    ax.set_ylim([-frame_limits * au, frame_limits * au])
    ax.set_zlim([-frame_limits * au, frame_limits * au])
    ax.set_title("2005 Rosetta Earth-Mars Trajectory")
    plt.show()'''
