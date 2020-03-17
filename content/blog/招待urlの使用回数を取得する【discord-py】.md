---
title: 招待URLの使用回数を取得する【discord.py】
date: 2020-01-18T11:44:12.720Z
categories:
  - discord.py
draft: false
---
[discord.Invite.uses](https://discordpy.readthedocs.io/en/latest/api.html#discord.Invite.uses)

Invite クラスの uses プロパティから取得できます。 返り値は int 型です。

## サンプルコード

以下は `/invite` というコマンドを打った時、
特定のユーザが作成した招待URLの使用回数を取得するコードです。

```python
@client.event
async def on_message(message):
    # /invite というコマンドで反応する
    if message.content != '/invite_count':
        return

    # サーバーの招待URLのリストを取得する
    invites = message.guild.invites

    # 特定のユーザが作成した招待URLを取得
    user_id = 462810739204161537
    invite = discord.utils.get(invites, inviter__id=user_id)

    # 招待URLの使用回数を取得
    count_use = invite.uses

    # チャンネルに情報を送信
    await message.channel.send(f'招待URLの仕様回数：{count_use}')
```

## 参考リンク

- [discord.Invite.uses](https://discordpy.readthedocs.io/en/latest/api.html#discord.Invite.uses)
- [discord.Guild.invites](https://discordpy.readthedocs.io/en/latest/api.html#discord.Guild.invites)
- [discord.abc.GuildChannel.invites](https://discordpy.readthedocs.io/en/latest/api.html#discord.abc.GuildChannel.invites)
- [discord.utils.get](https://discordpy.readthedocs.io/en/latest/api.html#discord.utils.get)
