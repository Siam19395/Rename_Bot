from pyrogram import Client, filters, enums
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup 
from config import ADMIN
 

@Client.on_callback_query(filters.regex("start"))
async def start(bot, msg, cb=True):   
    txt=f"Hey {msg.from_user.mention} I'm Rin Toosaka a rename bot for personal usage.\nThis bot is made by <b><a href=https://t.me/Chowdhury_Siam>Siam Chowdhury</a></b>"                                     
    button= [[
        InlineKeyboardButton("🛠️ Owner Channel", url="https://t.me/Anime_Kun_Channel")
        ],[
        InlineKeyboardButton("ℹ️ Help", callback_data="help"),
        InlineKeyboardButton("📡 About", callback_data="about") 
    ]]  
    if cb:
        await msg.message.edit(text=txt, reply_markup=InlineKeyboardMarkup(button), disable_web_page_preview = True, parse_mode=enums.ParseMode.HTML)
    else:
        await msg.reply_text(text=txt, reply_markup=InlineKeyboardMarkup(button), disable_web_page_preview = True, parse_mode=enums.ParseMode.HTML)


@Client.on_callback_query(filters.regex("help"))
async def help(bot, msg):
    txt=f"just send a file and /rename <new name> with replayed your file\n\nReply a photo and send /set to set temporary thumbnail\n/view to see your thumbnail"
    button= [[        
        InlineKeyboardButton("🚫 Close", callback_data="del"),
        InlineKeyboardButton("⬅️ Back", callback_data="start") 
    ]]  
    await msg.message.edit(text=txt, reply_markup=InlineKeyboardMarkup(button), disable_web_page_preview = True)


@Client.on_callback_query(filters.regex("about"))
async def about(bot, msg):
    me=await bot.get_me()
    Master=f"<a href=https://t.me/Chowdhury_Siam>Siam Chowdhury</a>"
    Source="<a href=https://github.com/Siam19395/Rename_Bot>Click Here</a>"
    txt=f"<b>Bot Name: {me.mention}\nDeveloper: <a href=https://t.me/Chowdhury_Siam>Siam Chowdhury</a>\nOwner Channel: <a href=https://t.me/Anime_Kun_Channel>Anime Kun</a>\nMy Master's: {Master}\nSource Code: {Source}</b>"                 
    button= [[        
        InlineKeyboardButton("🚫 Close", callback_data="del"),
        InlineKeyboardButton("⬅️ Back", callback_data="start") 
    ]]  
    await msg.message.edit(text=txt, reply_markup=InlineKeyboardMarkup(button), disable_web_page_preview = True, parse_mode=enums.ParseMode.HTML)


@Client.on_callback_query(filters.regex("del"))
async def closed(bot, msg):
    try:
        await msg.message.delete()
    except:
        return


@Client.on_callback_query(filters.regex("start"))
async def start(bot, msg, cb=True):   
    txt=f"Hey {msg.from_user.mention} I'm Rin Toosaka a rename bot for personal usage.\nThis bot is made by <b><a href=https://t.me/Chowdhury_Siam>Siam Chowdhury</a></b>"                                     
    button= [[
        InlineKeyboardButton("🛠️ Owner Channel", url="https://t.me/Anime_Kun_Channel")
        ],[
        InlineKeyboardButton("ℹ️ Help", callback_data="help"),
        InlineKeyboardButton("📡 About", callback_data="about") 
    ]]  
    if cb:
        await msg.message.edit(text=txt, reply_markup=InlineKeyboardMarkup(button), disable_web_page_preview = True, parse_mode=enums.ParseMode.HTML)
    else:
        await msg.reply_text(text=txt, reply_markup=InlineKeyboardMarkup(button), disable_web_page_preview = True, parse_mode=enums.ParseMode.HTML)


@Client.on_callback_query(filters.regex("help"))
async def help(bot, msg):
    txt=f"just send a file and /rename <new name> with replayed your file\n\nReply a photo and send /set to set temporary thumbnail\n/view to see your thumbnail"
    button= [[        
        InlineKeyboardButton("🚫 Close", callback_data="del"),
        InlineKeyboardButton("⬅️ Back", callback_data="start") 
    ]]  
    await msg.message.edit(text=txt, reply_markup=InlineKeyboardMarkup(button), disable_web_page_preview = True)


@Client.on_callback_query(filters.regex("about"))
async def about(bot, msg):
    me=await bot.get_me()
    Master=f"<a href=https://t.me/Chowdhury_Siam>Siam Chowdhury</a>"
    Source="<a href=https://github.com/Siam19395/Rename_Bot>Click Here</a>"
    txt=f"<b>Bot Name: {me.mention}\nDeveloper: <a href=https://t.me/Chowdhury_Siam>Siam Chowdhury</a>\nOwner Channel: <a href=https://t.me/Anime_Kun_Channel>Anime Kun</a>\nMy Master's: {Master}\nSource Code: {Source}</b>"                 
    button= [[        
        InlineKeyboardButton("🚫 Close", callback_data="del"),
        InlineKeyboardButton("⬅️ Back", callback_data="start") 
    ]]  
    await msg.message.edit(text=txt, reply_markup=InlineKeyboardMarkup(button), disable_web_page_preview = True, parse_mode=enums.ParseMode.HTML)


@Client.on_callback_query(filters.regex("del"))
async def closed(bot, msg):
    try:
        await msg.message.delete()
    except:
        return


