from twitchio.ext import commands
from random import choice

class Pick(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    @commands.cooldown(1, 1, commands.Bucket.user)
    async def pick(self, ctx: commands.Context):
        words = ctx.message.content.split()[1:]
        if len (words) < 2:
            await ctx.reply (f"Please provide at least two words 🥺")
        else:
            await ctx.reply (f"{choice (words)}")

def prepare(bot):
    bot.add_cog(Pick(bot))