import json, os
import requests, time, json, random, colorama
from colorama import Fore, Back, Style
from colorama import init

init()
with open("config.json") as jsonfile:
    config = json.load(jsonfile)
rate = config["smallmaxrate"]
srate = config["smallsellrate"]
resell = config["auto-resell"]
tokens = config["token"]
vbuy = config["valuemaxrate"]
vsell = config["valuesellrate"]
smallurl = "https://api.rbxflip.com/roblox/items/smalls"
itemsurl = "https://api.rbxflip.com/roblox/items"
loginurl = "https://api.rbxflip.com/auth/login"
posturl = "https://api.rbxflip.com/roblox/shop/list"
customrates = {}
with open('customrates.json', 'r') as openfile:
    customrates = json.load(openfile)


def sellall():
    useCRate = False
    if (resell == True):
        while True:
            try:

                tokens = config["token"]
                for token in tokens:
                    print(Fore.CYAN + "ATTEMPTING TO PUT ALL ON SALE")
                    s = requests.session()
                    s.headers["authorization"] = token
                    getsmalls = s.get(smallurl)
                    getsmalls = getsmalls.json()
                    smalls = []
                    itemstosell = []
                    bigitems = []
                    items = []
                    for x in range(len(getsmalls) - 1):
                        smalls.append(getsmalls[x]["userAssetId"])
                    getitems = s.get(itemsurl).json()
                    for item in getitems:
                        if (item["asset"]["rap"] > 1000):
                            try:
                                if (item["asset"]["isProjected"] == False
                                        and item["asset"]["value"] < 25000):
                                    print(Fore.CYAN, "Passed vibe check0")
                                    items.append(item["userAssetId"])
                            except:

                                items.append(item["userAssetId"])
                    x = 0
                    print(items)
                    print(smalls)
                    for item in items:
                        issmall = False
                        for small in smalls:
                            if small == item:
                                issmall = True
                        if issmall == False:
                            itemstosell.append(item)
                        x += 1
                    datas = []
                    i = 0
                    items = s.get("https://api.rbxflip.com/roblox/items")
                    items = items.json()
                    for x in itemstosell:
                        if i == 5:
                            break
                        for item in items:
                            if (item["userAssetId"] == x):
                                with open('danny.json', 'r') as openfile:
                                    danny = json.load(openfile)
                                aid = str(item["asset"]["assetId"])
                                if (useCRate == True):
                                    try:
                                        crate = customrates[aid]
                                        datas.append({
                                            "userAssetId": x,
                                            "rate": crate[1]
                                        })
                                        print("Custom valued item added")
                                        continue
                                    except:
                                        print(
                                            "Item does not have custom value")
                                if (danny[aid]["value"] != None):
                                    datas.append({
                                        "userAssetId": x,
                                        "rate": vsell
                                    })
                                else:
                                    datas.append({
                                        "userAssetId": x,
                                        "rate": srate
                                    })

                        i += 1

                    print(Fore.CYAN + str(datas))
                    selling = s.post(posturl, json=datas)
                    print(Fore.CYAN + selling.text)
                    if selling.status_code == 201:
                        print(Fore.GREEN +
                              "SUCCESSFULLY LISTED INVENTORY ITEM(S)")
                time.sleep(75)
            except Exception as e:
                print(Fore.RED, e)


sellall()
