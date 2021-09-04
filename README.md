# stickbugger

Stickbugger is a Discord bot that will react to every message with a `:partyStickbug:` emoji (a wiggly stickbug that has Party Parrot coloring).
The reactions are limited to user IDs listed in the `STICKBUG_VICTIMS` environment variable. 

![A Discord user saying "you're magical" with a stickbug emoji reaction on the message](https://i.imgur.com/EWlSjlh.png)

## Setting up

Rename `template.env` to `.env` and fill in the environment variables listed there. `STICKBUG_VICTIMS` is a comma-delimited list of Discord user IDs to act on.

