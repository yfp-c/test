import discord
from discord.ext import commands
from googletrans import Translator, LANGUAGES
from googletrans.models import Translated

# languages = list(LANGUAGES.values())
languages = list(LANGUAGES)
languages_shortened = list(LANGUAGES.values())

class google_trans(commands.Cog):
    def __init__(self, bot):
        self.bot = bot



    @commands.command(aliases=['translate'])
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def trans(self, ctx, lang, *, args):
        if lang not in languages and lang not in languages_shortened:
            wrong_embed = discord.Embed(title=f"Oops! I can't detect your language...\n", description=f"Format is: **!trans [language to translate to] [text to translate]**\n E.g. **!trans french good morning how are we doing guys?**")
            wrong_embed.add_field(name="Full language list", value="https://py-googletrans.readthedocs.io/en/latest/#googletrans-languages")
            await ctx.reply(embed=wrong_embed)
        else:
            t = Translator()
            a = t.translate(args, dest=lang)
            embed= discord.Embed(title=f'Extending my knowledge to the cloud and translating....', description=f'Successfully translated the text below (provided no typos) :point_down:  \n \n**{a.text}**', color=discord.Colour.random())
            embed.add_field(name="Full language list", value="https://py-googletrans.readthedocs.io/en/latest/#googletrans-languages")
            await ctx.reply(embed=embed)


async def setup(bot):
    await bot.add_cog(google_trans(bot))