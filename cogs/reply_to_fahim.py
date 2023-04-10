import discord
from discord.ext import commands
from time import time
import asyncio

# COOLDOWN_AMOUNT = 10.0  # seconds
# last_executed = time.time()

class fahim_reply(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._cd = commands.CooldownMapping.from_cooldown(1, 604800.0, commands.BucketType.member) # Change accordingly
                                                        # rate, per, BucketType
    

    def ratelimit_check(self, message):
        """Returns the ratelimit left"""
        bucket = self._cd.get_bucket(message)
        return bucket.update_rate_limit()

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return
        if message.author.id == 502069858129805312:
            retry_after = self.ratelimit_check(message)
            if retry_after is None:
                await message.channel.send('Stop docking')
                await self.bot.process_commands(message)
            else:
                return
 

async def setup(bot):
    await bot.add_cog(fahim_reply(bot))