from plot_ephemeris import *
dep = 3
arr = 5
start_date = "2027-Oct-27"
stop_date = "2030-Jan-02"
rev = 0
r = get_lambert_transfer(dep, arr, start_date, stop_date, rev)
frame_limits = 1.5
title = "Launch Window Simulator"
color_list = ['magenta', 'blue', 'green']
#plot_lambert_transfer(r[0], r[1], r[2], r[3], r[4], r[5], r[-1], frame_limits, title)
solution = plot_lambert_transfer(r[0], r[1], r[2], r[3], r[4], r[5], r[-1], frame_limits, title, color_list, 1, 1, plot=True, propagate=True)
data = [solution, r[0], r[1]]
print("Trajectory ephemeris length")
#print(len(solution[0]))
image_name = "window.gif"
divisor = 2
data_to_gif(data, divisor, color_list, title, image_name, frame_limits)
print("Closest")
#lst = ['2061', '2101', '2201', '3352', '3361', '3757', '3908', '4015', '4179', '4486', '4503', '4581', '4660', '5189', '5604', '5626', '5797', '6037', '6063', '6178', '6239', '6489', '7358', '7753', '8014', '8034', '8709', '10145', '10302', '10860', '11054', '11284', '14827', '16064', '18106', '18109', '18736', '19356', '19764', '22753', '25143', '26817', '35396', '40329', '41429', '52760', '54509', '65679', '65717', '65733', '65803', '65909', '68278', '85182', '85490', '85585', '85640', '85867', '88254', '89136', '96631', '98943', '99942', '100085', '101869', '136564', '136617', '136618', '137044', '137911', '138404', '138911', '139056', '140039', '140158', '141018', '141053', '141432', '141495', '141593', '143404', '143487', '144898', '152560', '152664', '152671', '152679', '152685', '152754', '152895', '153814', '153958', '154007', '154019', '154244', '154590', '154715', '155336', '155338', '159495', '162000', '162011', '162058', '162120', '162168', '162183', '162361', '162416', '162422', '162695', '162998', '163000', '163364', '163373', '163667', '163697', '164184', '164202', '164211', '164215', '164294', '170086', '172678', '173664', '175189', '175706', '177049', '178601', '179806', '184266', '190161', '190166', '190208', '194006', '198752', '199145', '199801']
for item in range(1, 1000):
    try:
        closest_approach(item, solution, start_date, stop_date)
    except ValueError:
        pass
