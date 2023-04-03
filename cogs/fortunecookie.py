import discord, random
from discord.ext import commands

class fortunecookie(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context = True , aliases=['fc', 'fortune'])
    @commands.cooldown(1, 43200, commands.BucketType.user)
    async def fortunecookie(self, ctx):
        # randomnumber1 = random.randint(1,99)
        # randomnumber2 = random.randint(1,99)
        # randomnumber3 = random.randint(1,99)
        # randomnumber4 = random.randint(1,99)
        # randomnumber5 = random.randint(1,99)
        # randomnumber6 = random.randint(1,99)
        # lucky_numbers = f"{randomnumber1}-{randomnumber2}-{randomnumber3}-{randomnumber4}-{randomnumber5}-[{randomnumber6}]"
        five_numbers = '-'.join(str(random.randint(1,99)) for _ in range(5))
        with open("./cogs/fortunecookiequotes/fortunecookiequotes.txt", "r") as file:
            allText = file.readlines()
            words = list(map(str, allText))
        await ctx.reply(f"Greetings {ctx.author.name}..."
        f"```fix\n🥠 {random.choice(words)}```"
        f"```py\n🍀 Your Lucky Numbers: {five_numbers}-[{random.randint(1,99)}]```")


async def setup(bot):
    await bot.add_cog(fortunecookie(bot))