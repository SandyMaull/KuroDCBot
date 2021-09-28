import discord
from discord.ext import commands
import youtube_dl
import requests
import json
import os
import time


def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return quote

class music(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def join(self,ctx):
        if ctx.author.voice is None:
            await ctx.send("You're not in a voice channel!")
        voice_channel = ctx.author.voice.channel
        if ctx.voice_client is None:
            await voice_channel.connect()
        else:
            await ctx.voice_client.move_to(voice_channel)

    @commands.command()
    async def disconnect(self,ctx):
        await ctx.voice_client.disconnect()

    @commands.command()
    async def play(self, ctx, url):
        try:
            ctx.voice_client.stop()
            FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
            YDL_OPTIONS = {'format':'bestaudio'}
            vc = ctx.voice_client

            with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
                info = ydl.extract_info(url, download=False)
                url2 = info['formats'][0]['url']
                #   exec_path = os.path.isfile('./Include/ffmpeg.exe')
                # source = await discord.FFmpegOpusAudio.from_probe(url2, **FFMPEG_OPTIONS, executable='./Include/ffmpeg.exe')
                source = await discord.FFmpegOpusAudio.from_probe(url2, **FFMPEG_OPTIONS)
                #   vc.play(discord.FFmpegPCMAudio(executable=exec_path, source=source))
                vc.play(source)
        except:
            await ctx.send("An error occurred, please check the backend services!")

    @commands.command()
    async def pause(self, ctx):
        await ctx.voice_client.pause()
        await ctx.send("paused")

    @commands.command()
    async def resume(self, ctx):
        await ctx.voice_client.resume()
        await ctx.send("resume")

    @commands.command()
    async def whoami(self, ctx):
        await ctx.send(ctx.author)

    @commands.command()
    async def quote(self, ctx):
        quotes = get_quote()
        await ctx.send(quotes)

    @commands.command()
    async def hello(self, ctx):
        await ctx.send('Hello {user} ! \nHow r u today? \nHere i got a nice quotes for filling your day, i hope everything will be fine :) \n\n{quotes}'.format(user=ctx.author, quotes=get_quote()))

    @commands.command()
    async def Hai(self, ctx):
        await ctx.send('Hai juga {response}'.format(response=ctx.author))

    @commands.command()
    async def get_roles(self, ctx):
        await ctx.send('Error on Applying new Roles to {user}'.format(user=ctx.author))

    @commands.command()
    async def ping(self, ctx):
        before = time.monotonic()
        message = await ctx.send("Pong!")
        ping = (time.monotonic() - before) * 1000
        await message.edit(content=f"Pong!  `{int(ping)}ms`")

def setup(client):
    client.add_cog(music(client))