import discord
import os
import roblox

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
CHANNEL = int(os.getenv('CHANNEL_ID'))
intents = discord.Intents.all()


# @ebot.event
class Ebot(commands.Bot):
    async def on_ready(self):
        print(f'{self.user} has connected to Discord!')
        channel = self.get_channel(CHANNEL)
        await channel.send('We got prime, bois.')

    async def on_member_join(self, member):
        print(f'New member')
        channel = self.get_channel(CHANNEL)
        await channel.send(f'Greetings {member.name}, welcome to my Discord server! Eh. Wait, what?')
        await member.create_dm()
        await member.dm_channel.send(
          f'Greetings {member.name}, welcome to my Discord server! Eh. Wait, what?'
        )

    def add_commands(self):
        @self.command(name="roblox_game", pass_context=True)
        async def roblox_game(ctx):
            print(ctx)
            await ctx.send(roblox.get_random_game())


ebot = Ebot(command_prefix='!', intents=intents)
ebot.add_commands()
ebot.run(TOKEN)
