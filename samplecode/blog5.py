import discord
import os

client = discord.Client(
    intents=discord.Intents.all()
)

ID_CHANNEL_README = 729000364261967998 # 該当のチャンネルのID
ID_ROLE_WELCOME = 775643766212653538 # 付けたい役職のID


@client.event
async def on_raw_reaction_add(payload):
    # channel_id から Channel オブジェクトを取得
    channel = client.get_channel(payload.channel_id)

    # 該当のチャンネル以外はスルー
    if channel.id != ID_CHANNEL_README:
        return

    # guild_id から Guild オブジェクトを取得
    guild = client.get_guild(payload.guild_id)

    # user_id から Member オブジェクトを取得
    member = guild.get_member(payload.user_id)

    # 用意した役職IDから Role オブジェクトを取得
    role = guild.get_role(ID_ROLE_WELCOME)

    # リアクションを付けたメンバーに役職を付与
    await member.add_roles(role)

    # 分かりやすいように歓迎のメッセージを送る
    await channel.send('いらっしゃいませ！')


token = os.environ.get('DISCORD_BOT_TOKEN')
client.run(token)
