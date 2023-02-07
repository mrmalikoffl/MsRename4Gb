import os 
from pyrogram import Client, filters
token = os.environ.get('TOKEN','')
botid = token.split(':')[0]
from helper.database import botdata, find_one, total_user
from helper.progress import humanbytes
@Client.on_message(filters.private & filters.command(["about"]))
async def start(client,message):
	botdata(int(botid))
	data = find_one(int(botid))
	total_rename = data["total_rename"]
	total_size = data["total_size"]
	await message.reply_text(f"👉🏻𝙏𝙤𝙩𝙖𝙡 𝙐𝙨𝙚𝙧𝙨: {total_user()}\n\n👉🏻𝘿𝙚𝙫𝙚𝙡𝙤𝙥𝙚𝙧: @mrmalik_offl\n\n👉🏻𝙁𝙤𝙧 𝙋𝙡𝙖𝙣 𝙐𝙥𝙜𝙧𝙖𝙙𝙚: @mrmalik_offl\n\n👉🏻𝘽𝙤𝙩 𝙐𝙥𝙙𝙖𝙩𝙚𝙨: https://t.me/+rN9QCFgIihgyZWM1\n\n👉🏻𝙏𝙤𝙩𝙖𝙡 𝙍𝙚𝙣𝙖𝙢𝙚𝙙 𝙁𝙞𝙡𝙚𝙨: {total_rename}\n\n𝙏𝙤𝙩𝙖𝙡 𝙎𝙞𝙯𝙚 𝙍𝙚𝙣𝙖𝙢𝙚𝙙: {humanbytes(int(total_size))}\n\n𝐓𝐡𝐚𝐧𝐤 𝐘𝐨𝐮 𝐅𝐨𝐫 𝐔𝐬𝐢𝐧𝐠 𝐌𝐞",quote=True)
