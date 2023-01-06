import requests
for item in range(1, 100000):
    command = str(item)
    url = "https://ssd-api.jpl.nasa.gov/cad.api?des=" + command + "&date-min=1900-01-01&date-max=2100-01-01&dist-max=0.075&body=Mars"
    approaches = requests.get(url).text
    count = approaches.split('count":"')[1].split('"')[0]
    if int(count) > 0:
        print("\u001b[32;1m\u001b[1m" + command + "\u001b[0m" + " will approach Mars.")
    else:
        print(item)
