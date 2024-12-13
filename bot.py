from twitchio.ext import commands
from datetime import datetime
from pathlib import Path
import pyspeedtest
import platform
import subprocess
import psutil
import shutil
import asyncio
import time
import json
import requests
import random
import os
start_time = time.time()

class soyjakbot(commands.Bot):
    def __init__(self):
        with open('api_keys.json') as f:
            data = json.load(f)
        twitchtoken = data['twitchtoken']
        super().__init__(token=twitchtoken, prefix='~', initial_channels=[])
        for command in [path.stem for path in Path("commands").glob("*py")]:
            self.load_module(f"commands.{command}")
            self.user_langs = {}

    async def event_ready(self):
        print('Ready')
        await bot.get_channel('').send(f"/me W-Weconnyected~~ UwU")
        loop = asyncio.get_event_loop()
        loop.create_task(self.test('zulul'))
        
    async def test(self, channel_name):
        while True:
            channel = self.get_channel(channel_name)
            url_2 = f'https://7tv.io/v3/users/twitch/1234567890' #insert your channel id here
            response_2 = requests.get(url_2)
            data_2 = response_2.json()
            set_id = data_2['emote_set']['id']

            url = f'https://7tv.io/v3/emote-sets/{set_id}'
            response = requests.get(url)
            data = response.json()

            count = data['emote_count']
            random_emote1 = random.randint(0, count)
            test = data['emotes'][random_emote1]['name']
            await bot.get_channel("YOUR_CHANNEL_NAME_TO_SEND_EMOTES_TO").send(f'{test}',)
            await asyncio.sleep(7200)

    async def event_message(self, message):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        try: 
            print(f"({message.channel.name}) [{current_time}] {message.author.name}: {message.content}")
        except AttributeError:
            print(f"({message.channel.name}) [{current_time}] Soyjakbot: {message.content}")
            return
        await self.handle_commands(message)

    async def event_command_error(self, ctx, error: Exception) -> None:
        if isinstance(error, commands.CommandOnCooldown):
            if error.command.name == "jak":
                random_thing = (
                f"No 'jaks for you ✋ ⏳ 25 minutes cooldown",
                "noooo you can't 😭😭😭😭 ⏳ 25 minutes cooldown",
                "You are on the CIA watchlist for now ⏳ 25 minutes cooldown", 
                "I'm tired boss PoroSad ⏳ 25 minutes cooldown", 
                "Fuck you 🖕 ⏳ 25 minutes cooldown", 
                )
                text = random.choice(random_thing)
                await ctx.reply(text)
            if error.command.name == "sell":
                random_thing = (
                f"Banned from the jak auction ✋ ⏳ 1 hour cooldown",
                "Out of stock ⏳ 1 hour cooldown",
                )
                text = random.choice(random_thing)
                await ctx.reply(text)

        
    @commands.command()
    async def dev(self, ctx: commands.Context, action, *, name: str = None):
        if ctx.author.id == "1234567890": #insert your channel id here to use the dev commands
            if action.startswith("reload"):
                try:
                    self.reload_module(f'commands.{name}')
                    await ctx.reply(f'Module "{name}" successfully reloaded')
                except Exception as e:   
                    await ctx.reply(f"{e}")
                return
            if action.startswith("load"):
                try:
                    self.load_module(f'commands.{name}')
                    await ctx.reply(f'Module "{name}" successfully loaded')
                except Exception as e:   
                    await ctx.reply(f"{e}")
                return
            if action.startswith("unload"):
                try:
                    self.unload_module(f'commands.{name}')
                    await ctx.reply(f'Module "{name}" successfully unloaded')
                except Exception as e:   
                    await ctx.reply(f"{e}")
                return
            if action.startswith("cmd"):
                try:
                    message = subprocess.getoutput(f'{name}')
                    await ctx.send(f"{message}")
                except Exception as e:   
                    await ctx.reply(f"{e}")
                return
            if action.startswith("sys"):
                try:
                    ram = psutil.virtual_memory()
                    ram_used = ram.total - ram.available
                    ram_percent = 100 * float(ram_used)/float(ram.total)
                    swap = psutil.swap_memory()
                    swap_percent = swap.percent
                    cpu = psutil.cpu_percent()
                    cpu_freqs = psutil.cpu_freq()
                    freq_current = cpu_freqs.current
                    freq_minimum = cpu_freqs.min
                    freq_maximum = cpu_freqs.max
                    cpu_usage_per_core = psutil.cpu_percent(interval=1, percpu=True)
                    dev_pc_uptime = subprocess.getoutput('uptime -p')
                    address = pyspeedtest.SpeedTest("www.twitch.tv")
                    ping_ms = address.ping()
                    python = platform.python_version()
                    uptime = time.time() - start_time
                    hours, remainder = divmod(uptime, 3600)
                    minutes, seconds = divmod(remainder, 60)
                    await ctx.reply(f"CPU: {cpu}% {freq_current:.1f}MHz, Minimum: {freq_minimum:.2f}MHz, Maximum: {freq_maximum:.2f}MHz. | RAM: {ram_percent:.1f}% Used: {ram_used / 1024 / 1024 / 1024:.2f}GB Free: {ram.available / 1024 / 1024 / 1024:.2f}GB, Total {ram.total / 1024 / 1024 / 1024:.4} GB | SWAP: {swap_percent}% | Is {dev_pc_uptime} | {ping_ms:.4} ms | Python {python} | Main script is running for {int(hours)} hours {int(minutes)} minutes {int(seconds)} seconds |")
                except Exception as e:   
                    await ctx.reply(f"{e}")
                return
        else:
            return

bot = soyjakbot()
asyncio.run(bot.run())
