from twitchio.ext import commands
import requests

class Math(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(1, 2, commands.Bucket.user)
    async def math(self, ctx: commands.Context):
        try:
            expression = ctx.message.content.split(ctx.prefix + ctx.command.name)[1].strip()
            expression = requests.utils.quote(expression)
            url = f'http://api.mathjs.org/v4/?expr={expression}'
            response = requests.get(url)
            data = response.json()
            number = data
            message = f'{number}'
            await ctx.reply(message)
        except Exception as e:
            print(e)
            await ctx.send(f"You are either retarded or the API doesn't work 🤔 [{e}]")

def prepare(bot):
    bot.add_cog(Math(bot))
