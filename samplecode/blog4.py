import discord
import os

client = discord.Client(
    intents=discord.Intents.all()
)


@client.event
async def on_message(message):
    if not isinstance(message.channel, discord.TextChannel):
        return
    await message.channel.send('ここはTextChannelだよ')


token = os.environ.get('DISCORD_BOT_TOKEN')
client.run(token)
