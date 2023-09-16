# Update v0.6.0

## Rewritten a *lot* of the code.
### *This means that everything should be more coherent, but some new bugs may occur as a result*
## Random Changes
- Bot will now cycle between statuses
 - Displays unique status when the bot is collecting Paladins match stats
 - 2 new statuses, showing "Playing {Apex/Paladins} with {Player Count} Steam players"
- **Revamped the `/help` command**
## Paladins
### *Paladins API is still broken with some new things in the Omen update. The `/paladins stats` command is disabled currently due to this as I'm unable to collect more match stats.*
### General Changes:
- Added Omen's assets
 - *20% chance of getting the early "Goofy Omen" icon instead of the normal Omen icon in places

- Champion aliases (such as "IOYA", "Tib", "Seven") will now work for all `champion` fields.
- Reduced the amount of autocomplete options that display at any one time from 10 -> 5 to reduce the amount of space it takes up on screen.

- Getting data on your, or any other discord user's linked accounts, will now be faster by caching users.
 - *(Refreshes every 3 hours, so if you change your name it won't instantly be updated, but everything will work the same)*
- Using a command on a console player no longer always requires an ID to work. It will now search for that specific player. 
 - Note: Can still potentially throw an error, but will now work more often and means there should be no need for a `/search` command
- Players with valid discord formatting in their names will no longer display like*this*.
### `/paladins match`
**Fixes**  
- Added icons for the Siege Remixed maps
- Fixed icons for certain payload maps
- Added proper error message for Hirez api being broken at the moment  
**Changes**  
- Removed skin image from the secondary image as some skins are missing official icons and maintaining this system was very tedious.
- Reworked how match image customisation works.
 - You can now choose between CSS colour names as well as HEX codes.
 - Added "Reset All" button
 - Other users can no longer edit your image if they have access to the customisation buttons.
### `/paladins loadouts` & `/paladins cards`
**Changes**  
- Added a new "Toggle Image" button that toggles between the champion background & title card and just the loadout cards.
**Fixes**  
- Fixed numerous issues with Mal'Damba and other selections
- Fixed issue where clicking "Generate" for `/paladins cards` without selecting a card first would cause an error
- Fixed autocomplete not working for the `champions` field in `/paladins cards`
- Fixed loadouts not working for Sha Lin and Vii.
- Fixed how the background image is cropped so that the whole art is showcased.
### `/paladins current`
**Changes**  
- Changed how it looks with multiple users in the command to make it easier to identify users by ID
- Properly implemented faster query for inputting multiple player ID's.
 - The bot will now add a note when multiple names are provided rather than ID's.

### `/paladins champions`
**Changes**  
- Added "Sorting by {}" notifier the top.
## Genshin & Star Rail
- Renamed `profile` to `account` to not conflict with `/paladins profile`
- Removed the `redeem_code` commands due to cookie tokens resetting every 3 days.
 - *This could be circumvented by making users register their accounts with email + password instead of their hoyolab cookies but in my opinion that is far too sensitive of data*
- `/link hoyolab` has been updated and works cleaner. You now don't add UID's manually but instead can refresh them with a new `refresh UIDs` button. If this causes any issues, please DM me!
 - It should now also actually *work*. This command breaks somewhat often due to API changes on Hoyoverse's side. :(
- Added a new **Notification System** for reminders.
 - These notifications can be found under `/<game> account info`
 - Resin, Commissions, Realm Currency and Transformer for Genshin
 - Trailblaze Power and Daily Training for Star Rail
## Genshin
### `/genshin account stats`
- Added "Owned Chars" which shows how many characters you own and the total amount of available characters in the game
## Star Rail
### `/starrail account stats`
- Added the limited amount of data that battle chronicle displays for Star Rail currently.

### `/starrail account info`
- Added:
 - Daily Training (Commissions)
 - Simulated Universe score
 - Weekly Boss Discounts
## Fortnite
Added Fortnite support!
### `/link fortnite`
Works the same way as `/link paladins`. You can either add by ID or Name.

### `/fortnite profile`
Displays user stats such as KDA/Wins/Match Count
Displays the users BP level and % to next level

## [Danbooru](https://danbooru.donmai.us)
Added Danbooru anime image board to Itto!
### `/danbooru`
Lets you browse for a specific tag with the Danbooru API.
Displays the images in a collage that you can click through, and it will update with more images when possible
