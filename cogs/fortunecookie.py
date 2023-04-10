import discord
import random
from discord.ext import commands

class FortuneCookie(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Method to generate lucky numbers
    def get_lucky_numbers(self, count=5):
        return '-'.join(str(random.randint(1, 99)) for _ in range(count))

    # Method to read the fortune cookie quotes from the file
    def read_fortune_quotes(self, filename):
        with open(filename, "r") as file:
            all_text = file.readlines()
        return list(map(str, all_text))

    # Method to pick a random quote from a list of quotes
    def get_random_quote(self, quotes):
        return random.choice(quotes)

    @commands.command(pass_context=True, aliases=['fc', 'fortune'])
    @commands.cooldown(1, 120, commands.BucketType.user)
    async def fortunecookie(self, ctx):
        # Call the get_lucky_numbers method to generate the lucky numbers
        five_numbers = self.get_lucky_numbers()

        # Call the read_fortune_quotes method to read quotes from the file
        words = self.read_fortune_quotes("./cogs/fortunecookiequotes/fortunecookiequotes.txt")

        # Call the get_random_quote method to select a random quote from the list of quotes
        random_quote = self.get_random_quote(words)

        await ctx.reply(f"Greetings {ctx.author.name}..."
        f"```fix\n🥠 {random_quote}```"
        f"```py\n🍀 Your Lucky Numbers: {five_numbers}-[{random.randint(1, 99)}]```")

async def setup(bot):
    await bot.add_cog(FortuneCookie(bot))

# old
# import discord, random
# from discord.ext import commands

# class fortunecookie(commands.Cog):
#     def __init__(self, bot):
#         self.bot = bot

#     @commands.command(pass_context = True , aliases=['fc', 'fortune'])
#     @commands.cooldown(1, 120, commands.BucketType.user)
#     async def fortunecookie(self, ctx):
#         five_numbers = '-'.join(str(random.randint(1,99)) for _ in range(5))
#         with open("./cogs/fortunecookiequotes/fortunecookiequotes.txt", "r") as file:
#             allText = file.readlines()
#             words = list(map(str, allText))
#         await ctx.reply(f"Greetings {ctx.author.name}..."
#         f"```fix\n🥠 {random.choice(words)}```"
#         f"```py\n🍀 Your Lucky Numbers: {five_numbers}-[{random.randint(1,99)}]```")


# async def setup(bot):
#     await bot.add_cog(fortunecookie(bot))

