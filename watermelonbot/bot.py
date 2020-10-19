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
    if payload.user_id == message.author.id:
        await channel.send(
            embed=Embed(title="Nice Try", description=f"Slow down there <@{payload.user_id}>.\nYou can't give yourself watermelons 🍉.", color=0xff0000)
        )
        return
    with open('received.json', 'r') as f:
        received = json.load(f)
    with open('given.json', 'r') as f:
        given = json.load(f)

    try:
        received[str(message.author.id)] = received[str(message.author.id)] + 1
        given[str(payload.user_id)] = given[str(payload.user_id)] + 1
    except:
        received[str(message.author.id)] = 1
        given[str(payload.user_id)] = 1

    with open('received.json', 'w') as f:
        json.dump(received, f)
    with open('given.json', 'w') as f:
        json.dump(given, f)


@bot.event
async def on_raw_reaction_remove(payload: RawReactionActionEvent):
    channel = await bot.fetch_channel(payload.channel_id)
    message = await channel.fetch_message(payload.message_id)
    if message.author.id == 753351906608283678:
        return
    if str(payload.emoji) != '🍉':
        return
    with open('received.json', 'r') as f:
        received = json.load(f)
    with open('given.json', 'r') as f:
        given = json.load(f)

    try:
        received[str(message.author.id)] = received[str(message.author.id)] - 1
        given[str(payload.user_id)] = given[str(payload.user_id)] - 1
    except:
        received[str(message.author.id)] = 0
        given[str(payload.user_id)] = 0

    with open('received.json', 'w') as f:
        json.dump(received, f)
    with open('given.json', 'w') as f:
        json.dump(given, f)


@bot.command()
async def writefile(ctx):
    await ctx.message.delete()
    received = {}
    given = {}
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
                    received[m.author.id] = received[m.author.id] + r.count
                    async for user in r.users():
                        given[user.id] = given[user.id] + 1
                except:
                    received[m.author.id] = r.count
                    async for user in r.users():
                        given[user.id] = 1
        y += 1
        print(f'{x} + {y}')

    # dump to the file
    with open('received.json', 'w') as f:
        json.dump(received, f)
    with open('given.json', 'w') as f:
        json.dump(given, f)

    print('done!')


@bot.command()
async def wb(ctx):
    await ctx.message.delete()
    with open('received.json', 'r') as f:
        received = json.load(f)
    with open('given.json', 'r') as f:
        given = json.load(f)

    emb = Embed(title='Watermelons', description=f'Channel: {ctx.channel.mention}', color=0xFF476F)

    final_received = ""
    final_given = ""

    for (user, count) in received.items():
        m = await bot.g.fetch_member(int(user))
        final_received += f'{m.mention}: `{count}`\n'

    for (user, count) in given.items():
        m = await bot.g.fetch_member(int(user))
        final_given += f'{m.mention}: `{count}`\n'

    emb.add_field(
        name="Watermelons Received",
        value=final_received,
        inline=True
    )
    emb.add_field(
        name="Watermelons Given",
        value=final_given,
        inline=True
    )

    m = await ctx.channel.send(embed=emb)
    await m.add_reaction('🍉')


bot.run('NzUzMzUxOTA2NjA4MjgzNjc4.X1k7ow.NwLk148Ob_aHIV3dH01gui-oR1c')
