import requests
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
'''for item in range(1, 453):
    des = str(item) + "P"
    alt_des = get_alt_des(des)
    for name in alt_des:
        if len(name.split(" ")) > 1:
            if comet_designation(name) == True:
                print(name)
    #print(item)'''
'''for item in range(1, 100000):
    alt_des = get_alt_des(item)
    if len(alt_des) > 8:
        print(item)'''
for item in range(1, 10000):
    alt_des = get_alt_des(item)
    for name in alt_des:
        if len(name.split(" ")) > 1 and name[0] != "A":
            if int(name[:3]) > 200:
                print(item)
