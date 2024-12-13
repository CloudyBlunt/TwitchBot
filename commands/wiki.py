from twitchio.ext import commands
import requests

class Wiki(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    @commands.cooldown(1, 3, commands.Bucket.user)
    async def wiki(self, ctx: commands.Context, language, *, search : str =None):
        try:
            if search is None:
                url1 = f'https://en.wikipedia.org/api/rest_v1/page/summary/{language}'
                response1 = requests.get(url1)
                data1 = response1.json()
                
                title1 = data1['titles']['normalized']
                more1 = data1['description']
                link1 = data1['content_urls']['desktop']['page']

                message1 = f'{title1} - {more1} | {link1}'
                await ctx.reply(message1)
                return
            url = f'https://{language}.wikipedia.org/api/rest_v1/page/summary/{search}'
            response = requests.get(url)
            data = response.json()
            
            title = data['titles']['normalized']
            more = data['description']
            link = data['content_urls']['desktop']['page']

            message = f'{title} - {more} | {link}'
            await ctx.reply(message)
        except Exception as e:
            await ctx.reply(f"Either nothing was found, or there was an error FeelsBadMan")       
            print(e) 
        return

def prepare(bot):
    bot.add_cog(Wiki(bot))
