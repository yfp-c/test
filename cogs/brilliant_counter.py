import discord, sqlite3
from discord.ext import commands

processed_messages = {}

class brilliant_count(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return
        if "brilliant" in message.content.lower():
            # Get the processed message IDs for the user
            user_messages = processed_messages.get(message.author.id, {})

            # Check if the message has been processed
            if message.id not in user_messages:
                # Add the message ID to the user's dictionary
                user_messages[message.id] = True
                processed_messages[message.author.id] = user_messages
            conn = sqlite3.connect(r"./cogs/brilliant_count.db")
            c = conn.cursor()

            # Get the user data
            user = message.author

            # Check if the user is already in the database
            c.execute("SELECT count FROM brilliant_counter WHERE discord_id=?", (user.id,))
            result = c.fetchone()
            if result is None:
                # User is not in the database, add them with a count of 1
                c.execute("INSERT INTO brilliant_counter (discord_id, discord_username, count) VALUES (?, ?, ?)", (user.id, user.name, 1))
            else:
                # User is in the database, increment the count
                count = result[0]
                count += 1
                c.execute("UPDATE brilliant_counter SET discord_username=?, count=? WHERE discord_id=?", (user.name, count, user.id))

            # Commit the changes to the database
            conn.commit()

            # Close the database connection
            conn.close()

    @commands.command(pass_context = True , aliases=['bc', 'brill_counter'])
    @commands.cooldown(1, 120, commands.BucketType.user)
    async def br_counter(self, ctx):
        if ctx.author == self.bot.user:
            return
        conn = sqlite3.connect(r"./cogs/brilliant_count.db")
        c = conn.cursor()

        # Get the user data
        user = ctx.message.author

        # Fetch the user's data from the database
        c.execute("SELECT * FROM brilliant_counter WHERE discord_id=?", (user.id,))
        data = c.fetchone()

        if data is None:
            # User is not in the database
            await ctx.send("You are not in the database, please begin by typing 'Brilliant' or 'Brilliant!!'")
        else:
            # User is in the database, send the data back to the user
            await ctx.send(f"Username: {data[0]}\nDiscord ID: {data[1]}\nCount: {data[2]}")

    @commands.command()
    @commands.cooldown(1, 120, commands.BucketType.user)
    async def br_leaderboard(self, ctx):
        # Connect to the database
        conn = sqlite3.connect(r"./cogs/brilliant_count.db")
        c = conn.cursor()

        # Fetch all the user data from the database, sorted by the count field in descending order
        c.execute("SELECT * FROM brilliant_counter ORDER BY count DESC")
        data = c.fetchall()

        # Format the leaderboard
        # i is for how many users in database
        # 1 row
        leaderboard = "**Brilliant Leaderboard**\n\n"
        for i, row in enumerate(data, 1):
            leaderboard += (f"{i}. {row[0]} ({row[1]}): has said **{row[2]}** brilliants!\n")

        # Send the leaderboard to the user
        await ctx.send(leaderboard)


async def setup(bot):
    await bot.add_cog(brilliant_count(bot))