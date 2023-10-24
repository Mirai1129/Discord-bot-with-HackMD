## Introduce

把 Discord bot 結合 HackMD api，藉由 Discord bot 查詢自己的使用者資料，在未來希望能夠直接利用機器人寫筆記。

## Required

1. Python
2. Requests 套件
```
python -m pip install requests
```
3. Discord 套件
([Pycord](https://docs.pycord.dev/en/stable/), [Nextcord](https://docs.nextcord.dev/en/stable/) 類似套件都可以)
[我用Nextcord簡單做的機器人](https://github.com/Mirai1129/DIscord-bot)。
4. Discord 及 HackMD 的 TOKEN

## Usage

建立一個 `.env` 檔，範例如下：

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
