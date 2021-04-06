import os
import discord
from discord.ext import commands

bot = commands.Bot(
    command_prefix=commands.when_mentioned_or('/'),
    help_command=None,
    intents=discord.Intents.all(),
)

ROLE_BASIC_ID = 934598783292524930


@bot.command()
@commands.has_permissions(administrator=True)
async def set_members(ctx):
    role_basic = ctx.guild.get_role(ROLE_BASIC_ID)
    for member in ctx.guild.members:
        if not member.bot:
            await member.add_roles(role_basic)


token = os.environ.get('DISCORD_BOT_TOKEN')
bot.run(token)
