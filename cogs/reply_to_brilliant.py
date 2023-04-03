from curses.panel import bottom_panel
import discord
from discord.ext import commands


class brilliant(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._cd = commands.CooldownMapping.from_cooldown(1, 60.0, commands.BucketType.member) # Change accordingly
                                                        # rate, per, BucketType
    
    def ratelimit_check(self, message):
        """Returns the ratelimit left"""
        bucket = self._cd.get_bucket(message)
        return bucket.update_rate_limit()

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return
        msg = message.content.lower()   
        brilliant = ['brilliant', 'Brilliant', 'brilliant!', 'Brilliant!'] 
        if any(word in msg for word in brilliant):
            retry_after = self.ratelimit_check(message)
            if retry_after is None:
                await message.channel.send("Brilliant!")
                await self.bot.process_commands(message)
            elif message.author.id == 155736840387821569:
                await message.channel.send("Brilliant!")
                await self.bot.process_commands(message)
            else:
                return

async def setup(bot):
    await bot.add_cog(brilliant(bot))