from curses.panel import bottom_panel
import discord, requests, json, random
from discord.ext import commands

class yesnomaybe(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def get_api(self):
        response = requests.get("https://yesno.wtf/api")
        json_data = json.loads(response.text)
        answer_gif = json_data["answer"] + "." + "\n" + json_data['image']
        myString=str(answer_gif)
        myString= myString[:1].upper() + myString[1:] # Capitalise first letter
        return(myString)

    def get_yes(self):  
        # yes_gifs = ['https://yesno.wtf/assets/yes/5-64c2804cc48057b94fd0b3eaf323d92c.gif', 'https://yesno.wtf/assets/yes/15-3d723ea13af91839a671d4791fc53dcc.gif', 
        # 'https://yesno.wtf/assets/yes/13-c3082a998e7758be8e582276f35d1336.gif', 'https://yesno.wtf/assets/yes/4-c53643ecec77153eefb461e053fb4947.gif',
        # 'https://yesno.wtf/assets/yes/0-c44a7789d54cbdcad867fb7845ff03ae.gif', 'https://yesno.wtf/assets/yes/1-af11222d8d4af90bdab8fc447c8cfebf.gif',
        # 'https://yesno.wtf/assets/yes/6-304e564038051dab8a5aa43156cdc20d.gif', 'https://yesno.wtf/assets/yes/2-5df1b403f2654fa77559af1bf2332d7a.gif',
        # 'https://yesno.wtf/assets/yes/12-e4f57c8f172c51fdd983c2837349f853.gif', 'https://yesno.wtf/assets/yes/9-6403270cf95723ae4664274db51f1fd4.gif',
        # 'https://yesno.wtf/assets/yes/10-271c872c91cd72c1e38e72d2f8eda676.gif']  
        response = requests.get("https://yesno.wtf/api?force=yes")
        json_data = json.loads(response.text)
        answer_gif = json_data["answer"] + "." + "\n" + json_data['image']
        myString=str(answer_gif)
        myString= myString[:1].upper() + myString[1:] # Capitalise first letter
        return(myString)

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return
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
    await bot.add_cog(yesnomaybe(bot))
