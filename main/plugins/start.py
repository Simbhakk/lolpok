#Github.com/mrinvisible7

from time import time
from uuid import uuid4
from pyrogram import Client, filters, enums
import os
from button_build import ButtonMaker
from .. import bot as Invix, Bot
from main.plugins.frontend import user_data
from telethon import events, Button

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
        text = "👋 Hi, I am a Save Bot. I can copy messages from PUBLIC RESTRICTED CHANNEL.\n\n**•Send direct message/video link from public channel.\n\n🚨Note- Our bot doesn't copy message from private channel & group."
    #await start_srb(event, text)        
        buttons = ButtonMaker()             
        buttons.ubutton("SOURCE", "https://t.me/Bypass_Restricted/68")
        buttons.ubutton("PREMIUM", "https://t.me/Bypass_Restricted/66")
        buttons.ubutton(f"How to use bot (click)", f"https://telegram.me/Filesharing6bot?start=Z2V0LTEzODI2MDE2MDQ0MDczMA") 
        reply_markup = buttons.build_menu(2)
        await message.reply_text(text=text, reply_markup=reply_markup)                             
                              
    '''
    await event.reply(text, 
                      buttons=[
                              [Button.inline("SET THUMB.", data="set"),
                               Button.inline("REM THUMB.", data="rem")],
                              [Button.url("Maintained and Modified by", url="t.me/Raj02_bots")]])
    '''
    
