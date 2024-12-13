from twitchio.ext import commands
import requests

class Site(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(1, 2, commands.Bucket.user)
    async def site(self, ctx: commands.Context, site: str):
        url = f'https://sitecheck.sucuri.net/api/v3/?scan={site}'
        response = requests.get(url)
        data = response.json()
        try:
            site = data['site']['final_url']
        except KeyError:
            site = "Please enter a valid website URL. (e.g. www.example.com)"
        try:
            duration = data['scan']['duration']
        except KeyError:
            duration = ""
        try:
            warnings = data['warnings']['scan_failed'][0]['msg']
        except KeyError:
            warnings = "1"
        if warnings == "1":
            message = f'{site}, Latency = {duration}, Is available and returned no errors.'
        else:
            message = f'{site} returned an error: {warnings}'
        await ctx.reply(message)

def prepare(bot):
    bot.add_cog(Site(bot))
