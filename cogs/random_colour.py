import discord
import random
from discord.ext import commands

class RandomColour(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Method to read the random colours file and return a random colour
    def get_random_colour(self):
        with open("./cogs/randomcolours/randomcolours.txt", "r") as file:
            allText = file.readlines()
            words = list(map(str, allText))
        return random.choice(words)

    # Command to send a random colour to the user
    @commands.command(pass_context=True, aliases=['rc', 'randomcolour'])
    @commands.cooldown(1, 21600, commands.BucketType.user)
    async def colour(self, ctx):
        # Call the get_random_colour method to fetch a random colour
        random_colour = self.get_random_colour()
        await ctx.reply(f"Greetings {ctx.author.name}...\n"
                        f"Your colour today is: **{random_colour}**")

async def setup(bot):
    await bot.add_cog(RandomColour(bot))

# old
# import discord, random
# from discord.ext import commands


# class random_colour(commands.Cog):
#     def __init__(self, bot):
#         self.bot = bot

#     @commands.command(pass_context = True , aliases=['rc', 'randomcolour'])
#     @commands.cooldown(1, 21600, commands.BucketType.user)
#     async def colour(self, ctx):
#         with open("./cogs/randomcolours/randomcolours.txt", "r") as file:
#             allText = file.readlines()
#             words = list(map(str, allText))
#             await ctx.reply(f"Greetings {ctx.author.name}...\n"
#             f"Your colour today is: **{random.choice(words)}**")

# async def setup(bot):
#     await bot.add_cog(random_colour(bot))