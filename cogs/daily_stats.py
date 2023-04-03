import discord, random, json, requests
from discord.ext import commands

class daily_stats(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def get_quote(self):
        response = requests.get("https://api.kanye.rest/")
        json_data = json.loads(response.text)
        quote = '"'+ json_data['quote'] + '"'
        return(quote)

    @commands.command(pass_context = True , aliases=['stats', 'dailystats'])
    @commands.cooldown(1, 43200, commands.BucketType.user)
    async def daily(self, ctx):
        quote = self.get_quote()
        embed = discord.Embed(
            colour=(discord.Colour.random()),
            description=f"HELLO {ctx.author.name}, your daily stats percentages are... \n"
            f"\n"
            f"-Health: **{random.randint(0,100)}%**\n"
            f"-Career: **{random.randint(0,100)}%**\n"
            f"-Happiness: **{random.randint(0,100)}%**\n"
            f"-Productivity: **{random.randint(0,100)}%**\n"
            f"-Luck: **{random.randint(0,100)}%**\n"
            f"-True love probability: **{random.randint(0,100)}%**\n"
            f"-Attractiveness: **{random.randint(0,100)}%**\n"
            f"\n"
            f"{quote} - Kanye West"
        )
        embed.set_footer(text="Note: Extremely accurate.")
        # embed.set_image(url=(random.choice(good_luck)))
        await ctx.reply(embed = embed)

async def setup(bot):
    await bot.add_cog(daily_stats(bot))
