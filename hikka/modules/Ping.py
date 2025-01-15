from .. import loader, utils
import time

@loader.tds
class PingMod(loader.Module):
    """Пинг"""

    strings = {
        "name": "Ping",
    }

    async def client_ready(self, client, db):
        self.client = client
        self.db = db

    def __init__(self):
        self.config = loader.ModuleConfig(
            "ping_text",
            "<emoji document_id=5400073337722388923>🗻</emoji><b>Userbot:</b> {me}\n\n"
            "<emoji document_id=5400073337722388923>🗻</emoji><b>Ping:</b> {ping} ms\n"
            "<emoji document_id=5400073337722388923>🗻</emoji><b>Uptime:</b> {uptime}",
            """
            {me} - Имя пользователя,
            {ping} - Пинг,
            {uptime} - Аптайм
            """,
            "custom_ping_photo",
            "https://0x0.st/s/2EJW1BlwTOe4VKY_GN_Fkg/8o2c.jpg",
            "URL фото"
        )

    @loader.command()
    async def ping(self, message):
        """Показать пинг"""
        start = time.perf_counter_ns()
        msg = await message.client.send_message(message.peer_id, '<emoji document_id=5893431652578758294>✅</emoji>')
        ping = round((time.perf_counter_ns() - start) / 10**6, 3)
        await msg.delete()

        me = await self.client.get_me()

        info = self.config["ping_text"].format(
            me=me.first_name + ' ' + (me.last_name or ''),
            ping=ping,
            uptime=utils.formatted_uptime(),
        )
        
        if self.config["custom_ping_photo"] and self.config["custom_ping_photo"] != "None":
            await self.client.send_file(
                message.peer_id,
                self.config["custom_ping_photo"],
                caption=info
            )
        else:
            await utils.answer(message, info)

    @loader.command()
    async def setping(self, message):
        """Установить кастомный текст пинга: .setping <текст>"""
        args = utils.get_args_raw(message)
        if not args:
            await utils.answer(message, "Укажите текст")
            return

        self.config["ping_text"] = args
        await utils.answer(message, "Ping - текст поставлен")

    @loader.command()
    async def setpingphoto(self, message):
      """Установить фото"""
      args = utils.get_args_raw(message)
      if not args:
        await utils.answer(message, "<b>Укажите ссылку</b>")
        return
      
      self.config["custom_ping_photo"] = args
      await utils.answer(message, "<b>Ссылка поставлена</b>")
