import discord
from discord.ext import commands

client = commands.Bot(command_prefix='!')

@client.event
async def on_ready():
    print(f'Logged in as: {client.user.name}\n-----\nMy prefix is !')

@client.event
async def on_member_join(member):
    print(f'{member} joined the server!')

@client.event
async def on_member_remove(member):
    print(f'{member} left the server')

@client.command(aliases=['p', 'q'])
async def ping(ctx, arg=None):
    if arg == "pong":
        await ctx.send('Nice job, you just ponged yourself')

    else:
        await ctx.send(f'Pong! Here is you ping: {round(client.latency * 1000)}ms')

client.run('your-token')
