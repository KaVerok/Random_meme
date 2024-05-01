import random
import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.command()
async def animals(ctx):
    paint=os.listdir('animals_meme')
    rand_image=random.choice(paint)
    with open(f'animals_meme/{rand_image}', 'rb') as f:
        # В переменную кладем файл, который преобразуется в файл библиотеки Discord!
        picture = discord.File(f)
   # Можем передавать файл как параметр!
    await ctx.send(file=picture)

@bot.command()
async def stars(ctx):
    paint=os.listdir('celebretystars')
    rand_image=random.choice(paint)
    with open(f'celebretystars/{rand_image}', 'rb') as f:
        # В переменную кладем файл, который преобразуется в файл библиотеки Discord!
        picture = discord.File(f)
   # Можем передавать файл как параметр!
    await ctx.send(file=picture)


bot.run("")