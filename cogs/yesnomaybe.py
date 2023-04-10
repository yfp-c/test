import discord
import requests
import json
import random
from discord.ext import commands

class YesNoMaybe(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Method to get a random yes, no or maybe answer from the API
    def get_api(self):
        response = requests.get("https://yesno.wtf/api")
        json_data = json.loads(response.text)
        answer_gif = json_data["answer"].capitalize() + ".\n" + json_data['image']
        return answer_gif

    # Method to get a 'Yes' answer from the API
    def get_yes(self):
        response = requests.get("https://yesno.wtf/api?force=yes")
        json_data = json.loads(response.text)
        answer_gif = json_data["answer"].capitalize() + ".\n" + json_data['image']
        return answer_gif

    # Command to get a random yes, no or maybe answer
    @commands.command()
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def yesno(self, ctx):
        if ctx.author.id == 155736840387821569:
            api = self.get_yes()
            await ctx.reply(f"{api}")
        else:
            api = self.get_api()
            await ctx.reply(f"{api}")

async def setup(bot):
    await bot.add_cog(YesNoMaybe(bot))

# old
# from curses.panel import bottom_panel
# import discord, requests, json, random
# from discord.ext import commands

# class yesnomaybe(commands.Cog):
#     def __init__(self, bot):
#         self.bot = bot

#     def get_api(self):
#         response = requests.get("https://yesno.wtf/api")
#         json_data = json.loads(response.text)
#         answer_gif = json_data["answer"] + "." + "\n" + json_data['image']
#         myString=str(answer_gif)
#         myString= myString[:1].upper() + myString[1:] # Capitalise first letter
#         return(myString)

#     def get_yes(self):  
#         response = requests.get("https://yesno.wtf/api?force=yes")
#         json_data = json.loads(response.text)
#         answer_gif = json_data["answer"] + "." + "\n" + json_data['image']
#         myString=str(answer_gif)
#         myString= myString[:1].upper() + myString[1:] # Capitalise first letter
#         return(myString)

#     @commands.Cog.listener()
#     async def on_message(self, message):
#         if message.author == self.bot.user:
#             return
#     @commands.command()
#     @commands.cooldown(1, 10, commands.BucketType.user)
#     async def yesno(self, ctx):
#         if ctx.author.id == 155736840387821569:
#             api = self.get_yes()
#             await ctx.reply(f"{api}")
#         else:
#             api = self.get_api()
#             await ctx.reply(f"{api}")

# async def setup(bot):
#     await bot.add_cog(yesnomaybe(bot))
