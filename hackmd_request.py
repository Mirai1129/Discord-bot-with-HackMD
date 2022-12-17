import nextcord
from nextcord.ext import commands
import time
import requests
import os
from dotenv import load_dotenv

TESTING_GUILD_ID = your testing guild id  # Replace with your testing guild id

load_dotenv()


class Main(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @nextcord.slash_command(guild_ids=[TESTING_GUILD_ID], description="取得使用者資料")
    async def me(self, interaction: nextcord.Interaction):
        # API網址
        url = "https://api.hackmd.io/v1/me"
        # 標頭
        headers = {
            "Authorization": ("Bearer " + str(os.getenv('HACKMD_TOKEN')))
        }
        access_token = requests.get(url, headers=headers)
        await interaction.response.send_message("```json\n"+access_token.text+"```", ephemeral=True)

    @nextcord.slash_command(guild_ids=[TESTING_GUILD_ID], description="取得筆記資料")
    async def mdfile(self, interaction: nextcord.Interaction):
        # API網址
        url = "https://api.hackmd.io/v1/notes"
        # 標頭
        headers = {
            "Authorization": ("Bearer " + str(os.getenv('HACKMD_TOKEN')))
        }
        access_token = requests.get(url, headers=headers)
        await interaction.response.send_message("```json\n"+access_token.text+"```", ephemeral=True)


def setup(bot):
    bot.add_cog(Main(bot))
