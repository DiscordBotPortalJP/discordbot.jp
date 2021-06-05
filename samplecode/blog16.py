import os

import discord


client = discord.Client(
    allowed_mentions=discord.AllowedMentions(replied_user=False)  # 返信のメンションをデフォルトでオフにする
)


@client.event
async def on_message(message):
    if message.content == "!ping":
        # Ping値を秒単位で取得
        raw_ping = client.latency

        # ミリ秒に変換して丸める
        ping = round(raw_ping * 1000)

        # 送信する
        await message.reply(f"Pong!\nBotのPingは{ping}msです。")

client.run(os.getenv("token"))
