import discord
import os

client = discord.Client(
    intents=discord.Intents.all()
)


@client.event
async def on_message(message):
    #メッセージを送信する
    if message.content.startswith('/send_dm'):
        # DMに送るメッセージを取得
        msg = message.content.replace('/send_dm ', '')
        # コマンドを打った人のDMに送信
        await message.author.send(msg)
        # message.author はメッセージを送信したユーザーです
    
    # Embedメッセージを送信する
    elif message.content.startswith('/send_embed'):
        # Embedメッセージ
        embed_msg = discord.Embed(title="Embedメッセージ", description="正常に送信されました")
        # コマンドを打った人のDMに送信
        await message.author.send(embed=embed_msg)
    
    # ファイルを送信する
    elif message.content.startswith('/send_file'):
        
        # コマンドを打った人のDMに送信
        await message.author.send(content='ファイル送信', file=discord.File('test.txt'))
        # discord.File()には、送信したいファイルの名前やファイルパスを入れます。
        # 例) 'image.jpg', './image/1.png', 'data.txt' など


token = os.environ.get('DISCORD_BOT_TOKEN')
client.run(token)
