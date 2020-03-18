import discord
import yfinance as yf
from yahoo_fin import stock_info as si

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
    await client.process_commands(message)

#sad
@client.event
async def on_message(message):
    if message.content.find("sad") != -1:
        await message.channel.send("F")
    await client.process_commands(message)

#sad
@client.event
async def on_message(message):
    if message.content.find("lol") != -1:
        await message.channel.send("lol")
    await client.process_commands(message)


#sad
@client.event
async def on_message(message):
    if message.content.find("losdfsdfl") != -1:
        await message.channel.send("losfdsfsl")
    await client.process_commands(message)

#fdklfsdlkf
@client.event
async def on_ready():
    print('CORRIENDO')

client.run('Njg5NDE5NjQ4MzY5Njg4NzY3.XnC3aQ.50hiX55CC7rJy1573c9ctb3SyUg')


#
#
# @bot.command()
# async def multiply(ctx, a: int, b: int):
#     await ctx.send(a*b)
#
# @bot.command()
# async def greet(ctx):
#     await ctx.send(":smiley: :wave: Hello, there!")
#
# @bot.commands()
# async def cat(ctx):
#     await ctx.send("https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif")
#
# bot.run('Njg5NDE5NjQ4MzY5Njg4NzY3.XnC10A.8wyLE3XZ3UehHM0-4vlvvdfkJXY')