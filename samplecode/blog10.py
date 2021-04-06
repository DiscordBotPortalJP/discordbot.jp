import discord
import os

client = discord.Client(
    intents=discord.Intents.all()
)


@client.event
async def on_message(message):

    # /last_msg チャンネル名 というコマンドで反応する
    if message.content.startswith('/last_msg'):
        channel_name = message.content.replace('/last_msg ', '')

        # 指定したチャンネルを取得する
        channel = discord.utils.get(message.guild.channels, name=channel_name)

        # 取得したチャンネルの最後のメッセージを取得する
        last_msg = channel.last_message

        # 取得したメッセージの内容を取得する
        last_msg_content = last_msg.content
        # 取得できなかった時は None が返されます

        # チャンネルに送信
        await message.channel.send(f'**{channel}**に送られた最後のメッセージ : {last_msg_content}')


token = os.environ.get('DISCORD_BOT_TOKEN')
client.run(token)
