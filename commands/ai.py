from twitchio.ext import commands
from gpt4all import GPT4All
import time
import requests
import json
import os


class Gpt(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases = ("gpt", "chat"))
    @commands.cooldown(1, 5, commands.Bucket.user)
    async def ai(self, ctx, *, input):
        self.user_langs = self.load_user_langs()
        user_lang = self.user_langs.get(ctx.author.name, "en")
        start_time = time.time()
        await ctx.reply(f"Chatting")
        try:
            model = GPT4All("qwen2-1_5b-instruct-q4_0.gguf")
            with model.chat_session():
                message = (model.generate(f'{input}', max_tokens=95))
            if len(message) > 500:
                response = requests.post("https://paste.ivr.fi/documents", data=message)
                if response.status_code == 200:
                    key = response.json()["key"]
                    link = f"https://paste.ivr.fi/raw/{key}"
                    await ctx.reply(f'Output is too long. Uploading to: {link}')
                return
            if user_lang != "en":
                target = message
                langpair = f"en|{user_lang}"
                response = requests.get(f"https://api.mymemory.translated.net/get?q={target}&langpair={langpair}&de=")
                if response.status_code == 200:
                    translated = response.json()["responseData"]["translatedText"]
                    await ctx.reply(f">{translated.upper()}")
                    end_time = time.time()
                    elapsed_time = end_time - start_time
                    print(f"Executed in {elapsed_time:.2f} seconds.")
                else:
                    await ctx.reply(f"{response.status_code}")
            else:
                await ctx.reply(f">{message.upper()}")
                end_time = time.time()  
                elapsed_time = end_time - start_time
                print(f"Executed in {elapsed_time:.2f} seconds.")
        except Exception as a:
            print(f"{a}")
            await ctx.reply(f"{a}")
        return

    def load_user_langs(self):
        try:
            with open('user_langs.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return {} 

def prepare(bot):
    bot.add_cog(Gpt(bot))
