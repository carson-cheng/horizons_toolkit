import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D
from PIL import Image
from lamberthub import izzo2015
from scipy.integrate import odeint
import requests, math, os
au = 149597870.7
#standard gravitational parameter of the sun
mu = int(6.674e-11 * 1.989e+30)
def distance(x1, y1, z1, x2, y2, z2):
    return abs(math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2))
def get_object_ephemeris(command, start_date, stop_date):
    #Gets the object's ephemeris vectors from the Horizons system
    #The command variable can be a number or a name. Most of the time, the command number will point you to the asteroid bearing that number, but sometimes it points to a major planet, a barycenter or a moon instead.
    url = "https://ssd.jpl.nasa.gov/api/horizons.api?command=" + str(command) + "&obj_data=no&make_ephem=yes&ephem_type=vectors&step_size=1d&start_time=" + str(start_date) + "&stop_time=" + str(stop_date) + "&center=@0"
    return requests.get(url).text
def read_ephemeris(ephemeris, start_date = "no_start_date", stop_date="no_stop_date"):
    #start_date and stop_date are useless now (removed for fixing a mysterious bug), but still included for backwards compatibility
    lines = ephemeris.split("\n")
    #print(len(lines))
    if len(lines) == 2:
        lines = ephemeris.split("\\n")
    x = []
    y = []
    z = []
    import time
    for item in lines:
        if "X =" in item:
            #print(item)
            x.append(float(item.split("X =")[1].split(" Y")[0]))
            y.append(float(item.split("Y =")[1].split(" Z")[0]))
            z.append(float(item.split("Z =")[1]))
    #Turns standard Python lists into numpy arrays for plotting
    x = np.array(x)
    y = np.array(y)
    z = np.array(z)
    return [x, y, z]
def data_to_gif(data, divisor, color_list, title, image_name, frame_limits):
    #Data format: [[x1, y1, z1], [x2, y2, z2], [x3, y3, z3]]
    #Makes sure that all data points are of the same length
    length = -1
    for object in data:
        for axis in object:
            obj_len = len(axis)
            if obj_len != length and length != -1:
                raise ValueError("Not all data points are of the same length.")
            else:
                days = obj_len
    #days = length
    frames = days / divisor
    #Makes sure that each data point has a color
    if len(data) != len(color_list):
        raise ValueError("Number of objects does not equal to the number of colors.")
    #Make sure that the image name is a gif file
    if "gif" not in image_name:
        raise ValueError("Image filename must contain gif.")
    #Now make each frame of the plot
    for item in range(math.floor(frames)):
        fig = plt.figure()
        ax = plt.axes(projection = '3d')
        ax.set_xlim([-frame_limits * au, frame_limits * au])
        ax.set_ylim([-frame_limits * au, frame_limits * au])
        ax.set_zlim([-frame_limits * au, frame_limits * au])
        color_count = 0
        for o in data:
            ax.plot3D(o[0][:item*divisor], o[1][:item*divisor], o[2][:item*divisor], color_list[color_count])
            ax.scatter3D(o[0][item*divisor], o[1][item*divisor], o[2][item*divisor], s=8, linewidth=1, color=color_list[color_count])
            color_count += 1
        ax.set_title(title)
        #Save each image
        plt.savefig(str(item) + ".png")
        plt.close()
        print(item)
    #Credit: https://stackoverflow.com/questions/38118598/3d-animation-using-matplotlib
    #If you open too many files at once, you may get an error saying that there are too many files open. As such, it's best to keep the file within 200 frames.
    #Another approach is to save the file in increments of 200 frames, but it has yet to be implemented (waiting for a more stable version)
    images = []
    for item in range(int(frames)):
        photo = Image.open(str(item) + ".png")
        images.append(photo)
    #images = [Image.open(f"{n}.png") for n in range(frames)]
    images[0].save(image_name, save_all=True, append_images=images[1:], duration=100, loop=0, fps=200)
    #Clean up temporary files
    os.system("rm *.png")
def tof_time(caldate_1, caldate_2):
    #Access the JD-to-calendar API
    dates = [caldate_1, caldate_2]
    julian_dates = []
    for item in dates:
        url = "https://ssd-api.jpl.nasa.gov/jd_cal.api?cd=" + item
        data = requests.get(url).text
        jd = data.split('"jd":"')[1].split('","')[0]
        try:
            jd2 = float(jd)
        except:
            jd = jd.split('"')[0]
            jd2 = float(jd)
        julian_dates.append(jd2)
    return abs(julian_dates[1] - julian_dates[0]) * 86400
def model_2BP(state, t, mu=int(6.674e-11 * 1.989e+30)/10**9):
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
def get_lambert_transfer(dep, arr, start_date, stop_date, rev):
    dep_ephemeris = get_object_ephemeris(dep, start_date, stop_date)
    dep_vectors = read_ephemeris(dep_ephemeris, start_date, stop_date)
    r1 = np.array([dep_vectors[0][0] * 1000, dep_vectors[1][0] * 1000, dep_vectors[2][0] * 1000])
    arr_ephemeris = get_object_ephemeris(arr, start_date, stop_date)
    arr_vectors = read_ephemeris(arr_ephemeris, start_date, stop_date)
    r2 = np.array([arr_vectors[0][-1] * 1000, arr_vectors[1][-1] * 1000, arr_vectors[2][-1] * 1000])
    print(len(dep_vectors[0]))
    print(len(arr_vectors[0]))
    tof = tof_time(start_date, stop_date)
    v1, v2= izzo2015(mu, r1, r2, tof, M=rev, prograde=True, low_path=True, maxiter=35, atol=1e-5, rtol=1e-7, full_output=False)
    dep_velocity_str = dep_ephemeris.split("$$SOE")[1].split("LT =")[0]
    arr_velocity_str = arr_ephemeris.split("$$EOE")[0].split("Z =")[-1]
    dep_vel = [float(dep_velocity_str.split("VX=")[1].split(" VY")[0]), float(dep_velocity_str.split("VY=")[1].split(" VZ")[0]), float(dep_velocity_str.split("VZ=")[1].split("\\n")[0])]
    arr_vel = [float(arr_velocity_str.split("VX=")[1].split(" VY")[0]), float(arr_velocity_str.split("VY=")[1].split(" VZ")[0]), float(arr_velocity_str.split("VZ=")[1].split("\\n")[0])]
    v1_km = np.array([x / 1000 for x in v1])
    v2_km = np.array([x / 1000 for x in v2])
    print("Departure position vector: ")
    print(r1)
    print("Departure velocity vector: ")
    print(v1)
    print("Arrival position vector: ")
    print(r2)
    print("Arrival velocity vector: ")
    print(v2)
    t1 = dep_vel - v1_km
    t2 = arr_vel - v2_km
    dep_rel = distance(0, 0, 0, t1[0], t1[1], t1[2])
    arr_rel = distance(0, 0, 0, t2[0], t2[1], t2[2])
    print("Departure delta-v: " + str(dep_rel) + " km/s")
    print("Arrival delta-v: " + str(arr_rel) + " km/s")
    return [dep_vectors, arr_vectors, v1, v2, r1, r2, t1, t2, dep_rel, arr_rel, tof]
def plot_lambert_transfer(dep_vectors, arr_vectors, v1, v2, r1, r2, tof, frame_limits, title, color_list, propagate_time, match_distance, plot=True, propagate=True):
    #two-body orbit propagation code start
    #Credit: Zack Fizell
    #Source: https://towardsdatascience.com/use-python-to-create-two-body-orbits-a68aed78099c
    t = np.linspace(0, tof, len(arr_vectors[0]))
    X_0 = r1[0] / 1000  # [km]
    Y_0 = r1[1] / 1000  # [km]
    Z_0 = r1[2] / 1000  # [km]
    VX_0 = v1[0] / 1000  # [km/s]
    VY_0 = v1[1] / 1000  # [km/s]
    VZ_0 = v1[2] / 1000  # [km/s]
    state_0 = [X_0, Y_0, Z_0, VX_0, VY_0, VZ_0]
    sol = odeint(model_2BP, state_0, t)
    X_Sat = sol[:, 0]  # X-coord [km] of satellite over time interval
    Y_Sat = sol[:, 1]  # Y-coord [km] of satellite over time interval
    Z_Sat = sol[:, 2]  # Z-coord [km] of satellite over time interval
    #- np.array([dep_vectors[0][-1], dep_vectors[1][-1], dep_vectors[2][-1]]
    #- np.array([dep_vectors[0][0], dep_vectors[1][0], dep_vectors[2][0]]
    #orbit propagation code end
    print(distance(0, 0, 0, X_Sat[-1], Y_Sat[-1], Z_Sat[-1]) / au)
    print(np.array([X_Sat[1], Y_Sat[1], Z_Sat[1]])- np.array([dep_vectors[0][1], dep_vectors[1][1], dep_vectors[2][1]]))
    print(np.array([X_Sat[-2], Y_Sat[-2], Z_Sat[-2]]) - np.array([dep_vectors[0][-2], dep_vectors[1][-2], dep_vectors[2][-2]]))
    #Get orbit intersection points with different distances
    sol_1 = odeint(model_2BP, state_0, np.linspace(0, propagate_time * 86400, propagate_time))
    X_Sat1 = sol[:, 0]  # X-coord [km] of satellite over time interval
    Y_Sat1 = sol[:, 1]  # Y-coord [km] of satellite over time interval
    Z_Sat1 = sol[:, 2]  # Z-coord [km] of satellite over time interval
    distances = []
    for item in range(len(X_Sat)):
        vectors = [X_Sat1[item], Y_Sat1[item], Z_Sat1[item]]
        distance_to_sun = distance(0, 0, 0, vectors[0], vectors[1], vectors[2])
        distances.append(abs(distance_to_sun / au - match_distance))
    print("Minimum distance at day " + str(distances.index(min(distances))) + " ; Distance from desired circle: " + str(min(distances)) + " AU")
    if plot == True:
        fig = plt.figure()
        ax = plt.axes(projection='3d')
        ax.plot3D(X_Sat, Y_Sat, Z_Sat, color_list[0])
        print(len(X_Sat))
        ax.plot3D(dep_vectors[0], dep_vectors[1], dep_vectors[2], color_list[1])
        ax.plot3D(arr_vectors[0], arr_vectors[1], arr_vectors[2], color_list[2])
        ax.set_xlim([-frame_limits * au, frame_limits * au])
        ax.set_ylim([-frame_limits * au, frame_limits * au])
        ax.set_zlim([-frame_limits * au, frame_limits * au])
        ax.set_title(title)
        plt.show()
    return [X_Sat, Y_Sat, Z_Sat]
def closest_approach(asteroid_number, coordinate_list, start_date, stop_date):
    ephemeris = get_object_ephemeris(asteroid_number, start_date, stop_date)
    #print(len(ephemeris))
    coordinate2 = read_ephemeris(ephemeris, start_date, stop_date)
    #print(len(coordinate2[0]))
    distances = []
    for item in range(len(coordinate_list[0])):
        x1, y1, z1 = coordinate_list[0][item], coordinate_list[1][item], coordinate_list[2][item]
        x2, y2, z2 = coordinate2[0][item], coordinate2[1][item], coordinate2[2][item]
        distances.append(distance(x1, y1, z1, x2, y2, z2))
    if min(distances) / au > 0.05:
        print("Minimum distance for " + str(asteroid_number) + ": " + str(min(distances) / au) + " AU")
    else:
        print("Minimum distance for " + str(asteroid_number) + ": \u001b[32;1m\u001b[1m" + str(min(distances) / au) + " AU\u001b[0m")
def get_comet_ephemeris(command, start_date, stop_date):
    #get_object_ephemeris() directly extracts a Horizons ephemeris and is not suitable for direct use in comets, where multiple ephemerides over multiple epochs are available. When researching mission options with comets, use get_comet_ephemeris() to prefilter the ephemeris instead.
    #use: get_object_ephemeris(get_comet_ephemeris(command, start_date, stop_date), start_date, stop_date)
    if "P" not in str(command):
        ephemeris = get_object_ephemeris(str(command) + "P", start_date, stop_date)
    else:
        ephemeris = get_object_ephemeris(str(command), start_date, stop_date)
    if len(ephemeris) > 10000:
        if "P" not in str(command):
            return str(command) + "P"
        else:
            return command
    else:
        lst = ephemeris.split(" ")
        int_list = []
        for item in lst:
            try:
                int_list.append(int(item))
            except:
                pass
        return max(int_list)
def get_moid(command1, command2, start_date, orbital_period):
    #Simple MOID calculation based on a very small number of points, only useful for pointing out interesting targets
    #orbital period parameter records the object with the largest period, rounded UP to the nearest integer
    url = "https://ssd-api.jpl.nasa.gov/jd_cal.api?cd=" + start_date
    data = requests.get(url).text
    jd = data.split('"jd":"')[1].split('","')[0]
    jd = float(jd)
    arrival_jd = jd + orbital_period
    url = "https://ssd-api.jpl.nasa.gov/jd_cal.api?jd=" + str(arrival_jd)
    data = requests.get(url).text
    stop_date = data.split('"cd":"')[1].split(" ")[0]
    ephemeris1 = read_ephemeris(get_object_ephemeris(command1, start_date, stop_date), start_date, stop_date)
    ephemeris2 = read_ephemeris(get_object_ephemeris(command2, start_date, stop_date), start_date, stop_date)
    distances = []
    for item in range(len(ephemeris1[0])):
        for item2 in range(len(ephemeris2[0])):
            dist = distance(ephemeris1[0][item], ephemeris1[1][item], ephemeris1[2][item], ephemeris2[0][item2], ephemeris2[1][item2], ephemeris2[2][item2])
            distances.append(dist)
    return min(distances) / au
def small_body_query(param_list, fields):
    #retrieves data from the small_body database
    #param_list: [(property, operator, value)]
    #for ranges, the value should be a string (e.g., "1-1.3")
    #e.g., [("type", "=", "TJN"), ("q", "<", "1.3")]
    #Uses the "AND" operator instead of the "OR" operator
    #fields: [field, field]
    #e.g., ["pdes", "H"]
    #example: small_body_query([("type", "=", "TJN"), ("q", "range", "4-5"), ("a", "<", 6)], ["pdes", "H"])
    strings = []
    status = []
    for item in param_list:
        #Decide on parameter
        if item[0] == "type":
            param = "sb-class"
        else:
            param = item[0]
        #Decide on operator
        if item[1] == "=":
            if "sb-" not in param:
                operator = "EQ"
            else:
                operator = "="
        elif item[1] == "!=":
            operator = "NE"
        elif item[1] == "<":
            operator = "LT"
        elif item[1] == ">":
            operator = "GT"
        elif item[1] == "range":
            operator = "RG"
        else:
            operator = item[1]
        #Decide on value of filter based on whether it is a range
        if operator == "RG":
            value = item[2].split("-")
        else:
            value = str(item[2])
        if "sb-" in param:
            custom = False
            #not contained in custom constraints
            string = param + operator + value
        else:
            custom = True
            #contained in custom constraints
            if operator != "RG":
                string = param + "|" + operator + "|" + value
            else:
                string = param + "|" + operator + "|" + value[0] + "|" + value[1]
        status.append(custom)
        strings.append(string)
    print(status)
    print(strings)
    general = "https://ssd-api.jpl.nasa.gov/sbdb_query.api?fields="
    custom = '{"AND":['
    #first deal with the fields
    fields = [str(x) + "," for x in fields]
    for item in fields:
        general += item
    general = general[0:-1] + "&"
    #then deal with the constraints
    for item in range(len(strings)):
        if status[item] == False:
            general = general + strings[item] + "&"
        else:
            custom = custom + '"' + strings[item] + '",'
    if len(custom) > 8:
        general += "sb-cdata="
        custom = custom[0:-1] + "]}"
        url = general + custom
    else:
        url = general[0:-1]
    data = requests.get(url).text
    #print(data)
    #get count
    count = data.split(":")[-1].split("}")[0]
    #print(url)
    #print(data)
    print("Qualifying objects: " + count)
    #return data
    objects = data.split('"data":[')[1].split('],"count"')[0]
    objs = objects.split("[")[1:]
    print(objs[-1])
    final_output = []
    for item in objs:
        processed = item.split("]")[0]
        values = processed.split(",")
        values = [x[1:-1] for x in values]
        final_output.append(values)
    return final_output
def number_to_command(number):
    #function that turns a number into the "command" parameter by the Horizons system
    if int(number) < 1000000:
        return "'DES=" + str(2000000 + int(number)) + "'"
    else:
        return "'DES=" + str(number) + "'"
def get_alt_des(des):
    #get the primary designation (e.g., 433) and alternate designations (e.g., 1956 PC) of an object
    url = "https://ssd-api.jpl.nasa.gov/sbdb.api?des=" + str(des) + "&alt-des=1"
    data = requests.get(url).text
    if '"pri":"' in data:
        prim_des = data.split('pri":"')[1].split('"')[0]
    else:
        prim_des = []
    designations = data.split('des":"')[1:]
    alt_des = [x.split('"')[0] for x in designations]
    if len(prim_des) != 0:
        return [prim_des] + alt_des
    else:
        return alt_des
def comet_designation(des):
    #determine whether a designation is cometary
    #if it returns true, the designation is asteroidal; otherwise, it's cometary.
    #for example, 2013 A1 returns false, while 2014 UN271 returns true.
    #not suitable for use for designations with the expression of (comet)/(name) (e.g., 167P/CINEOS), or primary designations (e.g., 433). It will return an IndexError.
    number = des.split(" ")[1]
    uppercase = list("QWERTYUIOPASDFGHJKLZXCVBNM")
    return number[1] in uppercase
def plot_data(data, color_list, frame_limits, title, image_name):
    fig = plt.figure()
    ax = plt.axes(projection = '3d')
    ax.set_xlim([-frame_limits * au, frame_limits * au])
    ax.set_ylim([-frame_limits * au, frame_limits * au])
    ax.set_zlim([-frame_limits * au, frame_limits * au])
    color_count = 0
    for o in data:
        ax.plot3D(o[0], o[1], o[2], color_list[color_count])
        ax.scatter3D(o[0][-1], o[1][-1], o[2][-1], s=8, linewidth=1, color=color_list[color_count])
        color_count += 1
    ax.set_title(title)
    #Save each image
    plt.savefig(image_name)
    plt.close()
def plot_2d(data, color_list, frame_limits, title, image_name):
    fig = plt.figure()
    ax = plt.axes()
    ax.set_xlim([-frame_limits * au, frame_limits * au])
    ax.set_ylim([-frame_limits * au, frame_limits * au])
    ax.set_aspect('equal')
    color_count = 0
    for o in data:
        ax.plot(o[0], o[1], color_list[color_count])
        ax.scatter(o[0][-1], o[1][-1], s=8, linewidth=1, color=color_list[color_count])
        color_count += 1
    ax.set_title(title)
    plt.savefig(image_name)
    plt.close()
    
