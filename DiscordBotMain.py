import discord
import yfinance as yf
from yahoo_fin import stock_info as si
import os

#escribir en la consola pipreqs C:\Users\Administrador\PycharmProjects\DiscordBot para generar requirementgi

from discord.ext import commands

#https://discordpy.readthedocs.io/en/latest/faq.html#why-does-on-message-make-my-commands-stop-working
#@client.event
#async def on_message(message):
#    print(message.content)#los mensajes seran impresos en la consola

from discord.ext import commands

client = discord.Client()
client = commands.Bot(command_prefix='$')


#remueve el comando help por defecto
client.remove_command('help')
#agrega nuevo comando ayuda
@client.command()
async def help(ctx):
    embed = discord.Embed(title="Titulo", description="descripcion descriptiva", color=0xeee657)
    embed.add_field(name="$test lol", value="Regresa lol", inline=False)
    embed.add_field(name="$accion TICKER",value="Regresa el precio de **TICKER**")
    await ctx.send(embed=embed)


#commandos
@client.command()
async def test(ctx, arg):
    await ctx.send(arg)


@client.command()
async def accion(ctx, stock):
    await ctx.send("espera.. OwO")
    try:
        temp=stock+' esta en = '+ str(si.get_live_price(stock))+' USD'
        await ctx.send(temp)
    except:
        await ctx.send("Ticker no encontrado >w<")

#si encuentra una palabra en el mensaje, envia otro mensaje
#evento anti gey
@client.event
async def on_message(message):
    if message.content.find("gey") != -1 or message.content.find("gay") != -1 or message.content.find("homo") != -1:
        await message.channel.send("No U")
    elif message.content.find("sad") != -1:
        await message.channel.send("F")
    if message.content.find('lol') != -1 and message.author.id != client.user.id:
        await message.channel.send('lol')
    await client.process_commands(message)


print(os.environ.get("BOT_TOKEN_UWU"))

#sad
@client.event
async def on_ready():
    print('CORRIENDO')

client.run(os.environ.get("BOT_TOKEN_UWU"))
