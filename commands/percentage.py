from twitchio.ext import commands
import random

class Percent(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases = ("%", "chance",))
    @commands.cooldown(1, 1, commands.Bucket.user)
    async def percent(self, ctx: commands.Context, *, word=None): 
        percent = random.randint(0, 100)
        percent2 = random.randint(0, 99)
        if word is None:
            await ctx.reply(f'{percent}.{percent2}%')
        else:
            await ctx.reply(f'{word} {percent}.{percent2}%')

def prepare(bot):
    bot.add_cog(Percent(bot))