import importlib
from pyrogram import idle
from uvloop import install


from Kazu.modules import ALL_MODULES
from Kazu import BOTLOG_CHATID, LOGGER, LOOP, aiosession, app, bots, ids
from Kazu.modules.basic import join

BOT_VER = "2.0.0"
CMD_HANDLER = ["." "," "?" "!"]
MSG_ON = """
💢 **𝙻𝙸𝙻𝚈-𝚄𝚂𝙴𝚁𝙱𝙾𝚃 𝚃𝙴𝙻𝙰𝙷 𝙰𝙺𝚃𝙸𝙵** 💢
╼┅━━━━━━━━━╍━━━━━━━━━┅╾
❍▹ **𝚄𝚂𝙴𝚁𝙱𝙾𝚃 𝚅𝙴𝚁𝚂𝙸𝙾𝙽 -** `{}`
❍▹ **𝙺𝙴𝚃𝙸𝙺** `{}help` **𝚄𝙽𝚃𝚄𝙺 MELIHAT MODULE**
╼┅━━━━━━━━━╍━━━━━━━━━━┅╾
"""


async def main():
    await app.start()
    print("LOG: Founded Bot token Booting..")
    for all_module in ALL_MODULES:
        importlib.import_module("Kazu.modules" + all_module)
        print(f"Successfully Imported {all_module} ")
    for bot in bots:
        try:
            await bot.start()
            ex = await bot.get_me()
            await join(bot)
            try:
                await bot.send_message(BOTLOG_CHATID, MSG_ON.format(BOT_VER, CMD_HANDLER))
            except BaseException:
                pass
            print(f"Started as {ex.first_name} | {ex.id} ")
            ids.append(ex.id)
        except Exception as e:
            print(f"{e}")
    await idle()
    await aiosession.close()


if __name__ == "__main__":
    LOGGER("Kazu").info("PyroZu-Userbot Telah Aktif")
    install()
    LOOP.run_until_complete(main())
