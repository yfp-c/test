import discord
from discord.ext import commands
from curses.panel import bottom_panel

vivek = ['vivek', 'viveek', 'viveeek', 'viveeeek', 'viveeeeek',
'viveeeeeek', 'viveeeeeeek', 'viveeeeeeeek', 'viveeeeeeeeek', 'viveeeeeeeeeek',
'viveeeeeeeeeeek', 'viveeeeeeeeeeeek', 'viveeeeeeeeeeeeek', 'viveeeeeeeeeeeeeek',
'viveeeeeeeeeeeeeeek', 'viveeeeeeeeeeeeeeeek', 'viveeeeeeeeeeeeeeeeek',
'viveeeeeeeeeeeeeeeeeek', 'viveeeeeeeeeeeeeeeeeeek', 'viveeeeeeeeeeeeeeeeeeeek',
'viveeeeeeeeeeeeeeeeeeeeek', 'viveeeeeeeeeeeeeeeeeeeeeek', 'viveeeeeeeeeeeeeeeeeeeeeeek',
'viveeeeeeeeeeeeeeeeeeeeeeeek', 'viveeeeeeeeeeeeeeeeeeeeeeeeek', 'viveeeeeeeeeeeeeeeeeeeeeeeeeek', 'viveeeeeeeeeeeeeeeeeeeeeeeeeeek',
'vivek!', 'viveek!', 'viveeek!', 'viveeeek!', 'viveeeeek!', 'viveeeeeek!', 'viveeeeeeek!', 'viveeeeeeeek!', 'viveeeeeeeeek!', 'viveeeeeeeeeek!',
'viveeeeeeeeeeek!', 'viveeeeeeeeeeeek!', 'viveeeeeeeeeeeeek!', 'viveeeeeeeeeeeeeek!', 'viveeeeeeeeeeeeeeek!', 'viveeeeeeeeeeeeeeeek!', 'viveeeeeeeeeeeeeeeeek!',
'viveeeeeeeeeeeeeeeeeek!', 'viveeeeeeeeeeeeeeeeeeek!', 'viveeeeeeeeeeeeeeeeeeeek!', 'viveeeeeeeeeeeeeeeeeeeeek!', 'viveeeeeeeeeeeeeeeeeeeeeek!', 'viveeeeeeeeeeeeeeeeeeeeeeek!',
'viveeeeeeeeeeeeeeeeeeeeeeeek!', 'viveeeeeeeeeeeeeeeeeeeeeeeeek!', 'viveeeeeeeeeeeeeeeeeeeeeeeeeek!', 'viveeeeeeeeeeeeeeeeeeeeeeeeeeek!']

class viveeeeek(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._cd = commands.CooldownMapping.from_cooldown(1, 60.0, commands.BucketType.member) # Change accordingly
    
    def ratelimit_check(self, message):
        """Returns the ratelimit left"""
        bucket = self._cd.get_bucket(message)
        return bucket.update_rate_limit()

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return
        msg = message.content.lower()         
        if any(word in msg for word in vivek):
            retry_after = self.ratelimit_check(message)
            if retry_after is None:
                await message.channel.send("Viveeeeeeeeeeeeeeeeeek!")
                await self.bot.process_commands(message)
            else:
                return

async def setup(bot):
    await bot.add_cog(viveeeeek(bot))