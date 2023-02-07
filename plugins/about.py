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
	await message.reply_text(f"👉🏻Total User:- {total_user()}\n👉🏻Developer :- @mrmalik_offl\n👉🏻Buy Subscription :- @mrmalik_offl\n👉🏻Bot Updates :- https://youtube.com/@GreyMattersYT\n\n👉🏻Total Renamed File :-{total_rename}\nTotal Size Renamed :- {humanbytes(int(total_size))} ",quote=True)
