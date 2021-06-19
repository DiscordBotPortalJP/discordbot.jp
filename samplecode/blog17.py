# 対策1

@bot.event
async def on_message(message):
    if message.content == "/neko":
        await message.channel.send("にゃーん")
    
    await bot.process_commands(message)  # 基本的にはすべての処理の最後につける

# 対策2

@bot.listen()  # かっこが必要
async def on_message(message):
    if message.content == "/neko":
        await message.channel.send("にゃーん")

# 対策2(関数名変更ver)

@bot.listen("on_message")  # かっこの中にイベント名を入れる
async def on_message_neko(message):
    if message.content == "/neko":
        await message.channel.send("にゃーん")

# おまけ

from discord.ext import commands

class MyCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(message):
        if message.content == "/neko":
            await message.channel.send("にゃーん")
