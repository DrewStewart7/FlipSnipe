from websocket import create_connection
import json, os,subprocess
import requests, time, json, random, colorama
from colorama import Fore, Back, Style
from colorama import init
import discord

init()
import discord, requests, threading, os, subprocess
from discord import Webhook, SyncWebhook, Embed
with open("config.json") as jsonfile:
    config = json.load(jsonfile)
webhookurl = config["webhook"]
webhook = SyncWebhook.from_url(webhookurl)
rate = config["smallmaxrate"]
srate = config["smallsellrate"]
resell = config["auto-resell"]
token = config["token"]
vbuy = config["valuemaxrate"]
vsell = config["valuesellrate"]
rbuy = config["raremaxrate"]
rsell = config["raresellrate"]
smallurl = "https://api.rbxflip.com/roblox/items/smalls"
itemsurl = "https://api.rbxflip.com/roblox/items"
loginurl = "https://api.rbxflip.com/auth/login"
posturl = "https://api.rbxflip.com/roblox/shop/list"
burl = "https://api.rbxflip.com/roblox/shop/buy"
balurl = "https://api.rbxflip.com/wallet/balance"
useCustomRates = False
customrates = {}
with open('customrates.json', 'r') as openfile:
    customrates = json.load(openfile)
# Copy the web brower header and input as a dictionary
headers = json.dumps({
    'Accept-Encoding':
    'gzip, deflate, br',
    'Accept-Language':
    'en-GB,en-US;q=0.9,en;q=0.8',
    'Cache-Control':
    'no-cache',
    'Connection':
    'keep-alive, Upgrade',
    'Host':
    'api.rbxflip.com',
    'Origin':
    'https://rbxflip.com',
    'Pragma':
    'no-cache',
    'Sec-WebSocket-Extensions':
    'permessage-deflate; client_max_window_bits',
    'Sec-WebSocket-Key':
    '77I/dnvYE3ybsw+sMJfAzg==',
    'Sec-WebSocket-Version':
    '13',
    'Upgrade':
    'websocket',
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
})
s = requests.session()

s.headers["x-socket-id"] = "2HLGb98oZmCSbi0UBtC-"
s.headers["content-type"] = "application/json"
count = 0
atoken = token[0].split(" ")[1]

def startratechange():
    #exec(open('FSMain.py').read())
    print("")

def startresell():
    exec(open('resell.py').read())


def startbot():
    exec(open('bot.py').read())


def startdanny():
    exec(open('values.py').read())
# starts 

def runprog():
    try:
        while True:
            try:

                def restartws():
                    # Launch the connection to the server.
                    # 
                    ws = create_connection(
                        'wss://api.rbxflip.com/socket.io/?EIO=4&transport=websocket',
                        headers=headers,
                        on_close=restartws,
                        on_error=restartws)

                    # Perform the handshake.
                    ws.send("40" + json.dumps({"accessToken": atoken}))
                    # restarts the 

                # Launch the connection to the server.
                ws = create_connection(
                    'wss://api.rbxflip.com/socket.io/?EIO=4&transport=websocket',
                    headers=headers,
                    on_close=restartws,
                    on_error=restartws)

                # Perform the handshake.

                ws.send("40" + json.dumps({"accessToken": atoken}))

                def buy(buylist, profit, rates, names):
                    random.seed()
                    s.headers["authorization"] = random.choice(token)
                    #s.headers["authorization"] = token[0]
                    aNum = token.index(s.headers["authorization"])
                    buy1 = s.post(burl, json=buylist)
                    print("Attempting to buy")
                    if (buy1.status_code == 201 and buy1.json()["ok"] == True):
                        print(Fore.GREEN + "Successful purchase")
                        bal = s.get(balurl).json()["balance"]
                        message = ""
                        embed = discord.Embed(title="FLIPSNIPE V2.3 SNIPE",
                                              description=":gun:",
                                              color=2218752)
                        for q in buylist:
                            uid = q["userAssetId"]
                            price = q["expectedPrice"]
                            message += f"NAME: {names[uid]}\nUAID: {uid}\nPRICE: {price}\nRATE: {rates[uid]}\n\n"
                            dataz = {
                                "content":"<https://www.rolimons.com/uaid/" +
                                str(q["userAssetId"]) + ">"
                            }
                            senduid = requests.post(config["webhook"],json=dataz)                          
                        messagez = f"Total Profit: ${profit}\nACCOUNT: {str(aNum)}\nNEW BALANCE: ${bal}\nITEMS:\n" + message
                        embed.add_field(name="Snipe information:",
                                        value=messagez)
                        webhook.send(embed=embed)
                        print("Sent webhook")
                    elif buy1.status_code == 400:
                        print(Fore.RED + buy1.text)
                        buy1 = s.post(burl, json=buylist)
                        print(Fore.WHITE + "ATTEMPT 2: " + buy1.text)
                        if (buy1.status_code == 201
                                and buy1.json()["ok"] == True):
                            print(Fore.GREEN + "Successful purchase")
                            bal = s.get(balurl).json()["balance"]
                            message = ""
                            embed = discord.Embed(
                                title="FLIPSNIPE V2.3 POSSIBLE SNIPE",
                                description=":gun:",
                                color=16705372)
                            for q in buylist:
                                uid = q["userAssetId"]
                                price = q["expectedPrice"]
                                message += f"NAME: {names[uid]}\nUAID: {uid}\nPRICE: {price}\nRATE: {rates[uid]}\n\n"
                            messagez = f"Total Profit: ${profit}\nNEW BALANCE: ${bal}\nITEMS:\n" + message
                            embed.add_field(name="Snipe information:",
                                            value=messagez)
                            webhook.send(embed=embed)
                            print("Sent webhook")
                    else:
                        print(Fore.RED + "Purchase failed")
                        print(buy1.text)
                        print(Fore.LIGHTRED_EX + buylist)

                while True:
                    global count
                    try:
                        result = ws.recv()
                        count += 1
                        if result == "2":
                            ws.send("3")
                        elif result == "Connection to remote host was lost.":
                            restartws()
                        else:
                            try:
                                profit = 0
                                buylist = []
                                comfig = {}
                                if ("shop.items.deposited" in result):
                                    with open("config.json") as jsonfile:
                                        config = json.load(jsonfile)
                                    rate = config["smallmaxrate"]
                                    srate = config["smallsellrate"]
                                    resell = config["auto-resell"]
                                    token = config["token"]
                                    vbuy = config["valuemaxrate"]
                                    vsell = config["valuesellrate"]
                                    result = result.replace("42", "", 1)
                                    result = json.loads(result)
                                    rates = {}
                                    names = {}
                                    result = result[1]
                                    for item in result:
                                        price = item["price"]
                                        if price >= 5:
                                            print(Fore.BLUE + "Item deposited")
                                            print(Fore.BLUE + "Found item for",
                                                item["rate"])

                                            if (useCustomRates == True):
                                                try:

                                                    crate = customrates[str(
                                                        item["userAsset"]["asset"]
                                                        ["assetId"])]
                                                    if (item["rate"] <= crate[0]):
                                                        data = {
                                                            "expectedPrice": price,
                                                            "userAssetId":
                                                            item["id"],
                                                            "userId":
                                                            item["sellerId"]
                                                        }
                                                        profit += ((item["price"] /
                                                                    item["rate"]) *
                                                                crate[1] -
                                                                item["price"])
                                                        buylist.append(data)
                                                        uid = item["id"]
                                                        rates[uid] = item["rate"]
                                                        names[uid] = item[
                                                            'userAsset']["asset"][
                                                                "name"]
                                                        continue

                                                except:
                                                    print(
                                                        Fore.WHITE +
                                                        "Item does not have custom rate"
                                                    )

                                            if (item["rate"] < rate):
                                                data = {
                                                    "expectedPrice": price,
                                                    "userAssetId": item["id"],
                                                    "userId": item["sellerId"]
                                                }
                                                profit += ((item["price"] /
                                                            item["rate"]) * srate -
                                                        item["price"])
                                                buylist.append(data)
                                                uid = item["id"]
                                                rates[uid] = item["rate"]
                                                names[uid] = item['userAsset'][
                                                    "asset"]["name"]

                                            elif (item["rate"] < vbuy):
                                                with open('danny.json',
                                                        'r') as openfile:
                                                    danny = json.load(openfile)
                                                aid = str(item["userAsset"]
                                                        ["asset"]["assetId"])

                                                if (danny[aid]["value"] != None and
                                                        danny[aid]["demandScore"]
                                                        >= 5):
                                                    print(
                                                        Fore.LIGHTGREEN_EX +
                                                        "Valued item: "
                                                        + danny[aid]["name"])
                                                    data = {
                                                        "expectedPrice": price,
                                                        "userAssetId": item["id"],
                                                        "userId": item["sellerId"]
                                                    }
                                                    profit += (
                                                        (item["price"] /
                                                        item["rate"]) * vsell -
                                                        item["price"])
                                                    buylist.append(data)
                                                    uid = item["id"]
                                                    rates[uid] = item["rate"]
                                                    names[uid] = item['userAsset'][
                                                        "asset"]["name"]

                                                else:

                                                    print(
                                                        Fore.LIGHTMAGENTA_EX +
                                                        "Unvalued item: "
                                                        + danny[aid]["name"])

                                            if (len(buylist) == 4):
                                                break

                                    if (len(buylist) != 0):
                                        buy(buylist, profit, rates, names)

                                elif ("shop.item.updated" in result):
                                    result = result.replace("42", "", 1)
                                    result = json.loads(result)
                                    rates = {}
                                    names = {}
                                    item = result[1]
                                    price = item["newPrice"]
                                    if price >= 5:
                                        print(Fore.YELLOW + "Item rate change")
                                        print(Fore.YELLOW + f"Found item for",
                                            item["newRate"])
                                        uid = item["userAssetId"]
                                        shop = requests.get(
                                            "https://api.rbxflip.com/roblox/shop"
                                        ).json()
                                        itemId = ""
                                        done = False
                                        for x in shop:
                                            if (x["id"] == uid):
                                                itemId = str(x["userAsset"]
                                                            ["asset"]["assetId"])
                                                if (useCustomRates == True):
                                                    try:
                                                        crate = customrates[itemId]
                                                        if (item["newRate"] <=
                                                                crate[0]):
                                                            data = {
                                                                "expectedPrice":
                                                                price,
                                                                "userAssetId": uid,
                                                                "userId":
                                                                x["sellerId"]
                                                            }
                                                            profit += (
                                                                (price /
                                                                item["newRate"]) *
                                                                crate[1] - price)
                                                            names[uid] = x[
                                                                'userAsset'][
                                                                    "asset"][
                                                                        "name"]
                                                            rates[uid] = item[
                                                                "newRate"]
                                                            buylist.append(data)
                                                            buy(
                                                                buylist, profit,
                                                                rates, names)
                                                            done = True
                                                    except:
                                                        print(
                                                            Fore.WHITE +
                                                            "Item does not have custom rate"
                                                        )
                                                    break
                                        if (item["newRate"] < rate
                                                and done == False):
                                            if (x["id"] == uid):
                                                itemId = str(x["userAsset"]
                                                            ["asset"]["assetId"])
                                                with open('danny.json',
                                                        'r') as openfile:
                                                    danny = json.load(openfile)
                                                if (price < 7):
                                                    data = {
                                                        "expectedPrice": price,
                                                        "userAssetId": uid,
                                                        "userId": x["sellerId"]
                                                    }
                                                    profit += (
                                                        (price / item["newRate"]) *
                                                        srate - price)
                                                    names[uid] = x['userAsset'][
                                                        "asset"]["name"]
                                                    rates[uid] = item["newRate"]
                                                    buylist.append(data)
                                                    buy(buylist, profit, rates,
                                                        names)
                                                elif (danny[itemId]["value"] !=
                                                    None):
                                                    data = {
                                                        "expectedPrice": price,
                                                        "userAssetId": uid,
                                                        "userId": x["sellerId"]
                                                    }
                                                    profit += (
                                                        (price / item["newRate"]) *
                                                        vsell - price)
                                                    buylist.append(data)
                                                    rates[uid] = item["newRate"]
                                                    names[uid] = x['userAsset'][
                                                        "asset"]["name"]
                                                    buy(buylist, profit, rates,
                                                        names)
                                                    done = True
                                        elif (item["newRate"] < vbuy
                                            and done == False):
                                            with open('danny.json',
                                                    'r') as openfile:
                                                danny = json.load(openfile)
                                            if (danny[itemId]["value"] != None and
                                                    danny[itemId]["demandScore"] >=
                                                    5):
                                                data = {
                                                    "expectedPrice": price,
                                                    "userAssetId": uid,
                                                    "userId": x["sellerId"]
                                                }
                                                profit += (
                                                    (price / item["newRate"]) *
                                                    vsell - price)
                                                buylist.append(data)
                                                rates[uid] = item["newRate"]
                                                names[uid] = x['userAsset'][
                                                    "asset"]["name"]
                                                buy(buylist, profit, rates, names)
                                                done = True

                            except Exception as e:
                                print(e)
                    except Exception as e:
                        print(e)
                        runprog()
            except Exception as e:
                print(e)
                runprog()
    except Exception as e:
        print(e)
        runprog()


t1 = threading.Thread(target=startresell)
t1.start()
t1 = threading.Thread(target=startdanny)
t1.start()
t1 = threading.Thread(target=startratechange)
t1.start()
while True:
    try:
        runprog()
    except Exception as e:
        runprog()
        print(e)
