import os
import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import mysql.connector

load_dotenv('.env')

# # DB connection
# mydb = mysql.connector.connect(
#     host=os.getenv('DB_HOST'),
#     user=os.getenv('DB_USER'),
#     password=os.getenv('DB_PASSWORD'),
#     database=os.getenv('DB_NAME')
# )
# mycursor = mydb.cursor()

# # SELECT QUERRY
# sqlstmt = 'SELECT * FROM `role`'
# mycursor.execute(sqlstmt)

# result = mycursor.fetchall()

# for x in result:
#     print(x)

# Logs
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.command(name='owner')
async def owner_find(ctx):
    server_owner = bot.get_user(int(ctx.guild.owner_id))
    await ctx.send(f'The owner of this server is : {server_owner}')
# @bot.command(name='help')



bot.run(os.getenv('TOKEN'), log_handler=handler, log_level=logging.DEBUG)