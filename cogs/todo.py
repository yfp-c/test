import discord, random
from discord.ext import commands

class todo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context = True , aliases=['do', 'todolist'])
    @commands.cooldown(1, 21600, commands.BucketType.user)
    async def todo(self, ctx):
        with open("./cogs/todo_list/bonjela1.txt", mode="r", encoding=None, errors=None) as file:
            allText = file.readlines()
            words = list(map(str, allText))
            embed = discord.Embed(title=f"Greetings {ctx.author.name}, your to-do for today: ", description=f"{random.choice(words)}", color=discord.Colour.random() )
            await ctx.reply(embed = embed)
            # await ctx.reply(random.choice(words))


async def setup(bot):
    await bot.add_cog(todo(bot))