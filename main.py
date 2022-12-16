import nextcord
from nextcord.ext import commands
import time

TESTING_GUILD_ID = 479164051230818306  # Replace with your testing guild id

class Main(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @nextcord.slash_command(guild_ids=[TESTING_GUILD_ID], description="Test command")
    async def my_slash_command(self, interaction: nextcord.Interaction):
        await interaction.response.send_message("This is a slash command in a cog!")

    @nextcord.slash_command(guild_ids=[TESTING_GUILD_ID], description="Replies with pong!")
    async def ping(self, interaction: nextcord.Interaction):
        await interaction.send("Pong!", ephemeral=True)

    @nextcord.slash_command(guild_ids=[TESTING_GUILD_ID], description="顯示機器人目前延遲")
    async def latency(self, interaction: nextcord.Interaction):
        embed = nextcord.Embed(title='延遲時間(ms)',
                                description=f'{round(self.bot.latency*1000)} 毫秒',
                                color=0xb12091)
        await interaction.send(embed=embed, ephemeral=True)
        
    @nextcord.slash_command(guild_ids=[TESTING_GUILD_ID], description="顯示目前時間")
    async def nowtime(self, interaction: nextcord.Integration):
        await interaction.send(f'現在時間是: <t:{int(time.time())}:F>', ephemeral=True)

def setup(bot):
    bot.add_cog(Main(bot))