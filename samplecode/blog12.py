import discord
import os

client = discord.Client(
    intents=discord.Intents.all()
)


@client.event
async def on_message(message):
    # /ch_create チャンネル名 というコマンドで反応する
    if message.content.startswith("/ch_create"):
        ch_name = message.content.split(' ')
        # 送信された/ch_createから始まるメッセージを、空白で分割し
        # それが list型 になったものを 変数:ch_name に格納している

        if len(ch_name)<=1:
            return
            # 一般的に ['/ch_create', '名前'] と返り、名前の部分を取り出した際に
            # 名前がない時、チャンネルを作成する際にエラーが発生するのを回避している

        # 権限を編集して作成するには以下のコードを追加
        permission = {
            message.guild.default_role: discord.PermissionOverwrite(read_messages=False),
            message.guild.me: discord.PermissionOverwrite(read_messages=True)
        }

        # チャンネルを作成するカテゴリを取得
        category = message.guild.get_channel(カテゴリID)

        #取得したカテゴリに指定した名前でチャンネルを作成
        ch = await category.create_text_channel(name=ch_name[1], overwrites=permission)

        # 権限を編集して作成するには、上記で追加した permission を
        # overwrites に指定する
        await message.channel.send(f"{ch.mention} を作成しました。")


token = os.environ.get('DISCORD_BOT_TOKEN')
client.run(token)
