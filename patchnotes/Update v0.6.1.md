# Update v0.6.1

### Quite a few major backend changes introduced this update to future-proof Itto
- (As always, bugs are to be expected but I will fix them as soon as I can!)

- Bot now loads commands and databases before it officially "boots" which means that it should not break if a command is executed between the time bot goes online and all commands are initialised
- Minor text/layout tweaks.

## Help Command
- Improved the display and changed some grammar issues.

## Paladins

### Added 4 random commands!
- Random drawing for Champions, Maps, Talents and Teams
- Can specify sub-parameters such as role, game-mode and champion.
- Include reroll buttons so you don't have to run commands again.

### New alias system
You can now set an alias for IGN's that you can type in instead of the IGN/ID.
You set this alias with `/paladins alias <ign/id> <alias>`
For example, you can set an alt account to "me2" and when you need to specify a player name, you can type in "me2"
- Aliases cannot have custom loadout images. Those are tied to your linked account
- "me" is reserved and not available to be set as that is a hardcoded alias for your own account
- If you alias an already existing IGN, you will have to either use their ID or remove your alias if you want to view the un-aliased player.
- You can view all your aliases by not passing in any arguments into `/paladins alias`

### Tracking new avatars myself
I now store all avatars locally so if any avatars are missing from the online database I will be able to update them.
- This means that all avatars will be made available over time on Itto, less empty/missing avatars.

### `/paladins loadouts`
- Unlinking your account now also removes your custom saved loadout images
- Storing custom loadout images is now changed, so your URL's are able to expire
 - Should provide some minor speed improvements
 - *(This was done as discord introduced timestamps so images hosted on discord would expire after a while)*
*Note: All users that had images saved before v0.6.1 will be migrated to new system upon update*

### `/paladins cards`
- Fixed an issue where negative levels would mean cards are missing their card asset.

### `/paladins stats`
- The data range for matches is going from 3 weeks to 4.
 - This is due to API breaking on more and more matches meaning we may need a larger pool for good quality data
 - Hoping to get more data for stats by adding another week. This will be in ***testing*** when bot goes live and may be tweaked back down to 3 weeks if the queries take too long.

### `/paladins match`
- Added disconnect indicators for players that disconnected during a match or didn't choose a talent.
 - May not always be 100% accurate as the system behind it is a little weird, but it should work fine. If there are any big issues with this please just DM me the match ID.
- Added a new "map flair" asset to fill out the right side of the middle match bar.
 - It's formatted based on a set of my own rules on maps so that the icons are always *somewhat* themed.
- Fixed an issue where the Fiery Disposition talent for Betty would not display due to weird API formatting.
- Fixed an issue with cards that have an exclamation in them, not showing their arts.
 - (Itto is deathly allergic to "!"'s, and beans)
### `/paladins champions`
- Recoded the champion stats list so it's slightly faster
### `/paladins history`
- Benefits from the same speed improvements mentioned above (hooray for re-use of code :D)
- Added win rates to the top stats tab
- Added sort by `role`

### `/paladins current`
- Aliases will be processed at the same speed as ID's when passed in.
 - This means that passing in multiple player aliases will be faster and won't show the note about typing in multiple ID's.
- Added a 5s cooldown in between uses.
 - To help alleviate API spam/rate limiting, I've added a per-user cooldown.
### `/paladins friends`
- You can now reset your search query by clicking the search button and then not typing anything into the box.
 - No longer have to re-run the command if you want to view the whole friends list!
## Genshin

### `/genshin account income`
- Removed command due to same reason redeeming codes has been removed in the past. (fast expiring cookies)

### `/genshin account abyss`
- New command that lets you view your current and previous abyss runs.
- Displays each floor and chamber's characters like Hoyolab would, but in Itto's own format.
- Also displays the general statistics like on hoyolab, such as strongest single hit, etc.

### `/genshin account characters`
- Completely re-coded the command.
 - Fixed weird button and dropdown menu bugs
 - Fixed some minor layout issues
 - Is now faster by default.
### `/genshin search bosses`
- Temporarily disabled command as I'm working on a larger overhaul to "character build"-esque features for Itto.
### Reminders
- Reworked code so it runs smoother and more efficiently.
- Added in "Spiral Abyss" reset reminder.
- It now aggregates any messages sent instead of spamming multiple single messages.
- Daily reset is now properly an hour before reset instead of two hours.
 - This was due to daylight savings time changes
## Star Rail

### `/starrail account characters`
- Added command!
- Displays info in a similar manor to `/genshin account characters`
 - Data is sadly a lot more limited than Genshin's, but that's all the info provided by Hoyolab.

## Other
### `/danbooru`
- Command has been removed as the system for it was slow and quite clunky. You can use the [official site](<https://safebooru.donmai.us>) for browsing art instead!

### `/fortnite`
- Commands have been removed as not many people used the system. May be re-added in a future larger Fortnite themed update.

### `/user`
- re-added the user command so you can fetch a user's ID, PFP, and banner.