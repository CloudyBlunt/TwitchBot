from twitchio.ext import commands
from datetime import datetime
import datetime as dt
import requests
import random

class User(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases = ("u",))
    @commands.cooldown(1, 2, commands.Bucket.user)
    async def user(self, ctx: commands.Context, name :str = None):
        if name is None:
            user_name = ctx.author.name
        else:
            name = name.replace ("@", "")
            name = name.replace (",", "")
            user_name = name

        url = f'https://api.ivr.fi/v2/twitch/user?login={user_name}'
        response = requests.get(url)
        data = response.json()
        format = "%Y-%m-%dT%H:%M:%S.%fZ"
        current_time = datetime.now().timestamp()
        try:
            banned = data[0]['banned']
            if banned:
                chatterCount = data[0]['chatterCount']
                followers = data[0]['followers'] 
                color = data[0]['chatColor'] 
                bio = data[0]['bio']
                prefix = data[0]['emotePrefix']
                id = data[0]['id']
                display_name = data[0]['displayName']
                createdDate = data[0]['createdAt']
                updatedDate = data[0]['updatedAt']
                banReason = data[0]['banReason']
                date_object = datetime.strptime(createdDate, format)
                output_format = "%Y.%m.%d"
                createdAt = date_object.strftime(output_format)
                date_object = datetime.strptime(updatedDate, format)
                output_format = "%Y.%m.%d"
                updatedAt = date_object.strftime(output_format)

                crying_emotes = ("😭","😢","😨","😰","😱","😩","😓","😔",)
                random_emote = random.choice(crying_emotes)
                await ctx.reply(f"{id} | @{display_name}, Created at: {createdAt} (Updated at {updatedAt}) [BANNED: {banReason} {random_emote}] | Colour: {color} | Prefix: {prefix} | Followers: {followers} | Chatters: {chatterCount} | Bio: {bio}")
            else:
                chatterCount = data[0]['chatterCount']
                followers = data[0]['followers'] 
                color = data[0]['chatColor']
                bio = data[0]['bio']
                prefix = data[0]['emotePrefix']
                id = data[0]['id']
                display_name = data[0]['displayName']
                createdDate = data[0]['createdAt']
                updatedDate = data[0]['updatedAt']
                date_object = datetime.strptime(createdDate, format)
                output_format = "%Y.%m.%d"
                createdAt = date_object.strftime(output_format)
                date_object = datetime.strptime(updatedDate, format)
                output_format = "%Y.%m.%d"
                updatedAt = date_object.strftime(output_format)
                
                await ctx.reply(f"{id} | @{display_name}, Created at: {createdAt} (Updated {updatedAt}) | Colour: {color} | Prefix: {prefix} | Followers: {followers} | Chatters: {chatterCount} | Bio: {bio}")
        except Exception as nigga:
            print(nigga)
            await ctx.reply(f"{user_name} doesn't exist 😢")

def prepare(bot):
    bot.add_cog(User(bot))