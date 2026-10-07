import discord
import random
import os
from config import TOKEN
from bot_logic import gen_pass
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'Estamos logados como {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Olá! eu sou um bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 100):
    await ctx.send("he" * count_heh)

@bot.command()
async def dino(ctx):
    await ctx.send("RAAAAAAAAAAAAAAAAAAHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH")

@bot.command()
async def aura(ctx, size = 10):
    await ctx.send("LEGENDS NEVER DIE" + "E" * size)

@bot.command()
async def senha(ctx, size = 10):
    await ctx.send(gen_pass(size))

@bot.command()
async def meme(ctx):
    chosed = random.choice(os.listdir('memes'))
    with open(f'memes/{chosed}', 'rb') as f:
        image = discord.File(f)
    await ctx.send(file=image)

bot.run(TOKEN)
