import discord

token = ''

client = discord.Client()

data = {'virus-game': {'start-key': ['霹靂卡霹靂拉拉 波波力那貝貝魯多 武漢殺遊戲 掙扎吧 在血和暗的深淵裡 痛苦吧 在仇與恨的地獄中！', '\/\/μ#4/v |<!11 &4^^3, 57@Я7!']}}


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    # print(client.guilds[1].channels)


@client.event
async def on_message(message):

    if message.content == '+1':
        data['virus-game']['game-lobby'][str(message.guild.id) + ':' + str(message.channel.id)]['players'][message.author.id] = {'player-name': message.author.name, 'role': 0}
        await message.add_reaction("👍")

    if message.author == client.user:
        return

    for key in data['virus-game']['start-key']:  # check key
        if message.content == key:
            data['virus-game']['game-lobby'] = {str(message.guild.id) + ':' + str(message.channel.id): {'players': {}}}

            await message.channel.send('''```javascript
武漢殺開始報名
請在下面打'+1'，由我先做一個示範，我會按讚表示確認。
若確定所有人都已確認加入了，請輸入'Everyone has joined.'```''')
            await message.channel.send('+1')


client.run(token)
