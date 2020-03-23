import discord
import os

token = ''
client = discord.Client()

files = os.listdir('C:\\Users\\Kulimi\\Pictures\\SuperDanger')

print(files)
print(len(files))

start_upload = False

record_file = open('record.txt', 'a')

@client.event
async def on_ready():
    print(f'{client.user} uploader')


@client.event
async def on_message(message):
    global start_upload, record_file
    print(f'[{message.guild.name}][{message.channel.name}][{message.author.name}]: {message.content}')

    if start_upload:
        return
    if message.author == client.user:
        return
    print(f'[{message.guild.name}][{message.channel.name}][{message.author.name}]: {message.content}')
    if input('upload?') == 'True':
        start_upload = True
        timer = 0
        for file in files:
            try:
                print(timer)
                print(('C:\\Users\\Kulimi\\Pictures\\SuperDanger\\' + file))
                record_file.write('C:\\Users\\Kulimi\\Pictures\\SuperDanger\\' + file + '\n')
                await message.channel.send(file=discord.File('C:\\Users\\Kulimi\\Pictures\\SuperDanger\\' + file))
            except Exception as e:
                print(e)
                print('error occur', 'C:\\Users\\Kulimi\\Pictures\\SuperDanger\\' + file)
            timer += 1
        print('End')

client.run(token)
