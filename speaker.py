import os
import discord
import gtts

token = ''

client = discord.Client()


@client.event
async def on_ready():
    global voice_client
    print(f'{client.user} has connected to Discord!')

    print(client.guilds)

    now_guild = client.guilds[0]
    now_text_channel = now_guild.channels[0]
    now_voice_channel = ''

    while True:
        input_str = input(f'[{now_guild}][{now_text_channel}]:')
        if input_str.split(' ')[0] == '/connect_voice_channel':
            for channel in now_guild.channels:
                if channel.name == input_str.split(' ')[1]:
                    await channel.connect()
                    now_voice_channel = channel
                    discord.VoiceClient = discord.utils.get(client.voice_clients, guild=now_guild)

                    break

        if input_str.split(' ')[0] == '/cd':
            print(input_str.split(' '))
            for guild in client.guilds:
                if guild.name == input_str.split(' ')[1]:
                    now_guild = guild
                    break
            for channel in now_guild.channels:
                if channel.name == input_str.split(' ')[2]:
                    now_text_channel = channel
                    break

        if input_str.split(' ')[0] == '/into_speak_mode':
            while True:
                gonna_speak = input(f'[{now_guild}][{now_text_channel}](Speaking):')
                tts = gtts.gTTS(text=gonna_speak, lang='zh-tw')
                tts.save("gonna_speak.mp3")
                audio_source = discord.FFmpegPCMAudio('gonna_speak.mp3')
                discord.VoiceClient.play(source=audio_source, after=None)
                # player = now_voice_channel.create_ffmpeg_player('gonna_speak.mp3', after=lambda: print('done'))
                # player.start()
        # if input_str.split(' ')[0] == '/disconnect_voice_channel':
        #     for channel in now_guild.channels:
        #         if channel.name == input_str.split(' ')[1]:
        #             await channel.disconnect()
        #             break

client.run(token)
