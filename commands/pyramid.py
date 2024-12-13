from twitchio.ext import commands

class Pyramid(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(1, 25, commands.Bucket.user)
    async def pyramid(self, ctx: commands.Context, num: int = 3, *, target: str):
        if not ctx.author.is_mod and not ctx.author.is_vip: 
            return
        messages = []

        if ctx.author.is_mod:
            if num < 1 or num > 50:
                await ctx.reply("Too big. Can't be bigger than 50")
                return

        if ctx.author.is_vip:
            if num < 1 or num > 25:
                await ctx.reply("Too big. Can't be bigger than 25")
                return

        for i in range(1, num + 1):
            message = (target + " ") * i
            await ctx.send(f"{message:.500}")
            messages.append(f"{message:.500}")
            
        for message in reversed(messages[:-1]):
            await ctx.send(f"{message:.500}")
        
def prepare(bot):
    bot.add_cog(Pyramid(bot))