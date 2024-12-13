from twitchio.ext import commands
import datetime
import requests
import json
import os
import pytz
class Weather(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.user_langs = self.load_user_langs()

    @commands.command(aliases = ("погода", "w"))
    @commands.cooldown(1, 2, commands.Bucket.user)
    async def weather(self, ctx: commands.Context, city: str = None):  
        with open('api_keys.json') as f:
            data = json.load(f)
        
        openweathermapkey = data['openweathermap']

        api_key = openweathermapkey
        with open("locations.json", "r") as f:
            locations = json.load(f)
        if city is None:
            user_id = ctx.author.id
            if user_id in locations:
                city = locations[user_id]
            else:
                await ctx.reply(f'Please provide a city name or use #set location to save your location.')
                return
        try:
            self.user_langs = self.load_user_langs()
            user_lang = self.user_langs.get(ctx.author.name, "en")
            url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang={user_lang}'
            data = requests.get(url, timeout=10).json()
        except requests.exceptions.Timeout:
            await ctx.reply(f"Connection timed out 😭 ☠️")
        else:
            if data['cod'] != 200:
                await ctx.reply(f"I couldn't find this place 😔")
                return

            temp = data['main']['temp']
            feels_like = data['main']['feels_like']
            humidity = data['main']['humidity']
            wind_speed = data['wind']['speed']
            cloudscover = data['clouds']['all']
            pressure = data['main']['pressure']
            description = data['weather'][0]['description']
            name = data['name']

            if data['clouds']['all'] > 0:
                message = f'{name}: {description} 🌤 Temperature {temp}°C, Feels like {feels_like}°C, Humidity {humidity}%, Air pressure: {pressure}hPa, Cloud cover {cloudscover}%,  Wind speed {wind_speed} m/s.'
                if user_lang != "en":
                    target = message
                    langpair = f"en|{user_lang}"
                    response = requests.get(f"https://api.mymemory.translated.net/get?q={target}&langpair={langpair}&de=v1ss0nd@yahoo.com")
                    if response.status_code == 200:
                        translated = response.json()["responseData"]["translatedText"]
                        await ctx.reply(translated)
                    else:
                        await ctx.reply(f"{response.status_code}")
                else:
                    await ctx.reply(message)
                    return
            else:
                message = f'{name}: {description} 🌞 Temperature {temp}°C, Feels like {feels_like}°C, Humidity {humidity}%, Air pressure: {pressure}hPa, Cloud cover {cloudscover}%,  Wind speed {wind_speed} m/s.'
                if user_lang != "en":
                    target = message
                    langpair = f"en|{user_lang}"
                    response = requests.get(f"https://api.mymemory.translated.net/get?q={target}&langpair={langpair}&de=")
                    if response.status_code == 200:
                        translated = response.json()["responseData"]["translatedText"]
                        await ctx.reply(translated)
                    else:
                        await ctx.reply(f"{response.status_code}")
                else:
                    await ctx.reply(message)

    def load_user_langs(self):
        try:
            with open('user_langs.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return {} 

def prepare(bot):
    bot.add_cog(Weather(bot))
