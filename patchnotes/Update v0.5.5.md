# Update v0.5.5
## General
### Properly implemented /help command.

## Paladins
### General
Increased the time before buttons timeout from 2 minutes to 5 minutes.
- (It may bug out sometimes, will keep an eye out for this)

### `/paladins calculate`
New command!
Allows you to calculate the diminishing returns for multiple values.

### `/paladins stats champion`
New command!
This allows you to view champion statistics for different things.
You can currently view:
1. Win/Pick/Ban Count & rates
2. Talent win/pick rates
3. Skins pick rates
You can narrow down stats returned with different options.
Current options are: Champion, Role, Map, Rank and Region

### `/paladins match`
**Changes:**
- Added the 2 new anniversary update bans. (Already in live bot)
**Fixes:**
- Updated the bans locations to be cleaner.
- **FINALLY (:D)** fixed the issue where it would display "Winning Team: X" when a player ID and match ID are both provided.

### `/paladins champions`
**Fixes**:
- Fixed an issue where the role sort "All" would not work as the first input.

### `/paladins cards` and `/paladins loadout`
**Fixes:**:
- Reduced the character length per line to 24 because 25 characters could cause slight clipping.

## Genshin
### `/genshin profile info`
**Changes**:
- Temporarily removed the emotes for Expeditions due to Hoyolab changes breaking things.

### `/genshin profile stats`
**Fixes:**
- Fixed an issue that caused chest count to display twice.

## Star Rail
### `/starrail profile info`
**Fixes:**
- Fixed an issue with the command failing if you had no expeditions active.

## *Few miscellaneous fixes not big enough to be listed here.*
