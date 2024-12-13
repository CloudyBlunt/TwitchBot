from twitchio.ext import commands
import requests
from bs4 import BeautifulSoup

class Genius(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    @commands.cooldown(1, 3, commands.Bucket.user)
    async def genius(self, ctx: commands.Context, *, target: str):
        url = f"https://genius.com/artists/{target}"
        response = requests.get(url)
        try:
            soup = BeautifulSoup(response.content, "html.parser")
            title = soup.find("p")
            name = soup.find("h1")
            fixed_url = url.replace(" ", "-")
            description = f"{title.get_text()}"
            if name.get_text().startswith("Oops"):
                await ctx.reply(f"I couldn't find anything close to {target} 😓😓🥺")
                return
            else:
                await ctx.reply(f"{name.get_text()} - {description:.400} | {fixed_url}")
        except Exception as a:
            await ctx.reply(f"[{a}]")

def prepare(bot):
    bot.add_cog(Genius(bot))