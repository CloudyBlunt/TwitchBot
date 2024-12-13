from twitchio.ext import commands
import requests
from bs4 import BeautifulSoup


class Lurk(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(aliases = ("Lurk",))
    @commands.cooldown(1, 3, commands.Bucket.user)
    async def lurk(self, ctx: commands.Context, *, search):
        try:
            url = f"https://neolurk.org/wiki/{search}"
            response = requests.get(url)
            soup = BeautifulSoup(response.content, "html.parser")

            word = soup.find("h1")
            meaning = soup.find("p")
            message = f"{word.get_text()} — {meaning.get_text():.400}"
            
            await ctx.reply(message)
        except Exception as e:
            await ctx.reply(f"{e}")
        return

def prepare(bot):
    bot.add_cog(Lurk(bot))
