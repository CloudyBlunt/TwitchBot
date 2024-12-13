from twitchio.ext import commands
import random
import requests
import json

class Ball(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases = ("8ball", "8b"))
    @commands.cooldown(1, 2, commands.Bucket.user)
    async def ball(self, ctx: commands.Context):
        self.user_langs = self.load_user_langs()
        user_lang = self.user_langs.get(ctx.author.name, "en")
        balls = ("It is certain.",
        "It is decidedly so.", 
        "Without a doubt.",
        "Yes - definitely.",
        "You may rely on it.",
        "As I see it, yes.",
        "Most likely.",
        "Outlook good.",
        "Yes.",
        "Signs point to yes.",
        "Reply hazy, try again.",
        "Ask again later.",
        "Better not tell you now.",
        "Cannot predict now.",
        "Concentrate and ask again.",
        "Don't count on it.",
        "My reply is no.",
        "My sources say no.",
        "Outlook not so good.",
        "Very doubtful",)
        ball = random.choice(balls)
        message = ball
        if user_lang != "en":
            target = message
            langpair = f"en|{user_lang}"
            response = requests.get(f"https://api.mymemory.translated.net/get?q={target}&langpair={langpair}&de=")
            if response.status_code == 200:
                translated = response.json()["responseData"]["translatedText"]
                await ctx.reply(f"🔮 {translated}")
            else:
                await ctx.reply(f"🔮 {response.status_code}")
        else:
            await ctx.reply(f"🔮 {message}")

    def load_user_langs(self):
        try:
            with open('user_langs.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return {}

def prepare(bot):
    bot.add_cog(Ball(bot))
