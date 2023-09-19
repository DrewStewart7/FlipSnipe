import requests,time,json

while True:
    try:
        danny = requests.get("https://api.danny.ink/api/itemdetails")
        if danny.status_code == 200:
            danny = json.loads(danny.text)
            danny = json.dumps(danny)
            with open("danny.json", "w") as outfile:
                outfile.write(danny)
            print("Danny updated")
        else:
            print("Danny down :(")
        time.sleep(120)
    except:
        print("Danny down :(")