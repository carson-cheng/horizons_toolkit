from plot_ephemeris import *
results = small_body_query([("sb-kind", "=", "a"), ("sb-ns", "=", "n"), ("sb-group", "=", "neo"), ("spec_B", "!=", "C")], ["pdes", "H"])
knowns = []
results = sorted(results, key=lambda x:float(x[0]))
for item in results:
    print(item)
