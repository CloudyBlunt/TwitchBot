from twitchio.ext import commands
import pyspeedtest
import time
import psutil
import os
import time
import platform
import socket
start_time = time.time()

class Ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases = ("pong", "peng", "pyng", "pung", "pang"))
    @commands.cooldown(1, 5, commands.Bucket.user)
    async def ping(self, ctx: commands.Context):
        try:
            address = pyspeedtest.SpeedTest("www.twitch.tv")
            ping_ms = address.ping()
            ram = psutil.virtual_memory()
            ram_used = ram.total - ram.available
            cpu = psutil.cpu_percent()
            python_mem = psutil.Process(os.getpid()).memory_info().rss / 1024 ** 2
            uptime = time.time() - start_time
            hours, remainder = divmod(uptime, 3600)
            minutes, seconds = divmod(remainder, 60)
            await ctx.reply(f'/me CPU: {cpu}% | Memory: {python_mem:.1f}MB | RAM: Used {ram_used / 1024 / 1024 / 1024:.2f}GB, {ram.total / 1024 / 1024 / 1024:.4}GB Total | {int(hours)} hours {int(minutes)} minutes {int(seconds)} seconds | Ping {ping_ms:.4}ms')
        except Exception as e:
            await ctx.reply(f'Bot is up, but the script returned an error FeelsBadMan [{e}] ')

def prepare(bot):
    bot.add_cog(Ping(bot))
