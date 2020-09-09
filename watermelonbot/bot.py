import json

from discord import Embed, RawReactionActionEvent
from discord.ext.commands import Bot

bot = Bot(command_prefix='w.')

bot.g = None


@bot.event
async def on_ready():
    bot.g = await bot.fetch_guild(694220562364366848)
    print('Online')


@bot.event
async def on_raw_reaction_add(payload: RawReactionActionEvent):
    channel = await bot.fetch_channel(payload.channel_id)
    message = await channel.fetch_message(payload.message_id)
    if message.author.id == 753351906608283678:
        return
    if str(payload.emoji) != '🍉':
        return
    with open('data.json', 'r') as f:
        data = json.load(f)

    print(data)

    try:
        data[str(message.author.id)] = data[str(message.author.id)] + 1
    except:
        data[str(message.author.id)] = 1

    print(data)

    with open('data.json', 'w') as f:
        json.dump(data, f)


@bot.command()
async def writefile(ctx):
    await ctx.message.delete()
    d = {}
    x = 0
    y = 0
    async for m in ctx.channel.history(limit=None):
        x += 1
        if m.author.id == 753351906608283678:
            continue
        if not m.reactions and '🍉' not in m.reactions:
            continue
        for r in m.reactions:
            if r.emoji == '🍉':
                try:
                    d[m.author.id] = d[m.author.id] + r.count
                except:
                    d[m.author.id] = r.count
        y += 1
        print(f'{x} + {y}')

    # dump to the file
    with open('data.json', 'w') as f:
        json.dump(d, f)


@bot.command()
async def wb(ctx):
    await ctx.message.delete()
    with open('data.json', 'r') as f:
        data = json.load(f)

    emb = Embed(title='Watermelons', description=f'Channel: {ctx.channel.mention}', color=0xFF476F)
    for (user, count) in data.items():
        m = await bot.g.fetch_member(int(user))
        emb.add_field(
            name=m.nick,
            value=f'{m.mention} has {count} watermelon(s). 🍉',
            inline=True
        )
    m = await ctx.channel.send(embed=emb)
    await m.add_reaction('🍉')


bot.run('NzUzMzUxOTA2NjA4MjgzNjc4.X1k7ow.NwLk148Ob_aHIV3dH01gui-oR1c')
