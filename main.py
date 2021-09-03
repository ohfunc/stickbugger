import os

import discord
import logging

from discord.errors import Forbidden, HTTPException, InvalidArgument, NotFound
from dotenv import load_dotenv

logging.basicConfig(level=logging.INFO)

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
VICTIMS = [int(id) for id in os.getenv('STICKBUG_VICTIMS').split(',')]

PARTYBUG_EMOJI='<a:partyBug:880999224660070510>'

client = discord.Client()

@client.event
async def on_connect():
  logging.info(f'{client.user} has connected')

@client.event
async def on_ready():
  logging.info(f'{client.user} is ready')

@client.event
async def on_message(message):
  if message.author.id in VICTIMS:
    logging.info(f'Stickbugging {message.author} ({message.author.id})')
    try: 
      await message.add_reaction(PARTYBUG_EMOJI)
    except (InvalidArgument, HTTPException, Forbidden, NotFound) as err:
      logging.error(f'Unable to add stickbug: {err}')

def main():
  logging.info(f'Running stickbugger on {VICTIMS}.')
  client.run(TOKEN)

if __name__ == '__main__':
  main()

