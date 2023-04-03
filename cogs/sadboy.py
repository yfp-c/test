import discord, random, sqlite3
from discord.ext import commands

class sadboy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context = True)
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def sb(self, ctx):
        # Connect to the database
        conn = sqlite3.connect(r"./cogs/sadboy_lyrics.db")
        c = conn.cursor()

        # Execute a SELECT query to retrieve the song name, artist, and lyrics from the database
        c.execute("SELECT song_name, artist, lyrics, artist_image_url FROM songs")
        songs = c.fetchall()

        # Shuffle the songs randomly
        random.shuffle(songs)

        # Extract the first song from the shuffled list
        song_id = songs[0]
        song_name = song_id[0]
        artist = song_id[1]
        lyrics = song_id[2]
        artist_image_url = song_id[3]

        # Create the embed object
        embed = discord.Embed(title=f"😥😔☹", color=discord.Colour.random())

        # Set the thumbnail and image
        # embed.set_thumbnail(url=f"{artist_image_url}")
        embed.set_image(url=f"{artist_image_url}")

        # Set the author
        embed.set_author(name=f"{artist}")

        # Add fields to the embed
        embed.add_field(name=f"{song_name}", value=f"🎵 {lyrics} 🎵", inline=False)

        # Send the embed
        await ctx.send(embed=embed)

        # Close the database connection
        conn.close()

async def setup(bot):
    await bot.add_cog(sadboy(bot))