import os
import discord
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

client = discord.Client()


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    print(client.guilds[1].channels)


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == "霹靂卡霹靂拉拉 波波力那貝貝魯多 武漢殺遊戲 掙扎吧 在血和暗的深淵裡 痛苦吧 在仇與恨的地獄中！":
        print(f'virus game start at guild {message.guild.name} ID:{message.guild.id} ')
        return


client.run(token)
