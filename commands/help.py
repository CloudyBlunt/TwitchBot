from twitchio.ext import commands

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    @commands.cooldown(1, 2, commands.Bucket.user)
    async def help(self, ctx: commands.Context):  
        await ctx.reply(f"/me ApuApustaja")

def prepare(bot):
    bot.add_cog(Help(bot))
