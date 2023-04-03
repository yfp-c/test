import discord, random
from discord.ext import commands

class trading_tips(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(pass_context = True , aliases=['tt', 'tradingtip', 'trading'])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def tradingtips(self, ctx):
        tips = ['Spin around in a circle and say 5 Hail Mary’s',
        'stop exercising options and trying exorcizing your house instead',
        'Double down buy more',
        "It's different this time, buy more!",
        "Go Hard or Go Home!",
        "It takes years and years and years to learn how to trade and read charts. You're better off buying this software and allowing the artificial intelligence software to do all the work for you. All that you have to do is subscribe, pay your monthly fee, set your settings and walk away. You can't beat it!",
        "It's only a loss if you sell",
        "Pay to join my discord Server, chat room alerts will bring your small account to the moon!",
        "Bitcoin is going to Zero , SHORT BTC.",
        "Don't do demo; you want to be a real trader, start live",
        "it will go to the moon. Trust me.",
        "it will be an epic crash. Trust me.",
        "technical analysis is just astrology for traders",
        "Real men don't use stops",
        "trade against the trend",
        "Buy the dip!",
        "No, seriously. You should go ALL IN on Doge. Elon Musk is gonna be on SNL tomorrow night. It's gonna skyrocket.",
        "It can't go lower",
        "This one is free money",
        "use a mental stop loss",
        "be patient when you are in red it will turn green",
        "It's just a correction",
        "Just wait for it…it will come back up!",
        "The people that do best in the market buy and forget about it. Years later they are millionaires.",
        "you should try trading, I think you'd be good at it",
        "HODL!"
        "Follow your gut",
        "Buy shib"
        ]

        await ctx.reply(f"**My financial advice:** {random.choice(tips)}")

async def setup(bot):
    await bot.add_cog(trading_tips(bot))