from plot_ephemeris import *
comets = small_body_query([("sb-kind", "=", "c")], ["pdes"])
knowns = []
for item in comets:
    pdes = item[0]
    if "-" in pdes:
        if pdes.split("-")[0] not in knowns:
            comet = pdes.split("-")[0]
            print(comet)
            knowns.append(comet)
print(knowns)
