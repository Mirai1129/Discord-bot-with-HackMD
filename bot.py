from threading import active_count
from discord import Status
import nextcord
from nextcord.ext import commands
import time
import os
from dotenv import load_dotenv


bot = commands.Bot()

bot.load_extension("main")
bot.load_extension("hackmd_request")


@bot.event
async def on_ready():
    print(f'{bot.user}上線了')
    status_online = nextcord.Status.online
    active_online = nextcord.Activity(type=nextcord.ActivityType.playing,
                                      name="早安吉祥")
    await bot.change_presence(status=status_online, activity=active_online)


@bot.slash_command(description="Replies with pong!")
async def ping(interaction: nextcord.Interaction):
    await interaction.send("Pong!", ephemeral=True)

# @bot.slash_command(description="顯示機器人目前延遲")
# async def ping2(interaction: nextcord.Interaction):
#     embed = nextcord.Embed(title='延遲時間(ms)',
#                             description=f'{round(bot.latency*1000)} 毫秒',
#                             color=0xb12091)
#     await interaction.send(embed=embed, ephemeral=True)

# @bot.slash_command(description="顯示目前時間")
# async def nowtime(interaction: nextcord.Integration):
#     await interaction.send(f'現在時間是: <t:{int(time.time())}:F>', ephemeral=True)

load_dotenv()
bot.run(os.getenv('TOKEN'))
