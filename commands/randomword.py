from twitchio.ext import commands
import requests
import json


class Randomword(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases = ("word",))
    @commands.cooldown(1, 2, commands.Bucket.user)
    async def randomword(self, ctx: commands.Context,):
        self.user_langs = self.load_user_langs()
        user_lang = self.user_langs.get(ctx.author.name, "en")
        url = f'https://random-word-api.herokuapp.com/word'
        response = requests.get(url)
        data = response.json()
        text = data[0]
        message = f'{text}'

        if user_lang != "en":
            target = message
            langpair = f"en|{user_lang}"
            response = requests.get(f"https://api.mymemory.translated.net/get?q={target}&langpair={langpair}&de=")
            if response.status_code == 200:
                translated = response.json()["responseData"]["translatedText"]
                await ctx.reply(translated)
            else:
                await ctx.reply(f"{response.status_code}")
        else:
            await ctx.reply(message)

    def load_user_langs(self):
        try:
            with open('user_langs.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return {} 

def prepare(bot):
    bot.add_cog(Randomword(bot))
