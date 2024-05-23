Jay's Portfolio Project #1 - Draft in Discord

Initial Plan:
- GOAL: Magic: the Gathering draft functionality within discord.
- Achieved via bot, without exiting the discord app
- Multiple draft pods simultaneously?
- Drafts are logged to txt files
- Set files uploaded outside of discord
- Draft settings determined by player who initiates the draft
- Draft settings include:
 - Time limit for player to make their picks
 - What set is being drafted
 - What players are drafting (draft sent via dms)
- Send image showing all cards in the draft.

Things I lack experience in:
- Python async type stuff.
 - I've worked with multithreading in C, but python's async framework I've rarely touched before. So this'll be an experience for me to learn it.
- Modern discord py
 - I've worked with previous versions but it's changed a lot.

Overall Project Goals:
- Other than just achieving the initial plan, I want to work on this every day and make a bit of progress every day. For my portfolio, this won't just be about showing off python experience, but also showing off ability to work in github and work consistency.


Structure:

issue 1 - async. 
async makes storing data much harder. There's a few ways to solve this.
my first instinct is to set up some mutex locks and have individual threads edit a single file async as needed.
additionally i could manage a file for each player, but it's possible for player inputs to arrive out of order.
thus, probably a single variable that generates a queue of file edits, that are loaded into a file between execution steps.

issue 2 - display.
displaying 15 cards at once is hard. 
the trivial solution would be to send 15 images, but discord maxes at 10 attachments per message.
plus, that looks bad and is annoying.
i'd rather send an image with all 15 cards stitched together.
each would be labeled with a number, for use selecting one.

issue 3 - timers.
generally, drafts online include a time limit on card picks.
discord makes this harder. so i think i'll just not include a timer.

issue 4 - internal state.
Knowing which cards each player picks is complicated.
My immediate idea is to just store the number slot each person picks, and alert them if they made an illegal decision.
and then store the array of choices, not caring about whether they've seen the pack yet.
but, it's possible that they want to change their pick.
Instead, I could have each pick only be finalized when everyone has picked a card.
Handling the draft without allowing any pack build-up.
But that can be pretty annoying to faster players.
Thus, I think I'll have each pick be immediately final.

issue 5 - delayed dm states
We can't send packs to a player exactly as the previous player finishes with them, so each player will need a queue of packs on the way to them.
This queue will be accessed in at least two places, so we'll need to keep in mind that.


Thus, I think I need to learn more about python async and how python handles multithreading.
Then, I need to learn how to handle a mutex locked queue type structure.
It's possible python already automates all of this. But I'd rather be sure, as testing multithreading is unreliable.

ok, spent a few hours reading up on that.

asyncio has a pretty basic lock system. (asyncio.Lock(), acquire, release)

Since actions are always primarily waiting on player response, the bigger worry is only that non-simultaneous responses will produce an unexpected logical state.

Imagining the ideal four player drafters, with four packs.
Players A, B, C, D.
Player A has four packs waiting on them. They only see the first pack.
Player A makes their first selection, and their pack is sent to Player B (by create_task())
Player B receives a pack, it is seen that they don't currently have an open pack (Ideally this is done without a lock, but is easiest to do with a lock), and they are sent the pack.

this all seems to come back to like... universal awaiting on player input being generally not how discord bots work.