# General
- Removed the random coloured strip on the left side of embeds. (Purely cosmetic but it just felt out of place for some things)
# Paladins
### /current
- Now displays the platform for each user in the form of an emote

### /match
- Fixed up a lot of annoying (and kinda small) transparency issues
	- Some talent icons will be much easier to see now thanks to this!
- Some minor display changes (Background to champ icon noteably)
- Completely rewritten backend.
	- The command will now be slightly faster, but in return, getting the "loadout/items" image will take slightly longer when first running it. (If you swap between both images it'll be just as fast, it's just the initial press of the button will be slightly slower)
	- Now has support for customisation! More about customisation will be below

#### /match customisation
#### A new system that allows customising your match image
- You can type `/paladins match customisation:True` to display a new menu which lets you change the colours of your match images! You can use google's colour picker https://g.co/kgs/XLBc82 to get your colour codes. 
- You get a live display of how your match image will roughly look, as you change your colours.

# Genshin
#### Big linking change!
- To accomodate for Honkai Star Rail, Genshin linking has been changed to **Hoyolab linking**. You can now link multiple accounts to your discord in case you have alts, etc. 
- If you had a Genshin account linked prior to this change, it will be carried over when the bot updates.
Note: Honkai Star Rail doesn't have any public-accessible API things yet. You cannot view your characters, Simulated Universe, etc. When this will be added, I will be sure to add it to the bot too. For now, your hoyolab link will still show your genshin accounts, but if you have a honkai account linked, it will redeem your daily rewards for that too.

# Honkai Star Rail
### /redeem
- You can now redeem Honkai Star Rail codes directly through the bot.
Note: Requires a Hoyolab acocunt linked.

# Announcements
- Fixed announcements being sent/ran twice in succession.
- You can now get Honkai Star Rail daily redemption announcements 
- Typing in just `/announcements` without a `type` now shows all the announcements the bot has, as well as the next time it will be ran.
## Now redeems all rewards for Honkai Star Rail and Genshin Impact. If the user is signed up to notify, it will notify the user of all rewards redeemed. (Daily redemption happens at 6pm GMT)