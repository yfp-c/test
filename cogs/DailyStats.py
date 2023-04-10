import discord
import random
import json
import requests
from discord.ext import commands

class DailyStats(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Method to generate a list of random percentages
    def get_percentages(self, count=7):
        return [random.randint(0, 100) for _ in range(count)]

    # Method to fetch a quote from the Kanye West API
    def get_quote(self):
        response = requests.get("https://api.kanye.rest/")
        json_data = json.loads(response.text)
        quote = '"' + json_data['quote'] + '"'
        return quote

    # Method to create a Discord embed with daily stats, quote, and footer
    def create_daily_stats_embed(self, ctx_author_name, percentages, quote):
        embed = discord.Embed(
            colour=(discord.Colour.random()),
            description=f"HELLO {ctx_author_name}, your daily stats percentages are.. \n"
            f"\n"
            f"-Health: **{percentages[0]}%**\n"
            f"-Career: **{percentages[1]}%**\n"
            f"-Happiness: **{percentages[2]}%**\n"
            f"-Productivity: **{percentages[3]}%**\n"
            f"-Luck: **{percentages[4]}%**\n"
            f"-True love probability: **{percentages[5]}%**\n"
            f"-Attractiveness: **{percentages[6]}%**\n"
            f"\n"
            f"{quote} - Kanye West"
        )
        embed.set_footer(text="Note: Extremely accurate.")
        return embed

    # Daily command to show daily stats and a quote
    @commands.command(pass_context=True, aliases=['stats', 'dailystats'])
    @commands.cooldown(1, 21600, commands.BucketType.user)
    async def daily(self, ctx):
        # Call the get_quote method to fetch a quote
        quote = self.get_quote()
        # Call the get_percentages method to generate random percentages
        percentages = self.get_percentages()
        # Call the create_daily_stats_embed method to create the embed message
        embed = self.create_daily_stats_embed(ctx.author.name, percentages, quote)
        # Send the embed message to the user
        await ctx.reply(embed=embed)

async def setup(bot):
    await bot.add_cog(DailyStats(bot))


# old
# import discord, random, json, requests
# from discord.ext import commands

# percentages = [random.randint(0, 100) for _ in range(7)]


# class daily_stats(commands.Cog):
#     def __init__(self, bot):
#         self.bot = bot

#     def get_quote(self):
#         response = requests.get("https://api.kanye.rest/")
#         json_data = json.loads(response.text)
#         quote = '"'+ json_data['quote'] + '"'
#         return(quote)

#     @commands.command(pass_context = True , aliases=['stats', 'dailystats'])
#     @commands.cooldown(1, 21600, commands.BucketType.user)
#     async def daily(self, ctx):
#         quote = self.get_quote()
#         embed = discord.Embed(
#             colour=(discord.Colour.random()),
#             description=f"HELLO {ctx.author.name}, your daily stats percentages are.. \n"
#             f"\n"
#             f"-Health: **{percentages[0]}%**\n"
#             f"-Career: **{percentages[1]}%**\n"
#             f"-Happiness: **{percentages[2]}%**\n"
#             f"-Productivity: **{percentages[3]}%**\n"
#             f"-Luck: **{percentages[4]}%**\n"
#             f"-True love probability: **{percentages[5]}%**\n"
#             f"-Attractiveness: **{percentages[6]}%**\n"
#             f"\n"
#             f"{quote} - Kanye West"
#         )
        
#         embed.set_footer(text="Note: Extremely accurate.")
#         # embed.set_image(url=(random.choice(good_luck)))
#         await ctx.reply(embed = embed)

# async def setup(bot):
#     await bot.add_cog(daily_stats(bot))

