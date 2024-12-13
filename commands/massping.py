from twitchio.ext import commands
import random
import requests

class Massping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    @commands.cooldown(1, 15, commands.Bucket.user)
    async def massping(self, ctx: commands.Context, count: int=None, *, word=None):
        if not ctx.author.is_mod:
            return

        if ctx._bot_is_mod() is False:
            await ctx.reply("I have t-to be a moderator to execute t-this command... 🥺")
            return

        if count is None:
            chatters = list(ctx.channel.chatters)
            nicknames = [user.name for user in chatters]
            text = '\n'.join(nicknames) 
            response = requests.post("https://paste.ivr.fi/documents", data=text)
            if response.status_code == 200:
                key = response.json()["key"]
                link = f"https://paste.ivr.fi/{key}"
                await ctx.reply(f':tf: 🤜 🔔 {link}')
                return

        for i in range(count):
            if ctx.author.is_mod:
                if count < 1 or count > 100:
                    return
            chatters_list = list(ctx.channel.chatters)
            random_chatter = random.choice(chatters_list)
            random_chatter_name = random_chatter.name
            emotes = ('🥺', '😍', '😂', '😱', '😳', '🤯', '😤', '🤢', '🤡', '👻', '😿', '😹', 'Stare', 'peepoHappy', 'ApuApustaja', 'FeelsOkayMan', 'FeelsStrongMan', 'FeelsWeirdMan', 'FeelsDankMan', 'gachiGASM', 'Gayge', 'bUrself', '4Head', '💀', '☠️', '🤩', '🥳', '🤓', '😎', ':tf:','😒', '😏', '😬', '🙄', 'AlienDance', 'VisLaud', 'LuL', 'KKona')
            emote = random.choice(emotes)
            if word is None:             
                await ctx.send(f'{emote} 🤜 🔔 {random_chatter_name}')         
            else:             
                await ctx.send(f'{random_chatter_name} {word}')

def prepare(bot):
    bot.add_cog(Massping(bot))
