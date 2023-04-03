import discord, random, json, requests
from discord.ext import commands

class biryani(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    def get_quote(self):
        response = requests.get("https://biriyani.anoram.com/get")
        json_data = json.loads(response.text)
        quote = json_data["image"]
        return(quote)

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return
    @commands.command()
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def biryani(self, ctx):
        quote = self.get_quote()
        await ctx.reply(f"{quote}")

async def setup(bot):
    await bot.add_cog(biryani(bot))