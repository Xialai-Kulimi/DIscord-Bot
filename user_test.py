import discord
import os

token = 'NTkwMTc0NDEzMTMyMDA1Mzk2.XoIIdA.GB_-EzuTQAzZ30VeVC3c6ST1NoM'
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
    await client.login("NDgwOTg3NTY4OTAxNDU1ODcy.XoIF3A._c1dEYNlaK--XjI4f5-8mQSVlWI")
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
            try:
                print(timer)
                print((upload_path + file))
                record_file.write(upload_path + file + '\n')
                await message.channel.send(file=discord.File(upload_path + file))
            except Exception as e:
                print(e)
                print('error occur', upload_path + file)
            timer += 1
        print('End')


# async def main():
#     await client.login("NDgwOTg3NTY4OTAxNDU1ODcy.XoIF3A._c1dEYNlaK--XjI4f5-8mQSVlWI")
#
#
# main()

client.run(token)
