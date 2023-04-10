import discord
import datetime
import time
from discord.ext import commands

start_time = time.time()

class Uptime(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Method to calculate the bot's uptime
    def get_uptime(self):
        current_time = time.time()
        difference = int(round(current_time - start_time))
        text = str(datetime.timedelta(seconds=difference))
        return text

    @commands.is_owner()
    @commands.command(pass_context=True)
    async def uptime(self, ctx):
        # Call the get_uptime method to calculate the bot's uptime
        text = self.get_uptime()
        embed = discord.Embed(colour=ctx.message.author.top_role.colour)
        embed.add_field(name="Uptime", value=text)
        embed.set_footer(text="The above is my uptime!")
        try:
            await ctx.send(embed=embed)
        except discord.HTTPException:
            await ctx.send("Current uptime: " + text)

async def setup(bot):
    await bot.add_cog(Uptime(bot))

# old
# import discord, datetime, time
# from discord.ext import commands

# start_time = time.time()


# class Uptime(commands.Cog):
#     def __init__(self, bot):
#         self.bot = bot

#     @commands.is_owner()
#     @commands.command(pass_context=True)
#     async def uptime(self, ctx):
#         current_time = time.time()
#         difference = int(round(current_time - start_time))
#         text = str(datetime.timedelta(seconds=difference))
#         embed = discord.Embed(colour=ctx.message.author.top_role.colour)
#         embed.add_field(name="Uptime", value=text)
#         embed.set_footer(text="The above is my uptime!")
#         try:
#             await ctx.send(embed=embed)
#         except discord.HTTPException:
#             await ctx.send("Current uptime: " + text)


# async def setup(bot):
#     await bot.add_cog(Uptime(bot))