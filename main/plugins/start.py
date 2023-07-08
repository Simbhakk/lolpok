#Github.com/mrinvisible7

from time import time
from uuid import uuid4
from pyrogram import Client, filters, enums
import os
from button_build import ButtonMaker
from .. import bot as Invix, Bot
from main.plugins.frontend import user_data
from telethon import events, Button

#from ethon.mystarts import start_srb
    
S = '/' + 's' + 't' + 'a' + 'r' + 't'

@Invix.on(events.callbackquery.CallbackQuery(data="set"))
async def sett(event):    
    Invix = event.client
    button = await event.get_message()
    msg = await button.get_reply_message()
    await event.delete()
    async with Invix.conversation(event.chat_id) as conv: 
        xx = await conv.send_message("Send me any image for thumbnail as a `reply` to this message.")
        x = await conv.get_reply()
        if not x.media:
            xx.edit("No media found.")
        mime = x.file.mime_type
        if 'png' not in mime and 'jpg' not in mime and 'jpeg' not in mime:
            return await xx.edit("No image found.")
        await xx.delete()
        t = await event.client.send_message(event.chat_id, 'Trying.')
        path = await event.client.download_media(x.media)
        if os.path.exists(f'{event.sender_id}.jpg'):
            os.remove(f'{event.sender_id}.jpg')
        os.rename(path, f'./{event.sender_id}.jpg')
        await t.edit("Temporary thumbnail saved!")
        
@Invix.on(events.callbackquery.CallbackQuery(data="rem"))
async def remt(event):  
    Invix = event.client            
    await event.edit('Trying.')
    try:
        os.remove(f'{event.sender_id}.jpg')
        await event.edit('Removed!')
    except Exception:
        await event.edit("No thumbnail saved.")                        
  
@Bot.on_message(filters.command("start") & filters.private)
async def start(_, message):
    if len(message.command) > 1:
        userid = message.from_user.id
        input_token = message.command[1]
        if userid not in user_data:
            return await message.reply_text('This token is not for you.')
        data = user_data[userid]
        if 'token' not in data or data['token'] != input_token:
            return await message.reply_text('This is a token already expired')
        data['token'] = str(uuid4())
        data['time'] = time()
        user_data[userid].update(data)
        return await message.reply_text('Token refreshed successfully! For 30 min.')    
    else:
        text = "👋 Hi, I'm Save Restricted content Bot.\n\n**•FOR PUBLIC CHANNEL**\n-Send direct message/videos link from channel to clone it.\n~~~~~----~~~~~~\n**•⚠️FOR PRIVATE CHANNEL/GROUP**\n-First send channel link then message or video link to download.\n\nNote:- This bot is based on token. Press /help for more info."
    #await start_srb(event, text)        
        buttons = ButtonMaker()             
        buttons.ibutton("SET THUMB.", "set")
        buttons.ibutton("REM THUMB.", "rem")
        buttons.ubutton(f"How to use bot (click)", f"https://telegram.me/Filesharing6bot?start=Z2V0LTEzODI2MDE2MDQ0MDczMA") 
        reply_markup = buttons.build_menu(2)
        await message.reply_text(text=text, reply_markup=reply_markup)
        
@Invix.on(events.NewMessage(incoming=True, pattern='/help'))                       
async def donate(event):
    text = "**This bot is based on token**\nwhen you send post link to bot. Bot will give you token url. You have to open it.( you can see video ,if you dont now how to open) .\n\nAnd this token will be valid for 30 min. after 30 min. you have to generate new token." 
    await event.reply(text)                           
    '''
    await event.reply(text, 
                      buttons=[
                              [Button.inline("SET THUMB.", data="set"),
                               Button.inline("REM THUMB.", data="rem")],
                              [Button.url("Maintained and Modified by", url="t.me/Raj02_bots")]])
    '''
    
