import random

import discord
from random_word import RandomWords
from discord.ext import commands

bot = commands.Bot('-')


@bot.event
async def on_ready():
    act = discord.CustomActivity('Fuck you!')
    await bot.change_presence(activity=act)

    print('Bot Online!')


@bot.command()
async def say(ctx: commands.Context, channel, *, text: str):
    await ctx.message.delete()

    channel = ctx.message.channel_mentions[0]

    await channel.send(
        embed=discord.Embed(
            color=0xED213A,
            description=text
        ).set_footer(text=ctx.message.author.name, icon_url=ctx.message.author.avatar_url)
    )


@bot.command()
async def solve(ctx: commands.Context, *, text: str):
    try:
        await ctx.channel.send(
            embed=discord.Embed(
                color=0xED213A,
                description=f'`{text}` = `{eval(text)}`'
            )
        )
    except:
        await ctx.channel.send(
            embed=discord.Embed(
                color=0xED213A,
                description="Give me a proper math equation dumbass."
            )
        )


@bot.command()
async def story(ctx: commands.Context):
    words = RandomWords().get_random_words(limit=500)
    s = ""
    count = 0
    for i in range(random.randint(45, 75)):
        s += f'{random.choice(list(words))} '
        count+=1

    await ctx.channel.send(
        embed=discord.Embed(
            title="A Short Story",
            description=s,
            color=0xED213A
        ).set_footer(text=f'Word Count: {count}')
    )


bot.run('NzQ3NTg2MjEwMTY3MzkwMzI5.X0RB6Q.Y2QJDVtXD7dCiENa_HkgNC1BxTU')
