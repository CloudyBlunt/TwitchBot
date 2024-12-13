from twitchio.ext import commands
import asyncio

class Spam(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(1, 15, commands.Bucket.user)
    async def spam(self, ctx: commands.Context, count: int, *, message :str=None):
        if not ctx.author.is_mod and not ctx.author.is_vip: 
            return    
            
        if ctx._bot_is_mod() is False:
            await ctx.reply("I have t-to be a moderator to execute t-this command... 🥺")
            return

        max_countMod = 500
        max_countVip = 30

        if ctx.author.is_mod:
            if count > max_countMod:
                await ctx.reply(f"{max_countMod} message limit")
                return

        if ctx.author.is_vip:
            if count > max_countVip:
                await ctx.reply(f"{max_countVip} message limit for you in particular")
                return

        if ctx.author.is_mod:
            for i in range(count):
                await ctx.send(message)

        if ctx.author.is_vip:
            for i in range(count):
                await ctx.send(message)
                await asyncio.sleep(0.2)

def prepare(bot):
    bot.add_cog(Spam(bot))
