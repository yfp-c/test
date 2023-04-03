import discord, random
from discord.ext import commands

# colours = ['White', 'Yellow', 'Blue', 'Red', 'Green', 'Black', 'Brown', 'Azure', 'Ivory', 'Teal', 'Silver', 'Purple', 'Navy', 'Grey', 'Orange', 'Maroon']

class random_colour(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context = True , aliases=['rc', 'randomcolour'])
    @commands.cooldown(1, 21600, commands.BucketType.user)
    async def colour(self, ctx):
        with open("./cogs/randomcolours/randomcolours.txt", "r") as file:
            allText = file.readlines()
            words = list(map(str, allText))
            await ctx.reply(f"Greetings {ctx.author.name}...\n"
            f"Your colour today is: **{random.choice(words)}**")

async def setup(bot):
    await bot.add_cog(random_colour(bot))