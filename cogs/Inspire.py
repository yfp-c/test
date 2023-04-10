import discord
import json
import requests
from discord.ext import commands

class InspirationalQuotes(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Method to fetch an inspirational quote from the ZenQuotes API
    def get_quote(self):
        response = requests.get("https://zenquotes.io/api/random")
        json_data = json.loads(response.text)
        quote = json_data[0]['q'] + " -" + json_data[0]['a']
        return quote

    # Listener to ignore bot's own messages (optional, you can remove this if you don't need it)
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return

    # Command to fetch and send an inspirational quote
    @commands.command()
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def inspire(self, ctx):
        # Call the get_quote method to fetch an inspirational quote
        quote = self.get_quote()
        # Send the quote as a reply
        await ctx.reply(quote)

async def setup(bot):
    await bot.add_cog(InspirationalQuotes(bot))

# old
# import discord, json
# from discord.ext import commands
# import requests

# class inspirational_quotes(commands.Cog):
#     def __init__(self, bot):
#         self.bot = bot

#     def get_quote(self):
#         response = requests.get("https://zenquotes.io/api/random")
#         json_data = json.loads(response.text)
#         quote = json_data[0]['q'] + " -" + json_data[0]['a']
#         return(quote)


#     @commands.Cog.listener()
#     async def on_message(self, message):
#         if message.author == self.bot.user:
#             return
#     @commands.command()
#     @commands.cooldown(1, 10, commands.BucketType.user)
#     async def inspire(self, ctx):
#         quote = self.get_quote()
#         await ctx.reply(quote)

# async def setup(bot):
#     await bot.add_cog(inspirational_quotes(bot))