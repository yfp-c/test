import discord, requests, json, random, asyncio
from discord.ext import commands

class Menu(discord.ui.View):
    def __init__(self, *, timeout = 1800):
        super().__init__(timeout=timeout)


    @discord.ui.button(label="Truth", style=discord.ButtonStyle.green)
    async def truth(self, interaction: discord.Interaction, button: discord.ui.Button):
        response = requests.get("https://api.truthordarebot.xyz/v1/truth")
        json_data = json.loads(response.text)
        #truth = "You've chosen: " + json_data["type"] + "\n" + "Rating: " + json_data['rating'] + "\n" + "Your question: " + json_data['question']
        embed = discord.Embed(
            color=discord.Color.random(),
            title=f"**{json_data['question']}**",
            )
        embed.add_field(name='\u200b', value=f"**Type:** {json_data['type']} | **Rating:** {json_data['rating']}", inline=True)
        embed.set_author(name=f'Requested by {interaction.user}', icon_url=interaction.user.avatar.url)
        button.disabled = True
        await asyncio.sleep(0.5)
        # await interaction.response.send_message(embed=embed,view=self)
        await interaction.response.send_message(embed=embed,view=self)
        # Delete the original button message
        await interaction.message.delete()


    @discord.ui.button(label="Dare", style=discord.ButtonStyle.red)
    async def dare(self, interaction: discord.Interaction, button: discord.ui.Button):
        response = requests.get("https://api.truthordarebot.xyz/api/dare")
        json_data = json.loads(response.text)
        #dare = "You've chosen: " + json_data["type"] + "\n" + "Rating: " + json_data['rating'] + "\n" + "Your dare: " + json_data['question']
        embed = discord.Embed(
            color=discord.Color.random(),
            title=f"**{json_data['question']}**",
            )
        embed.add_field(name='\u200b', value=f"**Type:** {json_data['type']} | **Rating:** {json_data['rating']}", inline=True)
        embed.set_author(name=f'Requested by {interaction.user}', icon_url=interaction.user.avatar.url)
        button.disabled = True
        await asyncio.sleep(0.5)
        # await interaction.response.send_message(embed=embed,view=self)
        await interaction.response.send_message(embed=embed,view=self)
        # Delete the original button message
        await interaction.message.delete()

    @discord.ui.button(label="Would you rather", style=discord.ButtonStyle.blurple)
    async def wyr(self, interaction: discord.Interaction, button: discord.ui.Button):
        response = requests.get("https://api.truthordarebot.xyz/api/wyr")
        json_data = json.loads(response.text)
        #wyr = "You've chosen: " + json_data["type"] + "\n" + "Rating: " + json_data['rating'] + "\n" + "Your 'would you rather': " + json_data['question']
        embed = discord.Embed(
            color=discord.Color.random(),
            title=f"**{json_data['question']}**",
            )
        embed.add_field(name='\u200b', value=f"**Type:** {json_data['type']} | **Rating:** {json_data['rating']}", inline=True)
        embed.set_author(name=f'Requested by {interaction.user}', icon_url=interaction.user.avatar.url)
        button.disabled = True
        await asyncio.sleep(0.5)
        # await interaction.response.send_message(embed=embed,view=self)
        await interaction.response.send_message(embed=embed,view=self)
        # Delete the original button message
        await interaction.message.delete()

    @discord.ui.button(label="Never have I ever", style=discord.ButtonStyle.gray)
    async def nhie(self, interaction: discord.Interaction, button: discord.ui.Button):
        response = requests.get("https://api.truthordarebot.xyz/api/nhie")
        json_data = json.loads(response.text)
        embed = discord.Embed(
            color=discord.Color.random(),
            title=f"**{json_data['question']}**",
            )
        embed.add_field(name='\u200b', value=f"**Type:** {json_data['type']} | **Rating:** {json_data['rating']}", inline=True)
        embed.set_author(name=f'Requested by {interaction.user}', icon_url=interaction.user.avatar.url)
        button.disabled = True
        await asyncio.sleep(0.5)
        # await interaction.response.send_message(embed=embed,view=self)
        await interaction.response.send_message(embed=embed,view=self)
        # Delete the original button message
        await interaction.message.delete()

    @discord.ui.button(label="Paranoia Question", style=discord.ButtonStyle.danger)
    async def pq(self, interaction: discord.Interaction, button: discord.ui.Button):
        response = requests.get("https://api.truthordarebot.xyz/api/paranoia")
        json_data = json.loads(response.text)
        embed = discord.Embed(
            color=discord.Color.random(),
            title=f"**{json_data['question']}**",
            )
        embed.add_field(name='\u200b', value=f"**Type:** {json_data['type']} | **Rating:** {json_data['rating']}", inline=True)
        embed.set_author(name=f'Requested by {interaction.user}', icon_url=interaction.user.avatar.url)
        button.disabled = True
        await asyncio.sleep(0.5)
        # await interaction.response.send_message(embed=embed,view=self)
        await interaction.response.send_message(embed=embed,view=self)
        # Delete the original button message
        await interaction.message.delete()
    


class Menu_r(discord.ui.View):
    def __init__(self, *, timeout = 1800):
        super().__init__(timeout=timeout)


    @discord.ui.button(label="Truth", style=discord.ButtonStyle.green)
    async def truth(self, interaction: discord.Interaction, button: discord.ui.Button):
        response = requests.get("https://api.truthordarebot.xyz/v1/truth?rating=r")
        json_data = json.loads(response.text)
        embed = discord.Embed(
            color=discord.Color.random(),
            title=f"**{json_data['question']}**",
            )
        embed.add_field(name='\u200b', value=f"**Type:** {json_data['type']} | **Rating:** {json_data['rating']}", inline=True)
        embed.set_author(name=f'Requested by {interaction.user}', icon_url=interaction.user.avatar.url)
        button.disabled = True
        await asyncio.sleep(0.5)
        # await interaction.response.send_message(embed=embed,view=self)
        await interaction.response.send_message(embed=embed,view=self)
        # Delete the original button message
        await interaction.message.delete()

    @discord.ui.button(label="Dare", style=discord.ButtonStyle.red)
    async def dare(self, interaction: discord.Interaction, button: discord.ui.Button):
        response = requests.get("https://api.truthordarebot.xyz/api/dare?rating=r")
        json_data = json.loads(response.text)
        embed = discord.Embed(
            color=discord.Color.random(),
            title=f"**{json_data['question']}**",
            )
        embed.add_field(name='\u200b', value=f"**Type:** {json_data['type']} | **Rating:** {json_data['rating']}", inline=True)
        embed.set_author(name=f'Requested by {interaction.user}', icon_url=interaction.user.avatar.url)
        button.disabled = True
        await asyncio.sleep(0.5)
        # await interaction.response.send_message(embed=embed,view=self)
        await interaction.response.send_message(embed=embed,view=self)
        # Delete the original button message
        await interaction.message.delete()

    @discord.ui.button(label="Would you rather", style=discord.ButtonStyle.blurple)
    async def wyr(self, interaction: discord.Interaction, button: discord.ui.Button):
        response = requests.get("https://api.truthordarebot.xyz/api/wyr?rating=r")
        json_data = json.loads(response.text)
        embed = discord.Embed(
            color=discord.Color.random(),
            title=f"**{json_data['question']}**",
            )
        embed.add_field(name='\u200b', value=f"**Type:** {json_data['type']} | **Rating:** {json_data['rating']}", inline=True)
        embed.set_author(name=f'Requested by {interaction.user}', icon_url=interaction.user.avatar.url)
        button.disabled = True
        await asyncio.sleep(0.5)
        # await interaction.response.send_message(embed=embed,view=self)
        await interaction.response.send_message(embed=embed,view=self)
        # Delete the original button message
        await interaction.message.delete()

    @discord.ui.button(label="Never have I ever", style=discord.ButtonStyle.gray)
    async def nhie(self, interaction: discord.Interaction, button: discord.ui.Button):
        response = requests.get("https://api.truthordarebot.xyz/api/nhie?rating=r")
        json_data = json.loads(response.text)
        embed = discord.Embed(
            color=discord.Color.random(),
            title=f"**{json_data['question']}**",
            )
        embed.add_field(name='\u200b', value=f"**Type:** {json_data['type']} | **Rating:** {json_data['rating']}", inline=True)
        embed.set_author(name=f'Requested by {interaction.user}', icon_url=interaction.user.avatar.url)
        button.disabled = True
        await asyncio.sleep(0.5)
        # await interaction.response.send_message(embed=embed,view=self)
        await interaction.response.send_message(embed=embed,view=self)
        # Delete the original button message
        await interaction.message.delete()

    @discord.ui.button(label="Paranoia Question", style=discord.ButtonStyle.danger)
    async def pq(self, interaction: discord.Interaction, button: discord.ui.Button):
        response = requests.get("https://api.truthordarebot.xyz/api/paranoia?rating=r")
        json_data = json.loads(response.text)
        embed = discord.Embed(
            color=discord.Color.random(),
            title=f"**{json_data['question']}**",
            )
        embed.add_field(name='\u200b', value=f"**Type:** {json_data['type']} | **Rating:** {json_data['rating']}", inline=True)
        embed.set_author(name=f'Requested by {interaction.user}', icon_url=interaction.user.avatar.url)
        button.disabled = True
        await asyncio.sleep(0.5)
        # await interaction.response.send_message(embed=embed,view=self)
        await interaction.response.send_message(embed=embed,view=self)
        # Delete the original button message
        await interaction.message.delete()



class TorD(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context = True, aliases=['truth','dare','tord'])
    @commands.cooldown(1, 1800, commands.BucketType.user)
    async def truthordare(self, ctx):
        view = Menu()
        await ctx.send("Truth or Dare?", view=view)

    @commands.command(pass_context = True, aliases=['truthr','darer','tordr'])
    @commands.cooldown(1, 1800, commands.BucketType.user)
    async def truthordarer(self, ctx):
        view = Menu_r()
        await ctx.send("Truth or Dare?", view=view)

async def setup(bot):
    await bot.add_cog(TorD(bot))