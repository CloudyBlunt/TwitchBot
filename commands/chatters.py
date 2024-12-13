from twitchio.ext import commands
import requests

class Chatters(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(1, 5, commands.Bucket.user)
    async def chatters(self, ctx: commands.Context, word: str = None):
        if word is None:
            channel_name = ctx.channel.name
        else:
            channel_name = word
        try:
            url = f"https://api.markzynk.com/twitch/chatters/{channel_name}"
            data = requests.get(url, timeout=3).json()
        except requests.exceptions.Timeout:
            try:
                chatters = list(ctx.channel.chatters)
                nicknames = [user.name for user in chatters]
                usernames = '\n'.join(nicknames)
                total = len(chatters)
                text = f"Total: {total} \n \n \n{usernames}"
                response = requests.post("https://paste.ivr.fi/documents", data=text)
                if response.status_code == 200:
                    key = response.json()["key"]
                    link = f"https://paste.ivr.fi/{key}"
                    await ctx.reply(f'Chatters: {total} | {link}')
                    return
            except Exception as oi:
                await ctx.reply(f"{oi}")
                return
        else:        
            moderators = data["chatters"].get('moderators', [])
            vips = data["chatters"].get('vips', [])
            viewers = data["chatters"].get('viewers', [])
            broadcasters = data["chatters"].get('broadcasters', [])

            total_chatters = (
                len(moderators) +
                len(vips) +
                len(viewers) +
                len(broadcasters)
                )

            total_moderators = (
                len(moderators)
                )

            total_viewers = (
                len(viewers)
                )

            total_vips = (
                len(vips)
                )

            chatters_list = []
            chatters_list.append(f"Chatters count: {total_chatters}\n")

            chatters_list.append(f"\nBroadcasters {len(broadcasters)}:\n")
            chatters_list.extend(broadcasters)

            chatters_list.append(f"\nModerators {len(moderators)}:\n")
            chatters_list.extend(moderators)

            chatters_list.append(f"\nVIPs {len(vips)}:\n")
            chatters_list.extend(vips)

            chatters_list.append(f"\nViewers {len(viewers)}:\n")
            chatters_list.extend(viewers)

            text = "\n".join(chatters_list)
        
            response = requests.post("https://paste.ivr.fi/documents", data=text, headers={"Content-Type": "text/plain"})
        
            if total_chatters == 0:
                await ctx.reply(f"@{word} has no chatters 😔😢")
            else:
                if response.status_code == 200:
                    key = response.json()["key"]
                    link = f"https://paste.ivr.fi/{key}"
            await ctx.reply(f'» {total_chatters} chatters [{total_moderators} Moderators | {total_vips} Vips | {total_viewers} Viewers] | {link}')

def prepare(bot):
    bot.add_cog(Chatters(bot))