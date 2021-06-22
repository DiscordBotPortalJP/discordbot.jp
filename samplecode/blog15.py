import discord
import os

client = discord.Client(
    intents=discord.Intents.all()
)


@client.event
# BOTが起動したときに発火するイベント 'on_ready'
async def on_ready():
    # 認識しているサーバーをlist型で取得し、その要素の数を 変数:guild_count に格納しています。
    guild_count = len(client.guilds)
    # 関数:lenは、引数に指定したオブジェクトの長さや要素の数を取得します。

    game = discord.Game(f'{guild_count} サーバー数に導入されています')
    # f文字列(フォーマット済み文字列リテラル)は、Python3.6からの機能です。

    # BOTのステータスを変更する
    await client.change_presence(status=discord.Status.online, activity=game)
    # パラメーターの status でステータス状況(オンライン, 退席中など)を変更できます。

    print('ログインしました')


token = os.environ.get('DISCORD_BOT_TOKEN')
client.run(token)
