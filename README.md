# AureusArchive
Here lies my first Discord bot. Working on this helped me get familiar with Python, and I've found it would be much easier to just make a new bot than to keep working on this one.
I'm uploading this about two months after I've stopped working on it, and many of the... even uglier cogs are missing.

-First, I relied a LOT on the tutorials in the discord.py docs, but only parts I understood. The discord.py tutorials didn't cover everything though, and not knowing Python at all at the time didn't help either. When I was first making the bot, I would sometimes follow a tutorial but not bother to learn the ins and outs of *why* something worked or why it didn't. Other times, I'd not use something simply BECAUSE I didn't understand how it worked.

-Next, looking back, this bot sucks. It has a few commands, but a lot is missing or broken:

- No logging. Good luck finding out when and why an error happened. I know how to log now, though!
- Lack of uniformity. Its on-ready event both prints to console AND sends a message to a single channel, while the bot is in three servers? This was useful when testing, but a bot should be running 24/7 so its usable to a server's members whenever. I know how to make all this consistent now, though!
- No database access. It isn't designed in a way that makes it easy to store data for an exp or economy system. Nor any sort of moderation-related logs (not that you'd want to use this bot for moderation when so many free alternatives already exist). I've learned PostgreSQL now, though. The next bot will have DB support!
- Little to no command error handling. Commands invoked without arguments or with invalid ones simply don't work. Ideally, the user invoking the command would receive an embed showing proper usage of a command. I know how to do this now, though!
- Some cogs are... not great. The MineServer cog is a complete mess, the music cog wasn't finished, some cogs had unnecessary commands(who uses a device with internet and doesn't know the time?), etc. I know how to design for the servers that would use this bot now, though!
- My commit format on the original repo was a mess. I know how to make slightly more useful and slightly more consistent commit messages now, though!
- Permissions. Discord.py has built-in ways to determine if a user has "admin" or "moderator" perms... and I ignored it all and used one server's role id instead. This makes a bunch of commands fail in the other servers the bot was in, and also looks dumb. I know how to use this a bit better now, though!
- No config/settings file, no way to disable or enable commands or a cog from within Discord
- A load of others I won't type out right now.
- No web dashboard. 

So, I've put this here, just for someone to look at, I guess. Please leave feedback here or message me on discord. While I don't plan on making the same mistakes with my next bot, **every** bit of criticism still helps!
