#! python3
#Made by Leevi Pussinen
from discord.ext.commands import Bot
from discord import Server, Game
botprefix = ('!')
client = Bot(command_prefix='!')

@client.command(pass_context=True,name='game',description='List the players who are playing a game. If the game has spaces in the name, quote it with "".',
                aliases=['playing'])
async def game(ctx,gameseek):
    server = ctx.message.server
    gamerlist = []
    for member in server.members:
        if str(member.game) == gameseek:
            gamerlist.append(member)
    gamerlist.append('---------')
    await client.say('Now playing '+ gameseek)
    for i in gamerlist:
        await client.say(i)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run('NTE2MjM5NTc4MzQ5NDM2OTQx.DtwxrQ.VsVjJVTb3--moqp0c8S5u8mr3NE')
