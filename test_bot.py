import discord

token = ''
client = discord.Client()


@client.event
async def on_ready():
    print(f'{client.user}上線拉！！！！！！！！！！！！！！！！！！')


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    await message.channel.send('好喔。')


client.run(token)