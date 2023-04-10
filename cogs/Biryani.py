import discord
import json
import requests
from discord.ext import commands

class Biryani(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Method to fetch a biryani image URL from the Biryani API
    def get_image_url(self):
        response = requests.get("https://biriyani.anoram.com/get")
        json_data = json.loads(response.text)
        image_url = json_data["image"]
        return image_url

    # Listener to ignore bot's own messages
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return

    # Command to fetch and send a biryani image URL
    @commands.command()
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def biryani(self, ctx):
        # Call the get_image_url method to fetch a biryani image URL
        image_url = self.get_image_url()
        # Send the image URL as a reply
        await ctx.reply(f"{image_url}")

async def setup(bot):
    await bot.add_cog(Biryani(bot))

# old
# import discord, random, json, requests
# from discord.ext import commands

# class biryani(commands.Cog):
#     def __init__(self, bot):
#         self.bot = bot
    
#     def get_quote(self):
#         response = requests.get("https://biriyani.anoram.com/get")
#         json_data = json.loads(response.text)
#         quote = json_data["image"]
#         return(quote)

#     @commands.Cog.listener()
#     async def on_message(self, message):
#         if message.author == self.bot.user:
#             return
#     @commands.command()
#     @commands.cooldown(1, 10, commands.BucketType.user)
#     async def biryani(self, ctx):
#         quote = self.get_quote()
#         await ctx.reply(f"{quote}")

# async def setup(bot):
#     await bot.add_cog(biryani(bot))