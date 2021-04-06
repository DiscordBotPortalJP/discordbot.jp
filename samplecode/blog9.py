import discord
import os

client = discord.Client(
    intents=discord.Intents.all()
)


@client.event
async def on_message(message):

    # /role 役職名 というコマンドで反応する
    if message.content.startswith('/role'):
        role_name = message.content.replace('/role ', '')

        # 指定した役職を取得する
        role = discord.utils.get(message.guild.roles, name=role_name)

        # 取得した役職が連携されているか取得する
        role_managed = role.managed

        # 返り値は bool 型なので、
        # されている場合は「True」、されていない場合は「False」が返ってきます
        # チャンネルに送信
        await message.channel.send(f'**{role}**の外部サービスとの連携 : {role_managed}')


token = os.environ.get('DISCORD_BOT_TOKEN')
client.run(token)
