#Github.com/mrinvisible7

from time import time
from uuid import uuid4
from pyrogram import Client, filters, enums
import os
#from button_build import ButtonMaker
from .. import bot as Invix, Bot, TOKEN_TIMEOUT
from main.plugins.frontend import user_data
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

@Bot.on_message(filters.command("help"))
async def help(_, message):
        text = "Bot can copy message from:- \n Public restricted channel ✅\n Public restricted Group ❌\n Private restricted channel ❌ \n private restricted group ❌"
        await message.reply_text(text=text)
        
@Bot.on_message(filters.command("token"))
async def token(_, message):
        text = "♨️ Bot is based on token , So that bot owner can earn some money and you can use bot without time limit. Watch ads , use bot and respect our work.\n Thanks 🙌"
        await message.reply_text(text=text)

@Bot.on_message(filters.command("start"))
async def start(_, message):
    if len(message.command) > 1:
        userid = message.from_user.id
        input_token = message.command[1]
        if userid not in user_data:
            return await message.reply_text('Who are you?')
        data = user_data[userid]
        if 'token' not in data or data['token'] != input_token:
            return await message.reply_text('This is a token already expired')
        data['token'] = str(uuid4())
        data['time'] = time()
        user_data[userid].update(data)
        token_refresh_hours, remainder = divmod(int(TOKEN_TIMEOUT), 3600) 
        token_refresh_minutes = remainder // 60 
        #token_refresh_minutes = int(TOKEN_TIMEOUT) // 60  # Convert seconds to minutes
        return await message.reply_text(f'Token refresh successfully for {token_refresh_hours} hours and {token_refresh_minutes} minutes.')
    else:
        
            start_text = """𝗜 𝗮𝗺 𝗮 𝗦𝗮𝘃𝗲 𝗥𝗲𝘀𝘁𝗿𝗶𝗰𝘁𝗲𝗱 𝗕𝗼𝘁. 𝗜 𝗰𝗮𝗻 𝗰𝗼𝗽𝘆 𝗺𝗲𝘀𝘀𝗮𝗴𝗲𝘀 𝗙𝗥𝗢𝗠 𝗣𝗨𝗕𝗟𝗜𝗖 𝗥𝗘𝗦𝗧𝗥𝗜𝗖𝗧𝗘𝗗 𝗖𝗛𝗔𝗡𝗡𝗘𝗟 𝗢𝗡𝗟𝗬.\n\n•𝙎𝙚𝙣𝙙 𝙢𝙚𝙨𝙨𝙖𝙜𝙚 𝙡𝙞𝙣𝙠 𝙛𝙧𝙤𝙢 𝙘𝙝𝙖𝙣𝙣𝙚𝙡 𝙩𝙤 𝙘𝙡𝙤𝙣𝙚 𝙞𝙩 𝙝𝙚𝙧𝙚.\n\n🚨Note:- 𝟷.Oᴜʀ ʙᴏᴛ ɪs ʙᴀsᴇᴅ ᴏɴ /token ғᴏʀ ᴇᴀʀɴɪɴɢ.\n𝟸.Bᴏᴛ ᴅᴏᴇsɴ'ᴛ ᴄᴏᴘʏ ᴍᴇssᴀɢᴇ ғʀᴏᴍ ᴘʀɪᴠᴀᴛᴇ ᴄʜᴀɴɴᴇʟ/\nɢʀᴏᴜᴘ & ᴘᴜʙʟɪᴄ ɢʀᴏᴜᴘ. Tʏᴘᴇ /help ғᴏʀ ᴍᴏʀᴇ ɪɴғᴏ."""
            await message.reply_text(start_text,
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton('👁️ Close', callback_data='cancel')]
                ]
            ))
@Bot.on_callback_query(filters.regex("cancel"))
async def cancel(client, callback_query):
    await callback_query.message.delete()
