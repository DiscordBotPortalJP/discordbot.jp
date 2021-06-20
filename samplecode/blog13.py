import discord
import os
import asyncio

client = discord.Client(
    intents=discord.Intents.all()
)


@client.event
async def on_message(message):
    # /greet というコマンドで反応する
    if message.content.startswith('/greet'):

        # メッセージが送信されたチャンネルを取得し、`channel` という変数に入れる
        channel = message.channel

        # チャンネルにメッセージを送信
        await channel.send('おはようと言うとさらに反応します')

        # 待っているものに該当するかを確認する関数
        def check(m):
            # メッセージが `おはよう` かつ メッセージを送信したチャンネルが
            # コマンドを打ったチャンネルという条件
            return m.content == 'おはよう' and m.channel == channel

        try:
            # wait_forを用いて、イベントが発火し指定した条件を満たすまで待機する
            msg = await client.wait_for('message', check=check, timeout=30)
            # wait_forの1つ目のパラメータは、イベント名の on_がないもの
            # 2つ目は、待っているものに該当するかを確認する関数 (任意)
            # 3つ目は、タイムアウトして asyncio.TimeoutError が発生するまでの秒数

        # asyncio.TimeoutError が発生したらここに飛ぶ
        except asyncio.TimeoutError:
            await channel.send(f'{message.author.mention}さん、時間切れです')
        else:
            # メンション付きでメッセージを送信する。
            await channel.send(f'{msg.author.mention}さん、おはようございます')


token = os.environ.get('DISCORD_BOT_TOKEN')
client.run(token)
