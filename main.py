import os 
import discord
from discord.ext import commands
from discord import app_commands

from myserver import server_on

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("Bot Online!")
    synced = await bot.tree.sync()


@bot.event
async def on_member_join(member):
     channel = bot.get_channel(1122400225953337365)
     text = f"ยินดีต้อนรับฮ๊าฟฟู่ว, {member.mention}!"
     emmbed = discord.Embed(title = "มีสมาชิกใหม่!",
                            color=0xd81b60,
                            description = text)

     await channel.send(embed = emmbed)

@bot.event
async def on_member_remove(member):
     channel = bot.get_channel(1122400225953337365)
     text = f"เขาได้จากเราไปแล้ว, {member.mention}!"
     emmbed = discord.Embed(title = "เราสูญเสียบางคนไป..",
                            color=0xd81b60,
                            description = text)
     await channel.send(embed = emmbed)

@bot.tree.command(name="help", description="Bot Commands")
async def helpcommand(interaction):
    emmbed = discord.Embed(title="About Moodeng! - Bot Commands",
                           description="Moodeng คือพนักงานต้อนรับคนเข้าดิส",
                           color=0xd81b60,
                           timestamp= discord.utils.utcnow())

    emmbed.add_field(name="/Info", value="Info Command", inline=False)

    emmbed.set_author(name="AomTa", url="https://discord.com/channels/@me", icon_url="https://tse2.mm.bing.net/th/id/OIP.qF1skKx0YRHyT1Z4omcZBgHaHV?pid=Api&P=0&h=180")

    emmbed.set_thumbnail(url="https://picx.zhimg.com/v2-7f3902a45265944fe0d39c5fa667976a_720w.jpg?source=172ae18b")
    emmbed.set_image(url="https://i.redd.it/lfebrs9i5crb1.gif")

    emmbed.set_footer(text="eiei",icon_url="https://picx.zhimg.com/v2-7f3902a45265944fe0d39c5fa667976a_720w.jpg?source=172ae18b")

    await interaction.response.send_message(embed = emmbed)

server_on()

bot.run(os.getenv("TOKEN"))