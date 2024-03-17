#Github.com/mrinvisible7

from time import time
from uuid import uuid4
from pyrogram import Client, filters, enums
import os
from button_build import ButtonMaker
from .. import bot as Invix, Bot
from main.plugins.frontend import user_data
from telethon import events, Button

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
        return await message.reply_text('Token refreshed successfully! For 30 min.')    
    else:
        text = "👋,𝗜 𝗮𝗺 𝗮 𝗦𝗮𝘃𝗲 𝗥𝗲𝘀𝘁𝗿𝗶𝗰𝘁𝗲𝗱 𝗕𝗼𝘁. 𝗜 𝗰𝗮𝗻 𝗰𝗼𝗽𝘆 𝗺𝗲𝘀𝘀𝗮𝗴𝗲𝘀 𝗙𝗥𝗢𝗠 𝗣𝗨𝗕𝗟𝗜𝗖 𝗥𝗘𝗦𝗧𝗥𝗜𝗖𝗧𝗘𝗗 𝗖𝗛𝗔𝗡𝗡𝗘𝗟 𝗢𝗡𝗟𝗬.\n\n•𝙎𝙚𝙣𝙙 𝙢𝙚𝙨𝙨𝙖𝙜𝙚 𝙡𝙞𝙣𝙠 𝙛𝙧𝙤𝙢 𝙘𝙝𝙖𝙣𝙣𝙚𝙡 𝙩𝙤 𝙘𝙡𝙤𝙣𝙚 𝙞𝙩 𝙝𝙚𝙧𝙚.\n\n🚨Note:- 𝟷.Oᴜʀ ʙᴏᴛ ɪs ʙᴀsᴇᴅ ᴏɴ /token ғᴏʀ ᴇᴀʀɴɪɴɢ.\n𝟸.Bᴏᴛ ᴅᴏᴇsɴ'ᴛ ᴄᴏᴘʏ ᴍᴇssᴀɢᴇ ғʀᴏᴍ ᴘʀɪᴠᴀᴛᴇ ᴄʜᴀɴɴᴇʟ/\nɢʀᴏᴜᴘ & ᴘᴜʙʟɪᴄ ɢʀᴏᴜᴘ. Tʏᴘᴇ /help ғᴏʀ ᴍᴏʀᴇ ɪɴғᴏ."
    #await start_srb(event, text)        
        buttons = ButtonMaker()             
        buttons.ubutton("SOURCE", "https://t.me/Save_Restricted_contentz/19")
        buttons.ubutton("PREMIUM", "https://t.me/Save_Restricted_contentz/18")
        buttons.ubutton("How to use this Bot", "https://telegram.me/Filesharing6bot?start=Z2V0LTEzODI2MDE2MDQ0MDczMA") 
        reply_markup = buttons.build_menu(2)
        await message.reply_text(text=text, reply_markup=reply_markup)

    '''
    await event.reply(text, 
                      buttons=[
                              [Button.inline("SET THUMB.", data="set"),
                               Button.inline("REM THUMB.", data="rem")],
                              [Button.url("Maintained and Modified by", url="t.me/Raj02_bots")]])
    '''
    
