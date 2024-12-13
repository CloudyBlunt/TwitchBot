from twitchio.ext import commands
import json
import requests
import random

class jaks(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.points = self.load_points()
        self.ranks = self.load_ranks()
        self.user_langs = {}

    @commands.command()
    @commands.cooldown(1, 2, commands.Bucket.user)
    async def jaks(self, ctx: commands.Context):
        try:
            user = ctx.message.content.split()[1]
        except IndexError:
            user = ctx.author.name

        if user not in self.points:
            self.points[user] = 10
        if user not in self.ranks:
                self.ranks[user] = 1

        points = self.points[user]
        rank = self.ranks[user]
        sorted_users = sorted(self.points.items(), key=lambda x: self.ranks.get(x[0], 0), reverse=True)
        place = sorted_users.index((user, points)) + 1
        message = f"{user} {points} 'jaks [Rank:{rank}] | Place in leaderboard: {place}"
        await ctx.reply(message)

    def load_points(self):
        with open('points.json', 'r') as f:
            return json.load(f)

    def load_ranks(self):
        with open('ranks.json', 'r') as f:
            return json.load(f)


    @commands.command()
    @commands.cooldown(1, 1500, commands.Bucket.user)
    async def jak(self, ctx: commands.Context):
        self.user_langs = self.load_user_langs()
        user_lang = self.user_langs.get(ctx.author.name, "en")
        user = ctx.author.name
        if user not in self.points:
            self.points[user] = 5

        if user not in self.ranks:
                self.ranks[user] = 1
        random_points = random.randint(-20, 50)
        self.points[user] += random_points

        if random_points > 1:
            random_thing = (
            f">I hate all normalfags, they fuckin suck \\\ NormGODS won keep seething autist ^",   
            ">russian bvlls are now using T-34s for training oh my FUCKING science ^", 
            'It s funny how chuds say shit like "TND" when all of them look like this and cant even talk to another person let alone kill one. ^',
            "amerimutts are white and aryan o algo ^",
            ">Chud United States 4 hours ago >I am a mormon and mormonism is thr only good branch of christianity and hitler was mormon ^",
            ">slavs are just the free trial version of being white ^",
            ">>552685 We've existed far before you, and will continue to exist far after, mutt ^",
            )
        else: 
            random_thing = (
            f">>552687 Your ethnicity is the slut of the world, mixture of Old Persians, Akkadians, Babylonians, Elamites, Azerbaijanis, Turks, Greeks, and Mongols",
            ">>552727 GEEEEG i googled white iranian and this was the second result",
            ">>546537 Have fun giving aids to your aryan wife", 
            )      
        
        text = random.choice(random_thing)
        message = f'{text} {random_points}. | {self.points[user]} Total'
        if user_lang != "en":
            target = message
            langpair = f"en|{user_lang}"
            response = requests.get(f"https://api.mymemory.translated.net/get?q={target}&langpair={langpair}&de=")
            if response.status_code == 200:
                translated = response.json()["responseData"]["translatedText"]
                fixed = translated.replace("^", "+")
                await ctx.reply(fixed)
            else:
                await ctx.reply(f"{response.status_code}")
        else:
            fixed2 = message.replace("^", "+")
            await ctx.reply(fixed2)

        self.save_points()

    def load_points(self):
        try:
            with open('points.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return {} 

    def save_points(self):
        with open('points.json', 'w') as f:
            json.dump(self.points, f)

    def load_ranks(self):

        try:
            with open('ranks.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return {} 

    def save_ranks(self):

        with open('ranks.json.json', 'w') as f:
            json.dump(self.ranks, f)

    def load_user_langs(self):
        try:
            with open('user_langs.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return {}


    @commands.command()
    @commands.cooldown(1, 3600, commands.Bucket.user)
    async def sell(self, ctx: commands.Context):
        self.user_langs = self.load_user_langs()
        user_lang = self.user_langs.get(ctx.author.name, "en")
        user = ctx.author.name
        if user not in self.points:
            self.points[user] = 5
        random_points = random.randint(30, 400)
        self.points[user] += random_points
         
        if random_points < 150:
            random_emote = (
            f"🤣", 
            "👎", 
            "😹", 
            "😹", 
            "🐖💨",
            "🤡 ",
            "🤮",
            "🤢",
            "😢",
            "😨",
            "DansGame",
            "BibleThump",
            ":tf:",
            "haHAA",
            "peepoSad",
            )
        else: 
            random_emote = (
            f"😱",
            "😳", 
            "🙀",
            "PogBones",
            "🥰", 
            "😊", 
            "😘", 
            "😍", 
            "👍", 
            "😼",     
            "☺️", 
            "🤤", 
            "B)", 
            "EZ", 
            "peepoHappy", 
            "FeelsOkayMan", 
            )  

        emote = random.choice(random_emote)
        message = f"You have placed your gemmy 'jaks to the 'ru and someone just upvoted them! +{random_points} {emote} | {self.points[user]} Total"
        
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

        self.save_points()

    def load_points(self):
        try:
            with open('points.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return {} 

    def save_points(self):
        with open('points.json', 'w') as f:
            json.dump(self.points, f)

    def load_user_langs(self):
        try:
            with open('user_langs.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return {}


    @commands.command()
    @commands.cooldown(1, 2, commands.Bucket.user)
    async def bet(self, ctx: commands.Context):
        user = ctx.author.name
        if user not in self.points:
            self.points[user] = 5
        try:
            amount = int(ctx.message.content.split()[1])
        except (IndexError, ValueError):
            not_valid_random = (
            f"That doesn't quite look like a valid number FeelsWeirdMan",
            "Not a valid number 🤨",
            )
            text = random.choice(not_valid_random)
            await ctx.reply(text)
            return

        if amount > self.points[user]:
            broke = (
            f"You don't have that many 'jaks to bet",
            "Too poor to bet 😭 ",
            )
            text = random.choice(broke)
            await ctx.reply(text)
            return
        
        if amount < 1:
            emotes = ("FeelsBadMan", "haHAA", "FeelsWeirdMan", "FeelsDankMan", "peepoSad", "Stare")
            emote = random.choice(emotes)
            await ctx.reply(f"You can't bet nothing {emote}")
            return

        random_chance = random.random()
        if random_chance < 0.5:
            winnings = amount * 1
            self.points[user] += winnings
            emotes = ("Clap", "WAYTOODANK", "EZ", "AlienDance", "FeelsStrongMan", "peepoHappy", "FeelsGoodMan", ":-D", "VisLaud")
            emote = random.choice(emotes)

            won_random = (
            f"Your bet has won PogBones",
            "PogBones PogBones PogBones !!!",
            )

            won_text = random.choice(won_random)
            await ctx.reply(f"{won_text} +{winnings} 'jaks | Now you have {self.points[user]} {emote}")
        else:
            self.points[user] -= amount
            emotes = ("peepoSad", "WAYTOODANK", "NotLikeThis", "FallCry", "BibleThump", "FeelsWeirdMan")
            emote = random.choice(emotes)
            lost_random = (
            f"Betting your 'jaks you flew too close to the sun FeelsBadMan",
            "That was way too self confident 😔",
            "Dumb people are often happier than the smart ones, but you are the exception 😂",
            )
            lost_text = random.choice(lost_random)
            await ctx.reply(f"{lost_text} -{amount} 'jaks | Now you have {self.points[user]} {emote}")
        self.save_points()

    def load_points(self):
        try:
            with open('points.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return {} 
        
    def save_points(self):
        with open('points.json', 'w') as f:
            json.dump(self.points, f)

    def load_user_langs(self):
        try:
            with open('user_langs.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return {}

    @commands.command()
    @commands.cooldown(1, 5, commands.Bucket.user)
    async def top(self, ctx: commands.Context):
        self.user_langs = self.load_user_langs()
        user_lang = self.user_langs.get(ctx.author.name, "en")
        sorted_users = sorted(self.points.items(), key=lambda x: self.ranks.get(x[0], 0), reverse=True)

        message = ""

        for i in range(6):

            user = sorted_users[i][0]
            points = sorted_users[i][1]

            if user not in self.ranks:
                self.ranks[user] = 1

            rank = self.ranks[user]

            message += f"{i+1}.{user} - [Rank: {rank}] {points} | \n"

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

    def load_points(self):
        with open('points.json', 'r') as f:
            return json.load(f)


    def save_points(self):

        with open('points.json', 'w') as f:
            json.dump(self.points, f)

    def load_ranks(self):
        with open('ranks.json', 'r') as f:
               return json.load(f)

    def save_ranks(self):

        with open('ranks.json', 'w') as f:
            json.dump(self.ranks, f)

    def load_user_langs(self):
        try:
            with open('user_langs.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return {}

    @commands.command()
    @commands.cooldown(1, 3, commands.Bucket.user)
    async def give(self, ctx: commands.Context):
        sender = ctx.author.name

        if sender not in self.points:
            self.points[sender] = 10
        try:
            recipient = ctx.message.content.split()[1]
            amount = int(ctx.message.content.split()[2])
        except (IndexError, ValueError):
            await ctx.reply(f"You need to provide a valid user and amount of 'jaks to give")
            return

        if amount > self.points[sender]:

            await ctx.reply(f"You don't have enough 'jaks")
            return


        if recipient not in self.points:
            await ctx.reply(f"This user doesn't exist")
            return

        self.points[sender] -= amount
        self.points[recipient] += amount

        await ctx.reply(f"You have {self.points[sender]} 'jaks! You gave {amount} 'jaks to {recipient} who now has {self.points[recipient]} 'jaks")

        self.save_points()

    def load_points(self):

        try:
            with open('points.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return {} 

    def save_points(self):
        with open('points.json', 'w') as f:
            json.dump(self.points, f)


    @commands.command()
    @commands.cooldown(1, 1, commands.Bucket.user)
    async def rankup(self, ctx: commands.Context):
        user = ctx.author.name

        if user not in self.points:
            self.points[user] = 10

        if user not in self.ranks:
            self.ranks[user] = 0

        points = self.points[user]

        cost = 10000
        if points < cost:

            await ctx.reply(f"You don't have enough 'jaks to rankup (5000)")
            return

        self.points[user] -= cost
        self.ranks[user] += 1


        await ctx.reply(f'You have {self.points[user]} and [{self.ranks[user]}] now')

        self.save_points()
        self.save_ranks()

    def load_points(self):
        try:
            with open('points.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return {} 

    def save_points(self):

        with open('points.json', 'w') as f:
            json.dump(self.points, f)

    def load_ranks(self):

        try:
            with open('ranks.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return {} 

    def save_ranks(self):

        with open('ranks.json', 'w') as f:
            json.dump(self.ranks, f)

def prepare(bot):
    bot.add_cog(jaks(bot))
