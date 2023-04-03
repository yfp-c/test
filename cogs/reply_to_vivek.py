import discord
from discord.ext import commands
from time import time
import asyncio

# COOLDOWN_AMOUNT = 10.0  # seconds
# last_executed = time.time()

class vivek_reply(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._cd = commands.CooldownMapping.from_cooldown(1, 86400.0, commands.BucketType.member) # Change accordingly
                                                        # rate, per, BucketType
    

    def ratelimit_check(self, message):
        """Returns the ratelimit left"""
        bucket = self._cd.get_bucket(message)
        return bucket.update_rate_limit()

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return
        if message.author.id == 390000183657758720:
            retry_after = self.ratelimit_check(message)
            if retry_after is None:
                await message.channel.send('Viveeeeeeeeeeeeek!')
                await self.bot.process_commands(message)
            else:
                return
 

async def setup(bot):
    await bot.add_cog(vivek_reply(bot))