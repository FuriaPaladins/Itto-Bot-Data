# Update v0.5.1
## General
- Cleaned up presentation of certain commands

## Paladins
- Added Champion autocomplete to `champion` parameters in commands. 
 - Note: Will still work with champion aliases (EG: "Betty"), it simply displays autocomplete for ease of use.

### `/paladins match`
**Fixes:**
- Fixed an issue where you couldn't get a match by ID if you don't have a paladins account linked
- Re-added the "Toggle Player Names" button. (It was broken last update)

### `/paladins champions`
**Changes**:
- Centred "Time" in the champions list. (Very big change, trust)
- Added `average level` to champions list.

**Fixes**:
- Typing in an incorrect champion will now return an error much faster.
- Renamed "games" in the list to "matches".
- Fixed Betty's champion icon not displaying

### `/paladins history`
**Changes:**
- Shows the class pick rate at the top of the embed.
- Now does not have the dropdown. You now specify the things you want to see in the command itself. 
- 2 new parameters added for the command:
	- Champion: now gets all matches for a specific champion
	- Count: narrows down how many results you'd like to get

**Fixes:**
- Should be faster and cleaner by no longer deleting and re-sending messages when user changes what to view.
- Typing in an incorrect champion will now return an error much faster.

### `/paladins friends`
You can now view your friends lists with a new command!
You can view pages, search for friends, and sort by their IDs, names or platforms.

### `/paladins loadouts`
**Changes**
- Now has support for customising your champion images! Just click the gear icon that shows up when you search for your own loadouts.

**Fixes**
- Fixed Mal'Damba's loadouts not displaying due to a typo
- Fixed Kasumi's card arts being wrong.

### `/link paladins`
**Changes**
Each paladins account can now only be linked to one discord user.
Rewritten the command so it now looks and works slightly different. This should improve how easy it is to use

## Genshin Impact
### `/genshin profile info`
**Changes**
- Added a display for when the daily, weekly and abyss resets happen.

**Fixes:**
- Now displays less information if a user hasn't gotten that feature yet/has nothing there. 
	- Transformer, Realm Currency and Expeditions will now not display if the user does not have any of them.

### `/link hoyolab`
**Changes:**
- Now displays the user's in-game nickname in the dropdown menu

**Fixes:**
- Fixed an issue where the "Set Active" button would still be click-able if you were to add a new account

## Honkai Star Rail & Genshin Impact
- Fixed some of the daily redemption breaking. (This thing really really does not like cooperating)