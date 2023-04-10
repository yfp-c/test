import discord
from discord.ext import commands
from googletrans import Translator, LANGUAGES

# Create lists of supported languages and their shortened codes
languages = list(LANGUAGES)
languages_shortened = list(LANGUAGES.values())

class GoogleTrans(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.translator = Translator()

    # Method to translate the given text to the specified target language
    def translate_text(self, text, lang):
        return self.translator.translate(text, dest=lang).text

    # Method to create a Discord embed with the given title, description, and language list URL
    def create_embed(self, title, description, lang_list_url):
        embed = discord.Embed(title=title, description=description, color=discord.Colour.random())
        embed.add_field(name="Full language list", value=lang_list_url)
        return embed

    # Command to translate the input text to the specified target language
    @commands.command(aliases=['translate'])
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def trans(self, ctx, lang, *, args):
        # Set the URL of the full language list provided by the googletrans library
        lang_list_url = "https://py-googletrans.readthedocs.io/en/latest/#googletrans-languages"

        # Check if the provided target language is valid (in languages or languages_shortened lists)
        if lang not in languages and lang not in languages_shortened:
            # If invalid, create an error embed with the proper message format and send it to the user
            title = f"Oops! I can't detect your language...\n"
            description = f"Format is: **!trans [language to translate to] [text to translate]**\n E.g. **!trans french good morning how are we doing guys?**"
            wrong_embed = self.create_embed(title, description, lang_list_url)
            await ctx.reply(embed=wrong_embed)
        else:
            # If valid, call the translate_text method to translate the input text to the target language
            translated_text = self.translate_text(args, lang)
            # Create an embed with the translated text and send it to the user
            title = f'Extending my knowledge to the cloud and translating....'
            description = f'Successfully translated the text below (provided no typos) :point_down:  \n \n**{translated_text}**'
            embed = self.create_embed(title, description, lang_list_url)
            await ctx.reply(embed=embed)

# Function to set up the GoogleTrans cog for the Discord bot
async def setup(bot):
    await bot.add_cog(GoogleTrans(bot))
    
# old
# import discord
# from discord.ext import commands
# from googletrans import Translator, LANGUAGES
# from googletrans.models import Translated

# # languages = list(LANGUAGES.values())
# languages = list(LANGUAGES)
# languages_shortened = list(LANGUAGES.values())

# class google_trans(commands.Cog):
#     def __init__(self, bot):
#         self.bot = bot



#     @commands.command(aliases=['translate'])
#     @commands.cooldown(1, 10, commands.BucketType.user)
#     async def trans(self, ctx, lang, *, args):
#         if lang not in languages and lang not in languages_shortened:
#             wrong_embed = discord.Embed(title=f"Oops! I can't detect your language...\n", description=f"Format is: **!trans [language to translate to] [text to translate]**\n E.g. **!trans french good morning how are we doing guys?**")
#             wrong_embed.add_field(name="Full language list", value="https://py-googletrans.readthedocs.io/en/latest/#googletrans-languages")
#             await ctx.reply(embed=wrong_embed)
#         else:
#             t = Translator()
#             a = t.translate(args, dest=lang)
#             embed= discord.Embed(title=f'Extending my knowledge to the cloud and translating....', description=f'Successfully translated the text below (provided no typos) :point_down:  \n \n**{a.text}**', color=discord.Colour.random())
#             embed.add_field(name="Full language list", value="https://py-googletrans.readthedocs.io/en/latest/#googletrans-languages")
#             await ctx.reply(embed=embed)


# async def setup(bot):
#     await bot.add_cog(google_trans(bot))


