#Github.com/mrinvisible7

import time, os
import logging
from short import short_url
from .. import bot as Invix
from .. import userbot, Bot, TOKEN_TIMEOUT, bot_name
from .. import FORCESUB as fs
from main.plugins.pyroplug import get_msg
from main.plugins.helpers import get_link, join, screenshot

from telethon import events, Button
from pyrogram.errors import FloodWait
from uuid import uuid4
from ethon.telefunc import force_sub
#from main.plugins.helpers import force_sub

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.INFO)
logging.getLogger("telethon").setLevel(logging.INFO)

ft = f"You have to join @{fs} to use me."

message = "Send me the message link you want to start saving from, as a reply to this message."
          
process=[]
timer=[]
user=[]
user_data = {}

async def checking_access(event):     
    user_id = event.sender_id       
  #  if user_id in SUDO_USERS: 
     #  return True      
    if TOKEN_TIMEOUT:
        user_data.setdefault(user_id, {})
        data = user_data[user_id]
        expire = data.get('time')
        isExpired = expire is None or (expire is not None and (time.time() - expire) > TOKEN_TIMEOUT)
        if isExpired:
            token = data.get('token') or str(uuid4())
            if expire is not None:
                del data['time']
            data['token'] = token
            user_data[user_id].update(data)             
            await event.reply(f'**Generate new token to use me.**', 
                              buttons=[                              
                              [Button.url("Click Here to generate", url=short_url(f"https://telegram.me/{bot_name}?start={token}"))],
                              [Button.url("How to generate(video)", url="https://telegram.me/Filesharing6bot?start=Z2V0LTEzNzI1ODI3NTIyMDE0NQ")]])  
            return False
    return True, None

@Invix.on(events.NewMessage(incoming=True, func=lambda e: e.is_private))
async def clone(event):
    user_id = event.sender_id
    logging.info(event)
    file_name = ''
    if event.is_reply:
        reply = await event.get_reply_message()
        if reply.text == message:
            return
    lit=event.text
    li=lit.split("\n")
    if len(li) > 1:
        await event.reply("max 2 links per message")
        return
    for li in li:
        #1239
    
        try:
            link = get_link(li)
            if not link:
                return
    
        except TypeError:
            return
        s, r = await force_sub(event.client, fs, event.sender_id, ft)
        if s == False:
            await event.reply(ft)
            return
        if not await checking_access(event):
            return
        edit = await event.reply("Processing!")
        if f'{int(event.sender_id)}' in user:
            return await edit.edit("Please don't spam links, wait until ongoing process is done.")
        user.append(f'{int(event.sender_id)}')
        if "|" in li:
            url = li
            url_parts = url.split("|")
            if len(url_parts) == 2:
            
                file_name = url_parts[1]
        if file_name is not None:
            file_name = file_name.strip()                
        try:
            if 't.me/' not in link:
                await edit.edit("invalid link")
                ind = user.index(f'{int(event.sender_id)}')
                user.pop(int(ind))
                return
            if 't.me/' in link:
                msg_id = 0
                try:
                    msg_id = int(link.split("/")[-1])
                except ValueError:
                    if '?single' in link:
                        link_ = link.split("?single")[0]
                        msg_id = int(link_.split("/")[-1])
                    else:
                        msg_id = -1
                m = msg_id
                await get_msg(userbot, Bot, event.sender_id, edit.id, link, m, file_name)
        except FloodWait as fw:
            await Invix.send_message(event.sender_id, f'Try again after {fw.value} seconds due to floodwait from telegram.')
            await edit.delete()
        except Exception as e:
            logging.info(e)
            await Invix.send_message(event.sender_id, f"An error occurred during cloning of `{link}`\n\n**Error:** {str(e)}")
            await edit.delete()
        ind = user.index(f'{int(event.sender_id)}')
        user.pop(int(ind))
        time.sleep(1)
