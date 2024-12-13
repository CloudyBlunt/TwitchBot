from twitchio.ext import commands
import requests
import json

class Uselessfact(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.user_langs = self.load_user_langs()
        
    @commands.command(aliases = ("fact",))
    async def uselessfact(self, ctx: commands.Context,):
        self.user_langs = self.load_user_langs()
        user_lang = self.user_langs.get(ctx.author.name, "en")
        url = f'https://uselessfacts.jsph.pl/api/v2/facts/random'
        response = requests.get(url)
        data = response.json()
        text = data['text']
        message = f'{text}'

        if user_lang != "en":
            target = message
            langpair = f"en|{user_lang}"
            response = requests.get(f"https://api.mymemory.translated.net/get?q={target}&langpair={langpair}&de=v1ss0nd@yahoo.com")
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
    bot.add_cog(Uselessfact(bot))