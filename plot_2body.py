import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
# Earth Model
def model_2BP(state, t):
    mu = int(9.40275927e+26 * 6.674e-11)/10**9
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
X_0 = 477298  # [km]
Y_0 = 0.01  # [km]
Z_0 = 0.01  # [km]
VX_0 = 0.02  # [km/s]
VY_0 = 10.21  # [km/s]
VZ_0 = 0.16  # [km/s]
state_0 = [X_0, Y_0, Z_0, VX_0, VY_0, VZ_0]

# Time Array
t = np.linspace(0, 150000, 900)  # Simulates for a time period of 6
                                 # hours [s]
frame_limits = 0.005
au = 149597870.7
# Solving ODE
sol = odeint(model_2BP, state_0, t)
X_Sat = sol[:, 0]  # X-coord [km] of satellite over time interval
Y_Sat = sol[:, 1]  # Y-coord [km] of satellite over time interval
Z_Sat = sol[:, 2]  # Z-coord [km] of satellite over time interval
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot3D(X_Sat, Y_Sat, Z_Sat, 'magenta')
print(len(X_Sat))
ax.set_xlim([-frame_limits * au, frame_limits * au])
ax.set_ylim([-frame_limits * au, frame_limits * au])
ax.set_zlim([-frame_limits * au, frame_limits * au])
ax.set_title("Orbit simulator")
plt.show()
