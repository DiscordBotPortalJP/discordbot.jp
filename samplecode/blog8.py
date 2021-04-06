import discord
import os

client = discord.Client(
    intents=discord.Intents.all()
)


@client.event
async def on_message(message):
    # /invite というコマンドで反応する
    if message.content != '/invite_count':
        return

    # サーバーの招待URLのリストを取得する
    invites = await message.guild.invites()

    # 特定のユーザが作成した招待URLを取得
    user_id = 462810739204161537
    invite = discord.utils.get(invites, inviter__id=user_id)

    # 招待URLの使用回数を取得
    count_use = invite.uses

    # チャンネルに情報を送信
    await message.channel.send(f'招待URLの使用回数：{count_use}')


token = os.environ.get('DISCORD_BOT_TOKEN')
client.run(token)
