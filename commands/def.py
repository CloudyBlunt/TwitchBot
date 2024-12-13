from twitchio.ext import commands
import requests
from bs4 import BeautifulSoup

class Wiktionary(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(aliases = ("def","dict","meaning"))
    @commands.cooldown(1, 3, commands.Bucket.user)
    async def dictionary(self, ctx: commands.Context, language, *, search : str =None):
        try:
            if search is None:
                url = f"https://en.wiktionary.org/wiki/{language}"
                response = requests.get(url)
                
                soup = BeautifulSoup(response.content, "html.parser")
                word1 = soup.find("p")
                word2 = soup.find("h1")
                meaning1 = soup.find("ol")
                                        
                await ctx.reply(f"{word2.get_text()} ({word1.get_text()}) — {meaning1.get_text():.400}")
                
                return
            url = f"https://{language}.wiktionary.org/wiki/{search}"
            response = requests.get(url)

            soup = BeautifulSoup(response.content, "html.parser")
            word1 = soup.find("p")
            word2 = soup.find("h1")
            meaning1 = soup.find("ol")               

            await ctx.reply(f"{word2.get_text()} ({word1.get_text()}) — {meaning1.get_text():.400}")
        except Exception as a:
            print(f"{a}")
            await ctx.reply(f"Either this word doesn't exist or the API returned an error [{a}] ")

def prepare(bot):
    bot.add_cog(Wiktionary(bot))