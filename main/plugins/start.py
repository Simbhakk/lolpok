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
        photo ="https://graph.org/file/afa9243d3bb22e2f4d626.jpg",
        caption = "👋I am a Save Restricted Bot. I can copy messages **\nFROM PUBLIC RESTRICTED CHANNEL ONLY.\n\n•Send message link from channel to clone it here.**\n\n🚨Note:- 1.Our bot is based on /token for earning.\n2.Bot doesn't copy message from private channel/group & public group."
    #await start_srb(event, text)        
        buttons = ButtonMaker()             
        buttons.ubutton("SOURCE", "https://t.me/Save_Restricted_contentz/19")
        buttons.ubutton("PREMIUM", "https://t.me/Save_Restricted_contentz/18")
        buttons.ubutton("How to use this Bot", "https://telegram.me/Filesharing6bot?start=Z2V0LTEzODI2MDE2MDQ0MDczMA") 
        reply_markup = buttons.build_menu(2)
        await message.reply_text(text=text, reply_markup=reply_markup)                             

# @Bot.on_message(filters.command("token"))
                              
    '''
    await event.reply(text, 
                      buttons=[
                              [Button.inline("SET THUMB.", data="set"),
                               Button.inline("REM THUMB.", data="rem")],
                              [Button.url("Maintained and Modified by", url="t.me/Raj02_bots")]])
    '''
    
