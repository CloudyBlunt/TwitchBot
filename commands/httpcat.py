
from twitchio.ext  import commands
import random

class HttpsCat(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(1, 3, commands.Bucket.user)
    async def httpcat(self, ctx: commands.Context,  *, number: int=None):
        numbers = (
        "100",
        "101",
        "102",
        "103",
        "200",
        "201",
        "202",
        "203",
        "204",
        "205",
        "206",
        "207",
        "208",
        "214",
        "226",
        "300",
        "301",
        "302",
        "303",
        "304",
        "305",
        "307",
        "308",
        "400",
        "401",
        "402",
        "403",
        "404",
        "405",
        "406",
        "407",
        "408",
        "409",
        "410",
        "411",
        "412",
        "413",
        "414",
        "415",
        "416",
        "417",
        "418",
        "420",
        "421",
        "422",
        "423",
        "424",
        "425",
        "426",
        "428",
        "429",
        "431",
        "444",
        "450",
        "451",
        "497",
        "498",
        "499",
        "500",
        "501",
        "502",
        "503",
        "504",
        "506",
        "507",
        "508",
        "509",
        "510",
        "511",
        "521",
        "522",
        "523",
        "525",
        "530",
        "599",
        )               
        if number is None:
            code = random.choice(numbers)
            await ctx.send(f'https://http.cat/{code}')
            return

        await ctx.send(f'https://http.cat/{number}')

        
def prepare(bot):
    bot.add_cog(HttpsCat(bot))
