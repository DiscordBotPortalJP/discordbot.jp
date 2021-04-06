import discord
import os

client = discord.Client(
    intents=discord.Intents.all()
)


@client.event
async def on_message(message):
    # /test と打った場合のみ反応するように
    if message.content != '/test':
        return

    # message インスタンスから guild インスタンスを取得
    guild = message.guild 

    # ユーザとBOTを区別しない場合
    member_count = guild.member_count
    await message.channel.send(f'メンバー数：{member_count}')

    # ユーザのみ
    user_count = sum(1 for member in guild.members if not member.bot)
    await message.channel.send(f'ユーザ数：{user_count}')

    # BOTのみ
    bot_count = sum(1 for member in guild.members if member.bot)
    await message.channel.send(f'BOT数：{bot_count}')


token = os.environ.get('DISCORD_BOT_TOKEN')
client.run(token)
