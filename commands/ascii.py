from twitchio.ext import commands
import requests
import pyfiglet

class Ascii(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    @commands.cooldown(1, 5, commands.Bucket.user)
    async def ascii(self, ctx: commands.Context):
        args = ctx.message.content.split()
        if len(args) > 1:
            text = args[1]
            if len(args) > 2:
                style = args[2]
            else:
                style = "standard"
            ascii = pyfiglet.figlet_format(text, font=style)
            fixed = ascii.replace(" ", "_")
            response = requests.post("https://haste.potat.app/documents", data=fixed)
            if response.status_code == 200:
                key = response.json()["key"]
                link = f"https://haste.potat.app/{key}"
                await ctx.reply(f"{link}")
            else:
                await ctx.reply(f"{response.status_code}")
        else:
            await ctx.reply("👉 #ascii [text] [style], (available styles = slant, 3-d, 3x5, 5lineoblique, alphabet, banner3-D, doh, standard, isometric1, letters, alligator, dotmatrix)")

def prepare(bot):
    bot.add_cog(Ascii(bot))