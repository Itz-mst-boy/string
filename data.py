from pyrogram.types import InlineKeyboardButton


class Data:
    generate_single_button = [InlineKeyboardButton(" ɢᴇɴᴇʀᴀᴛᴇ sᴇssɪᴏɴ ", callback_data="generate")]

    generate_button = [generate_single_button]

    buttons = [
        generate_single_button,
        [InlineKeyboardButton("❣️ sᴜᴩᴩᴏʀᴛ ❣️", url="https://t.me/worldwide_friend_zone"),
         InlineKeyboardButton("🥀ᴍᴏɪ ɴᴇᴛᴡᴏʀᴋ 🥀", url="https://t.me/mastermind_network_official"),
        ],
    ]

    START = """
Hᴇʏ {},

Tʜɪs ɪs {},
A sᴛʀɪɴɢ sᴇssɪᴏɴ ɢᴇɴᴇʀᴀᴛᴏʀ ʙᴏᴛ, ᴡʀɪᴛᴛᴇɴ ɪɴ ᴩʏᴛʜᴏɴ ᴡɪᴛʜ ᴛʜᴇ ʜᴇʟᴩ ᴏғ ᴩʏʀᴏɢʀᴀᴍ.

ᴊᴏɪɴ: [sᴜᴘᴘᴏʀᴛ ᴄʜᴀᴛ](https://t.me/worldwide_friend_zone)
Mᴀᴅᴇ ᴡɪᴛʜ ❤ ʙʏ : [ᴍᴜᴋᴇsʜ](https://t.me/itz_mst_boi) !
    """
