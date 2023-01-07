from plot_ephemeris import *
import matplotlib.pyplot as plt
import numpy as np
import random
results = small_body_query([("sb-kind", "=", "a"), ("sb-ns", "=", "n"), ("a", "<", "6")], ["pdes", "a", "e"])
results = random.choices(results, k=20000)
param0 = []
param1 = []
param2 = []
for item in results:
    p0 = item[0]
    p1 = item[1]
    p2 = item[2]
    if p1[0] == ".":
        p1 = "0" + p1
    if p2[0] == ".":
        p2 = "0" + p2
    param1.append(float(p1))
    param2.append(float(p2))
    param0.append(p0)
#print(param1)
#print(param2)
param1 = np.array(param1)
param2 = np.array(param2)
#print(param0)
fig = plt.figure()
plt.scatter(param1, param2, s=1)
plt.xlabel("Semi-major axis (au)")
plt.ylabel("Eccentricity")
plt.title("Semi-major axis vs eccentricity")
plt.show()
