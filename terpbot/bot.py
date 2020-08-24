import discord
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


bot.run('NzQ3NTg2MjEwMTY3MzkwMzI5.X0RB6Q.Y2QJDVtXD7dCiENa_HkgNC1BxTU')
