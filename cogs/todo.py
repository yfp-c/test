import discord
import random
from discord.ext import commands

class Todo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Method to read the todo list file and return a random task
    def get_random_task(self):
        with open("./cogs/todo_list/bonjela1.txt", "r", encoding=None, errors=None) as file:
            allText = file.readlines()
            words = list(map(str, allText))
        return random.choice(words)

    # Command to send a random task to the user
    @commands.command(pass_context=True, aliases=['do', 'todolist'])
    @commands.cooldown(1, 21600, commands.BucketType.user)
    async def todo(self, ctx):
        # Call the get_random_task method to fetch a random task
        random_task = self.get_random_task()
        embed = discord.Embed(title=f"Greetings {ctx.author.name}, your to-do for today... ",
                              description=f"{random_task}",
                              color=discord.Colour.random())
        await ctx.reply(embed=embed)

async def setup(bot):
    await bot.add_cog(Todo(bot))

# old
# import discord, random
# from discord.ext import commands

# class todo(commands.Cog):
#     def __init__(self, bot):
#         self.bot = bot

#     @commands.command(pass_context = True , aliases=['do', 'todolist'])
#     @commands.cooldown(1, 21600, commands.BucketType.user)
#     async def todo(self, ctx):
#         with open("./cogs/todo_list/bonjela1.txt", "r", encoding=None, errors=None) as file:
#             allText = file.readlines()
#             words = list(map(str, allText))
#             embed = discord.Embed(title=f"Greetings {ctx.author.name}, your to-do for today... ", description=f"{random.choice(words)}", color=discord.Colour.random() )
#             await ctx.reply(embed = embed)



# async def setup(bot):
#     await bot.add_cog(todo(bot))