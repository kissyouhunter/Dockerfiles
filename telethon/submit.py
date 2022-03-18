#!/usr/bin/env python3

from telethon import TelegramClient

api_id = xxxxx #申请的TG API ID https://my.telegram.org
api_hash = 'XXXXXXXXX' #申请的TG API hash https://my.telegram.org

with TelegramClient('/telethon/kiss', api_id, api_hash) as client: #kiss为缓存的授权密钥，kiss可更改为任意名字，登录tg后会在文件夹下生成一个xxx.session的文件
    client.loop.run_until_complete(client.send_message('@JD_ShareCode_Bot', 'This is a test msg from telethon!')) #代码中的@JD_ShareCode_Bot为收信人的用户名，This is a test msg from telethon!为发送内容。比如想给发送一句/fruit xxxxx。这里就替换成('@JD_ShareCode_Bot', '/fruit xxxxx')。多条信息，多复制本行就可以，需格式对其。
