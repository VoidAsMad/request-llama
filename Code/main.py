#import
import discord
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext

bot = commands.Bot(command_prefix=['?'], intents=discord.Intents.all())
slash = SlashCommand(bot, sync_commands=True)




@bot.event
async def on_ready():
  print('로딩완료')
  await bot.change_presence(activity=discord.Game("/docs"))

@slash.slash(name="추방하기",description="유저를 킥하는거야!", guild_ids=[971984827177926716])
async def kicks(ctx, 유저 : discord.Member, 사유 = None):
  c = await check_admin(ctx)
  if c == "No":
    return None
  await kick(ctx, 유저, 사유)

@slash.slash(name="차단하기",description="유저를 밴하는거야!", guild_ids=[971984827177926716])
async def bans(ctx, 유저 : discord.Member, 사유 = None):
  c = await check_admin(ctx)
  if c == "No":
    return None
  await ban(ctx, 유저, 사유)

@slash.slash(name="역할부여",description="유저에게 역할을 부여해!", guild_ids=[971984827177926716])
async def addroles(ctx, 역할 : discord.Role, 유저 : discord.Member):
  c = await check_admin(ctx)
  if c == "No":
    return None
  await addrole(ctx, 역할, 유저)


@slash.slash(name="역할삭제",description="유저에게 역할을 제거해!", guild_ids=[971984827177926716])
async def removeroles(ctx, 역할 : discord.Role, 유저 : discord.Member):
  c = await check_admin(ctx)
  if c == "No":
    return None
  await removerole(ctx, 역할, 유저)
  
  
bot.run("token")
