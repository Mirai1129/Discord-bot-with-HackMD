## Introduce

把 Discord bot 結合 HackMD api，藉由 Discord bot 查詢自己的使用者資料，在未來希望能夠直接利用機器人寫筆記。

## Required

我使用的語言是 Python，如果使用其他語言要自行更改喔

1. Python
2. Requests 套件
```
python -m pip install requests
```
3. Discord 套件
([Pycord](https://docs.pycord.dev/en/stable/), [Nextcord](https://docs.nextcord.dev/en/stable/), [Discord.js](https://discord.js.org/#/) 等其中之一都可以)
[我用Nextcord簡單做的機器人](https://github.com/Mirai1129/DIscord-bot)。
4. Discord 及 HackMD 的 TOKEN

## Usage

如果你是用我做的[超簡易機器人](https://github.com/Mirai1129/DIscord-bot)的話，從 Github 下載下來後別忘記要建立一個 `.env` 檔喔，因為所有的 Token 都寫在裡面，而檔案裡要新增 `DISCORD_TOKEN` 以及 `HACKMD_TOKEN` 喔。

```env
DISCIRD_TOKEN = YOUR DISCORD TOKEN
HACKMD_TOKEN = YOUR HACKMD TOKEN
```


建議把機器人指令部分改為***Slash command***，以便跟上 Discord 的整合化。

## 參考資料

- [HackMD API Documentation](https://hackmd.io/@hackmd-api/developer-portal)
- [HackMD OpenAPI](https://documenter.getpostman.com/view/68277/UVeNmhpT#363df43e-f4c8-4c88-82ed-0ac9ec4b85cd)
- [Disocrd API Documentation](https://discord.com/developers)
- [Nextcord API Documentation](https://docs.nextcord.dev)
