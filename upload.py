import discord
import os

token = 'NTkwMTc0NDEzMTMyMDA1Mzk2.XoNlJQ.pIlSyI-aqB7KW7VJo6Us6it5iqg'
client = discord.Client()
upload_path = 'C:\\Users\\Kulimi\\Pictures\\UploadArea\\'
files = os.listdir(upload_path)

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
    if start_upload:
        return
    if message.author == client.user:
        return
    print(f'[{message.guild.name}][{message.channel.name}][{message.author.name}]: {message.content}')
    if input('upload?') == 'True':
        start_upload = True
        timer = 0
        for file in files:
            timer += 1
            try:
                print(timer)
                print((upload_path + file))
                record_file.write(upload_path + file + '\n')
                await message.channel.send(file=discord.File(upload_path + file))
            except Exception as e:
                print(e)
                print('error occur', upload_path + file)
        print('End')


client.run(token)
