from twitchio.ext import commands
import random

class Mycheck(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(aliases=("mycock",))
    @commands.cooldown(1, 2, commands.Bucket.user)
    async def cock(self, ctx: commands.Context):
        cms = random.randint(0, 50)
        if cms < 20:
            emotes = ("😁", "🤣", "🤢", "😢", "😂")
            lmao = random.choice(emotes)
            message = f"{lmao} 👉 {cms} cm."
            await ctx.reply(message)  
        else:
            emotes = ("🤩", "😍", "🥰", "🥺🥛", "😉", "😏", "😳", "🤯")
            waow = random.choice(emotes)
            message = f"{waow} 👉 {cms} cm."
            await ctx.reply(message)
        
def prepare(bot):
    bot.add_cog(Mycheck(bot))