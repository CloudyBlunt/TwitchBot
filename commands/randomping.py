from twitchio.ext import commands
import random
import requests

class Randomping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases = ("rp",))
    @commands.cooldown(1, 1, commands.Bucket.user)
    async def randomping(self, ctx: commands.Context, *, word=None):
        chatters_list = list(ctx.channel.chatters)
        random_chatter = random.choice(chatters_list)
        random_chatter_name = random_chatter.name
        emotes = ('🥺', '😍', '😂', '😱', '😳', '🤯', '😤', '🤢', '🤡', '👻', '😿', '😹', 'Stare', 'peepoHappy', 'ApuApustaja', 'FeelsOkayMan', 'FeelsStrongMan', 'FeelsWeirdMan', 'FeelsDankMan', 'Gayge', 'bUrself', '4Head', '💀', '☠️', '🤩', '🥳', '🤓', '😎', ':tf:','😒', '😏', '😬', '🙄', 'AlienDance', 'VisLaud', 'LuL', 'UwU')
        emote = random.choice(emotes)
        if word is None:             
            await ctx.send(f'{emote} {random_chatter_name}')         
        else:             
            await ctx.send(f'{random_chatter_name} {word}')

def prepare(bot):
    bot.add_cog(Randomping(bot))
