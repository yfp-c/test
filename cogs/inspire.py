import discord, json
from discord.ext import commands
import requests

class inspirational_quotes(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def get_quote(self):
        response = requests.get("https://zenquotes.io/api/random")
        json_data = json.loads(response.text)
        quote = json_data[0]['q'] + " -" + json_data[0]['a']
        return(quote)


    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return
    @commands.command()
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def inspire(self, ctx):
        quote = self.get_quote()
        await ctx.reply(quote)

async def setup(bot):
    await bot.add_cog(inspirational_quotes(bot))