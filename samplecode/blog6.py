import discord
import os

client = discord.Client(
    intents=discord.Intents.all()
)

ID_ROLE_MEMBER = 576891687620118902


@client.event
async def on_member_join(member):
    # 用意したIDから Role オブジェクトを取得
    role = member.guild.get_role(ID_ROLE_MEMBER)

    # 入ってきた Member に役職を付与
    await member.add_roles(role)


token = os.environ.get('DISCORD_BOT_TOKEN')
client.run(token)
