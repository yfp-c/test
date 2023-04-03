import discord, random
from discord.ext import commands

class quotes(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context = True , aliases=['q', 'quotes'])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def quote(self, ctx):

        quotes = ['Viveeeeeek!',
    'Brilliant, I am so proud of you guys..',
    "let's give a woooww moment to .....",
    "He's gone above and beyond!",
    'This is your show, take it away!',
    "You need to sell yourself in front of the clients",
    "Amazing job you guys!",
    "We need to do some interview prep",
    "How you doing Fred?",
    "How you doing Latif?",
    "How was lunch?",
    "Good Moooooornnnning!!! How you guys doing today?",
    "Share your GitHub repo by the close of business today",
    "Let's do the daily standup",
    "There is no one in this class who is not capable to finish this task",
    "Always go to the official documentation",
    "Vladimir!",
    "Is this readable for everyone?",
    "What's the score on the board?",
    "👍",
    "👏",
    "yaqooob!",
    "Can you zoom in? I can't see",
    "Hello.",
    "Good job",
    "Good luck!",
    "Amazing",
    "brilliant!",
    "I'll add the diagram to trello",
    "In the interest of time..",
    "Perfect",
    "Monitoring team, best team ever!",
    "Proud of you",
    "Share your screen",
    "Zilaaamooo! What is he showing? God knows what hes showing. Is that the ceiling? Zilaamo, is everything okay?",
    "Who would like to share their screen? No one? I like the enthusiasm in this class.",
    "Go for it",
    "You guys have done a cracking job",
    "His magic word is yeye",
    "Consider this as a learning experience",
    "There's 11 of you and you can't fix this blocker?",
    "Time for lunch",
    "Breaks boost productivity",
    "Globally available, highly scalable",
    "Eat some chocolate (To Vlad when he had a migraine)",
    "Can you follow along or are you somewhere else [Zilamo]?",
    "Let's go back to the diagram",
    "No invitation has been received by the grace of god",
    "I can't remember the name of the client",
    "What's the progress?",
    "HELLOO!",
    "This is an excellent example of Effective. Communication.",
    "Monday is busy busy busy busy busy",
    "That's another bonus, cherry on the cake",
    "If you have any questions, fire away",
    "Believe in yourself man!",
    "What makes you stand out in the crowd",
    "If you want to do it yourself, by all means do it",
    "You need a space shuttle to go to sky!",
    "How would people feel that you're using ramadan?",
    "Type your name in the chat, full name",
    "Am I daydreaming? I can't be",
    "Armaan why are you worried? You're gone",
    "I gave him a thumbs up",
    "I type very hard on the keyboard",
    "The rest is destiny",
    "Anybody home?",
    "It's not rocket science, anybody can build a bot.",
    "The ball is in your court",
    "He's the same guy asking for the same people, what's wrong with him?",
    "Market yourself",
    "Don't worry about the money Armaan, the money will come"
    ]    

        # if message.content.startswith('!q'):
        await ctx.reply(random.choice(quotes))


async def setup(bot):
    await bot.add_cog(quotes(bot))