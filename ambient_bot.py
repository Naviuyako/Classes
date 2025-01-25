import discord
from discord.ext import commands
import random
import os

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix = '#', intents = intents)

@bot.event
async def log():
    print(f'Loggeado como{bot.user}')

@bot.command()
async def craft(ctx):
    img_name = random.choice(os.listdir('images'))
    with open(f'images/{img_name}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def fact(ctx):
    with open('datos\dato1.txt', 'r', encoding="utf-8") as f:
        await ctx.send(f.read())
        


bot.run(DISCORD TOKEN)
