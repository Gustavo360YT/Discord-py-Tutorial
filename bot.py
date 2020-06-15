import discord
from discord.ext import commands

client = commands.Bot(command_prefix='!')

@client.event
async def on_ready():
    print(f'Bot is now online')

@client.command(aliases=['p', 'q'])
async def ping(ctx, arg=None):
    if arg == "pong":
        await ctx.send('Nice job, you just ponged yourself')

    else:
        await ctx.send(f'Pong! Here is you ping: {round(client.latency * 1000)}ms')

client.run('NzIwNjE2Njg0Nzc5NDcwODcx.XuI1bA.cEVGZzuj5oLnZMnQCtMm7R0EPKw')
