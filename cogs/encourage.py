import discord
from discord.ext import commands
import random

sad_words = ['sad', 'depressed', 'unhappy', 'angry', 'miserable']

starter_encouragements = [
    'Cheer up!',
    'Hang in there.',
    'You are a great person!',
    'Believe in yourself, man!',
    "When the going gets tough, don't give up!"
]

class Encourage(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._cd = commands.CooldownMapping.from_cooldown(1, 120.0, commands.BucketType.member)
    
    # Method to check rate limit    
    def ratelimit_check(self, message):
        """Returns the ratelimit left"""
        bucket = self._cd.get_bucket(message)
        return bucket.update_rate_limit()
    
    # Method to check if any sad words are in the message
    def has_sad_words(self, msg):
        return any(word in msg for word in sad_words)

    def get_sad_word(self, msg):
        for word in sad_words:
            if word in msg:
                return word
        return None
    
    # Listener to process messages and respond with encouragements
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return
        msg = message.content.lower()
        sad_word = self.get_sad_word(msg)
        if sad_word:
            retry_after = self.ratelimit_check(message)
            if retry_after is None:
                encouragement = random.choice(starter_encouragements)
                response = f"You said you are {sad_word}? Well don't be.. {encouragement}"
                await message.reply(response)
                await self.bot.process_commands(message)
            else:
                return

async def setup(bot):
    await bot.add_cog(Encourage(bot))

# old
# import discord
# from discord.ext import commands
# import random

# sad_words = ['sad', 'depressed', 'unhappy', 'angry', 'miserable']

# starter_encouragements = [
#   'Cheer up!',
#   'Hang in there.',
#   'You are a great person!',
#   'Believe in yourself man!',
#   "When the goings get tough, don't give up!"
# ]

# class encourage(commands.Cog):
#     def __init__(self, bot):
#         self.bot = bot
#         self._cd = commands.CooldownMapping.from_cooldown(1, 120.0, commands.BucketType.member) # Change accordingly

#     def ratelimit_check(self, message):
#         """Returns the ratelimit left"""
#         bucket = self._cd.get_bucket(message)
#         return bucket.update_rate_limit()

#     @commands.Cog.listener()
#     async def on_message(self, message):
#         if message.author == self.bot.user:
#             return
#         msg = message.content.lower()
#         if any(word in msg for word in sad_words):
#             retry_after = self.ratelimit_check(message)
#             if retry_after is None:
#                 await message.channel.send(random.choice(starter_encouragements))
#                 await self.bot.process_commands(message)                              
#             else:
#                 return

# async def setup(bot):
#     await bot.add_cog(encourage(bot))