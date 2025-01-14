from hikkatl.tl.types import Message

from .. import loader, utils


@loader.tds
class HyeKoMod(loader.Module):
    """Sends a HyeKo message with a photo"""

    strings = {"name": "HyeKo"}

    def __init__(self):
        self.config = loader.ModuleConfig(
            loader.ConfigValue(
                "photo_url",
                "https://0x0.st/s/WB5AYGf-ba6iPD6MMCfcYQ/8oT8.jpg",
                lambda: self.strings("_cfg_photo_url"),
                validator=loader.validators.Link(),
            )
        )

    @loader.command()
    async def hyoku(self, message: Message):
        """Sends the HyeKo message with a photo"""
        text = (
            "<emoji document_id=5400073337722388923>🗻</emoji> HYEKO\n"
            "<emoji document_id=5400073337722388923>🗻</emoji> Version: 1.6.5\n"
            "<emoji document_id=5400073337722388923>🗻</emoji> Forked: @arioncheck\n"
            "<emoji document_id=5400073337722388923>🗻</emoji> Designed: @arioncheck"
        )
        
        await utils.answer_file(message, self.config["photo_url"], text)
