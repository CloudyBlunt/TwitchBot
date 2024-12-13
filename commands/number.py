from twitchio.ext import commands
import random

class Number(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases = ("randomnumber",))
    @commands.cooldown(1, 2, commands.Bucket.user)
    async def number(self, ctx: commands.Context):
        try:
            a, b = [int(x) for x in ctx.message.content.split()[1:3]]
        except ValueError:
            await ctx.reply(f"Please provide two valid numbers 🥺")
            return
        num = random.randint(a, b)
        await ctx.reply(f"{num}")


def prepare(bot):
    bot.add_cog(Number(bot))