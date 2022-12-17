---
title: Integration with Discord
description: The Discord bot with HackMD-API
tags: HackMD-Theme, HackMD-API, Discord-API
author: Mirai
---

{%hackmd @themes/dracula %}

# Discord Integration | Discord 整合

|Suggested by|Description|HackMD Profile
|--|--|--|
未來|Discord| [@Mirai1129](https://hackmd.io/@Mirai1129)

## Introduce

把Discord bot結合HackMD api，藉由Discord bot查詢自己的使用者資料，在未來希望能夠直接利用機器人寫筆記。

## Required

我使用的語言是Python，如果使用其他語言要自行更改喔

1. Python本體(廢話)
2. Requests套件
```
python -m pip install requests
```
3. Discord套件
([Pycord](https://docs.pycord.dev/en/stable/), [Nextcord](https://docs.nextcord.dev/en/stable/), [Discord.js](https://discord.js.org/#/) 等其中之一都可以)
[我用Nextcord簡單做的機器人](https://github.com/Mirai1129/DIscord-bot)，但HackMD功能未完全QQ。
4. Discord及HackMD的TOKEN

## Usage

如果你是用我做的[超簡易機器人](https://github.com/Mirai1129/DIscord-bot)的話，從Github下載下來後別忘記要建立一個 `.env` 檔喔，因為所有的Token都寫在裡面，而檔案裡要新增 `DISCORD_TOKEN` 以及 `HACKMD_TOKEN` 喔。

```env
DISCIRD_TOKEN = YOUR DISCORD TOKEN
HACKMD_TOKEN = YOUR HACKMD TOKEN
```

:::info
建議把機器人指令部分改為***Slash command***，以便跟上Discord的整合化，||偷偷告訴你們，擁有***Slash command***的機器人可以拿到[badge](https://support-dev.discord.com/hc/en-us/articles/10113997751447-Active-Developer-Badge)喔。||
:::

## 參考資料

- [HackMD API Documentation](https://hackmd.io/@hackmd-api/developer-portal)
- [HackMD OpenAPI](https://documenter.getpostman.com/view/68277/UVeNmhpT#363df43e-f4c8-4c88-82ed-0ac9ec4b85cd)
- [Disocrd API Documentation](https://discord.com/developers)
- [Nextcord API Documentation](https://docs.nextcord.dev)
