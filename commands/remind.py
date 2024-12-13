from twitchio.ext import commands
import asyncio
import requests
import json

class Remind(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.user_langs = self.load_user_langs()

    @commands.command()
    @commands.cooldown(1, 3, commands.Bucket.user)
    async def remind(self, ctx: commands.Context):
        try:
            time, message = [x.strip() for x in ctx.message.content.split(maxsplit=2)[1:]]
            seconds = convert(time)
        except ValueError:
            await ctx.reply(f"Please provide a valid time and message 🥺")
            return
        
        self.user_langs = self.load_user_langs()
        user_lang = self.user_langs.get(ctx.author.name, "en")

        if user_lang != "en":
            target = f"I'll remind you in {time} < {message} >"
            langpair = f"en|{user_lang}"
            response = requests.get(f"https://api.mymemory.translated.net/get?q={target}&langpair={langpair}&de=")
            if response.status_code == 200:
                translated = response.json()["responseData"]["translatedText"]
                await ctx.reply(f'@{ctx.author.name}, {translated}')
            else:
                await ctx.reply(f"{response.status_code}")
        else:
            await ctx.reply(f'@{ctx.author.name}, I`ll remind you in {time}, < {message} >')

        await asyncio.sleep(seconds)
        if user_lang != "en":
            target = f'🔔 Your reminder {time} ago < {message} > '
            langpair = f"en|{user_lang}"
            response = requests.get(f"https://api.mymemory.translated.net/get?q={target}&langpair={langpair}&de=")
            if response.status_code == 200:
                translated = response.json()["responseData"]["translatedText"]
                await ctx.send(f'@{ctx.author.name}, {translated}')
            else:
                await ctx.send(f"{response.status_code}")
        else:
            await ctx.send(f'@{ctx.author.name}, 🔔 Your reminder {time} ago.  < {message} > ')


    def load_user_langs(self):
        try:
            with open('user_langs.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return {} 

def convert(time):
    time_dict = {"s": 1, "m": 60, "h": 3600, "d": 86400, "w": 604800, "mo": 2628000}
    unit = time[-1]

    if unit not in time_dict:
        raise ValueError("Invalid time unit.")
    
    value = int(time[:-1])
    return value * time_dict[unit]

def prepare(bot):
    bot.add_cog(Remind(bot))
