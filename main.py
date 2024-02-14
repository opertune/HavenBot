import os
import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
from commands.database import DB
import json

load_dotenv('.env')

# Logs
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='/', intents=intents)
database = DB()

# Help command
@bot.command(name='haven_help')
async def help(ctx):
    await ctx.send('!! Important!! You must place the \'Havenbot\' role above the other roles in your server settings')
    await ctx.send('To set roles to be automatically added to a newcomer, use the command /haven_autorole @role1 @role2 @role3. If you want to update the role reuse the same command as /haven_autorole @role1 @role3.')
    await ctx.send('If you want to remove all roles and your server from our database use /haven_delete')

# Add auto role in db
@bot.command(name='haven_autorole')
@commands.has_permissions(administrator=True) # Server owner restriction
async def addAutorole(ctx, *args):
    # list with role id
    roles = []
    for arg in args:
        roles.append(arg[3:-1])

    # Add the previous list in database or update it if the server has already an autorole
    if database.select("SELECT * FROM server WHERE server_id = %s", (ctx.message.guild.id,)):
        database.update("UPDATE server SET role_id = %s WHERE server_id = %s", (json.dumps(roles), ctx.message.guild.id))
        await ctx.send('Autorole updated.')
        await ctx.send(f'Autorole list : {args}.')
    else:
        database.insert("INSERT INTO server (server_id, role_id) VALUES (%s, %s)", (ctx.message.guild.id, json.dumps(roles)))
        await ctx.send('Autorole added.')
        await ctx.send(f'Autorole list : {args}.')

# Remove the server from database
@bot.command(name='haven_delete')
@commands.has_permissions(administrator=True)
async def deleteServer(ctx):
    database.delete("DELETE FROM server WHERE server_id = %s", (ctx.message.guild.id,))
    await ctx.send('Server and autorole removed from database')

# Get roles ind database and ddd roles to newcomer
@bot.event
async def on_member_join(member):
    roles = database.select("SELECT role_id FROM server WHERE server_id = %s", (member.guild.id,))
    for role in json.loads(roles[0][0]):
        await member.add_roles(bot.get_guild(member.guild.id).get_role(int(role)))

bot.run(os.getenv('TOKEN'), log_handler=handler, log_level=logging.DEBUG)