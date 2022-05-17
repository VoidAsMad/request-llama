async def check_admin(ctx):
  if not ctx.author.guild_permissions.manage_messages:
    if str(ctx.author.id) == '712838792595112006':
      return 'Yes'
    await ctx.reply("관리자도 아닌게....이 명령어를?", hidden = True)
    return 'No'

async def kick(ctx, user, reason):
  await user.kick(reason=reason)
  await ctx.reply(f"<@{user.id}>를 추방했어! 퉷")

async def ban(ctx, user, reason):
  await user.ban(reason=reason)
  await ctx.reply(f"<@{user.id}>를 차단했어! 퉷")


async def addrole(ctx, role, user):
  await user.add_roles(role)
  await ctx.reply(f"<@{user.id}>에게 <@&{role.id}>를 부여했어~")


async def removerole(ctx, role, user):
  await user.remove_roles(role)
  await ctx.reply(f"<@{user.id}>에게 <@&{role.id}>를 제거했어~")
