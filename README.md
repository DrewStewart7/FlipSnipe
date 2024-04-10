# FlipSnipe
Roblox Third Party Market Item Sniper Bot

Introduction 

Roblox is a game with many games inside of it. Think of it as almost like a metaverse. A user can create games and other users can play these games from within the Roblox platform. There are certain items in Roblox that can be traded amongst users. These are items like hats, faces, hair, etc for your avatar. These items stay with you in every Roblox game across the platform.

Where this program comes into play:

FlipSnipe will buy these Roblox items that are being sold for real money on a third party site called RBXFlip.com (website is offline now due to Roblox trading changes). Item prices would range from $5-$20,000.

It will only buy the items that are being sold at a large discount. It is because of this that FlipSnipe must be as efficient as possible. There was very much competition in this market amongst bot developers like myself. Everyone wants to snipe the good items, but only those with the fastest bots are able to.

FlipSnipe used something called Websockets. Instead of having to repetedly ask for information about the market, websockets are kind of like a constant bridge between server and client. The server would basically tell the program when a new item was listed, intead of the other way around(program asks if an item was listed). This functionality also removes the need for proxies or any anti-ratelimiting measure because we are doing nothing more than a regular user looking at the market would do.

Furthermore, FlipSnipe had the capability to snipe multiple items at once. This would happen if a user listed all of the discounted items on the market at the same time. Flipsnipe would only send 1 http request to buy all the items (up to 
5 at a time), instead of sending 1 for each item individually.

So, did it work?

Yes. It did. This program would "snipe"(buy items at a discount) 100-200 times per day. $0.50-$100 profit would be earned with each snipe, with most of them being closer to the lower bound. High profit snipes were the most difficult to get because of the immense competition.

Feel free to take a look at my work that was done. Keep in mind that it was always intended as personal-use only. The code is far from production-quality and is mising important things like comments and pretty line spacing.

Earnings

FlipSnipe was able to generate about $1,500 profit per month, every month, until Roblox changed and made this impossible...


Thank you for taking the time to learn about my program :)

Some pictures of snipe information:

![image](https://github.com/DrewStewart7/FlipSnipe/assets/114938193/4a4ce005-e4eb-4a1a-96cb-410df2070789)

![image](https://github.com/DrewStewart7/FlipSnipe/assets/114938193/bec14c72-e49d-4bfc-8fcd-1b5e7b6b9e8a)

