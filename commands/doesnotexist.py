from twitchio.ext import commands
import random

class ThisDoesNotExist(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(aliases = ("pepe", "randompepe", "aipepe"))
    @commands.cooldown(1, 3, commands.Bucket.user)
    async def thispepedoesnotexist(self, ctx: commands.Context):
        random_number = random.randint(0, 9000)
        await ctx.reply(f'http://www.thispepedoesnotexist.co.uk/out/pepe%20({random_number}).png')

    @commands.command(aliases = ("cat", "randomcat", "aicat"))
    @commands.cooldown(1, 3, commands.Bucket.user)
    async def thiscatdoesnotexist(self, ctx: commands.Context):
        random_number1 = random.randint(1, 3)
        random_number2 = random.randint(0, 8100)
        await ctx.reply(f'https://d2ph5fj80uercy.cloudfront.net/0{random_number1}/cat{random_number2}.jpg')

    @commands.command(aliases = ("waifu", "randomwaifu", "aiwaifu"))
    @commands.cooldown(1, 3, commands.Bucket.user)
    async def thiswaifudoesnotexist(self, ctx: commands.Context):
        random_number = random.randint(0, 99999)
        await ctx.reply(f'https://www.thiswaifudoesnotexist.net/example-{random_number}.jpg')

def prepare(bot):
    bot.add_cog(ThisDoesNotExist(bot))