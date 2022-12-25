# Horizons Toolkit
This repository contains a toolkit that uses the Horizons system to:
  1. Obtain ephemerides and plot the trajectories of solar system bodies
  2. Calculate interplanetary transfer trajectories based on a Lambert solver
  
Code credits:
  1. Two-body orbit propagator: Zack Fizell (source: https://towardsdatascience.com/use-python-to-create-two-body-orbits-a68aed78099c)
  2. Lambert solver: Dario Izzo (source: https://arxiv.org/abs/1403.2705, source code obtained through lamberthub (https://github.com/jorgepiloto/lamberthub))

## How to Use This Repository
  1. Clone it (git clone https://github.com/carson-cheng/horizons_toolkit)
  2. Refer to the input files:
    Use perseverance.py and galileo.py for plotting existing trajectories
    Use launch_window.py window_1.py window_2.py to plot Lambert transfer trajectories
    Use window_3.py to plot multiple Lambert transfer trajectories
  3. Modify these files to create the trajectories!
 
 ## How to Read the Outputs
When you create a Lambert transfer trajectory in this repository, you will see a bunch of outputs on the terminal. For example, when you run window_2.py for a direct transfer to Jupiter, this shows up:

1137  
1137  
Departure position vector:   
[ 1.21926325e+11 -8.91305230e+10  3.32822387e+07]  
Departure velocity vector:   
[19849.98566809 32858.04947671 -2808.03025697]  
Arrival position vector:   
[-7.56475422e+11  2.84314833e+11  1.57518470e+10]  
Arrival velocity vector:   
[-1656.6154075  -7012.12537839   487.9579752 ]  
Departure delta-v: 9.689941496155635 km/s  
Arrival delta-v: 5.562601673161371 km/s  
5.407993278078477  
[ 252241.91948563  760762.44516042 -242467.22702925]
[-9.04045211e+08  3.11062501e+08  1.52776325e+07]  
Minimum distance at day 10 ; Distance from desired circle: 0.00011312994870160686 AU  
1127

The first two lines contain the same number (time of travel); this variable is printed twice.
The following eight lines contain the departure and arrival position and velocity vectors, as marked in the output. Note that the speed is heliocentric instead of relative to the object.
The departure and arrival delta-v is the relative velocity of the trajectory from the departure object at departure, and from the arrival object at arrival, respectively
The following line contains the heliocentric distance of the arrival object at arrival point
The two following lines contain the relative position of the trajectory of the object from departure on the second day and the second-last day of the trajectory, respectively
The second-last line contains the data on the minimum distance of the trajectory from a specific heliocentric distance
The last line contains the time from launch to the end of orbit propagation. Note that it is normally longer than time of travel, but it can also be shorter (as in this case)

When the trajectory is being generated into a gif file, positive integers are printed in ascending order. This records a frame being created and saved. Note that you should not generate more than 240 frames in a single file, or an error saying that too many files are open may appear.

After the trajectory is generated, you may see something like this:

Minimum distance for 'DES=2000001': 2.1415064661950716 AU  
Minimum distance for 'DES=2000002': 2.963438902455112 AU  
Minimum distance for 'DES=2000003': 3.8000730384617305 AU  
Minimum distance for 'DES=2000004': 3.272232352705707 AU  
Minimum distance for 'DES=2000005': 3.0640074411790423 AU  
Minimum distance for 'DES=2000006': 2.6689292623825627 AU  

This is the closest_approach function being called repeatedly in a for-loop. This function help seek secondary targets by looking at close approaches to asteroids and seeing if it is close enough to maybe redirect the trajectory towards the asteroid. 
 
 ## Notes
 
 Note that all transfer trajectories are computed and plotted using two-body methods. Thus, it may become inaccurate over years or decades. Thus, for scientifically rigorous results and studies, perturbations should be included in addition to the nominal two-body trajectory.
