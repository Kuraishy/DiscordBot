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
#------------------------------------------AYUDA-------------------------------------------------------------------------
@client.command()
async def help(ctx):
    embed = discord.Embed(title="Titulo", description="descripcion descriptiva", color=0xeee657)
    embed.set_footer(text='TICKER = AMD, SPCE, BRZU, TSLA, MSFT... codigo de las acciones')
    #embed.set_thumbnail(url='https://s.pacn.ws/640/u5/love-live-sunshine-nesoberi-plush-watanabe-you-cyaron-m-542929.1.jpg?oy1sqe')
    embed.set_thumbnail(url=client.user.avatar_url)
    embed.set_author(name=client.user.name,url=client.user.avatar_url,icon_url=client.user.avatar_url)
    embed.set_image(url=client.user.avatar_url)
    embed.add_field(name="$accion TICKER",value="Regresa el precio de **TICKER**", inline=False)
    embed.add_field(name="$perdedores", value="Regresa los top **perdedores** del dia", inline=False)
    embed.add_field(name="$ganadores", value="Regresa los top **ganadores** del dia", inline=False)
    embed.add_field(name="$info TICKER", value="Regresa informacion basica del **TICKER**", inline=False)
    embed.add_field(name="$informacion TICKER", value="lo mismo que $info pero regresa tambien la descripcion de la empresa", inline=False)
    await ctx.send(embed=embed)


#crear embebed para los pededores y ganadores-------------------------------------------------------------------
def crearEmbed(ctx, temp, titulo, descripcion,url,color):
    embed = discord.Embed(
        title=titulo,
        description=descripcion,
        color=color
    )
    embed.set_footer(text='lol')
    embed.set_image(
        url=url)
    # embed.set_thumbnail(url='https://s.pacn.ws/640/u5/love-live-sunshine-nesoberi-plush-watanabe-you-cyaron-m-542929.1.jpg?oy1sqe')
    # embed.set_author(name='nombre autor', icon_url='https://otsukai.com/optimized?key=public/item/560/original-5aeb58b3a350d.jpg&operation=resize&w=960')
    embed.add_field(name='Symbolo', value=temp['Symbol'], inline=True)
    embed.add_field(name='Nombre', value=temp['Name'], inline=True)
    embed.add_field(name='Precio', value=temp['Price (Intraday)'], inline=True)
    embed.add_field(name='Cambio', value=temp['Change'], inline=True)
    embed.add_field(name='Cambio %', value=temp['% Change'], inline=True)
    embed.add_field(name='P/E %', value=temp['PE Ratio (TTM)'], inline=True)
    return embed

#------------------------------------crear embed para infomracion------------------------------------------
def crearEmbedInfo(ctx, lol,tipo):
    try:
        temp=yf.Ticker(lol).info
        tempDesc = temp['sector'] + ', ' + temp['industry'] + ', ' + '\n' + '\n' + temp['longBusinessSummary']
        # print(tempDesc)
        if tipo is 0:  # si pide la informacion completa (descripcion de la compañia)
            embed = discord.Embed(
                title=lol,
                description=tempDesc,
                color=0x0000FF
            )
        else:  # descripcion corta (sin descripcion de la compañia
            embed = discord.Embed(
                title=lol,
                description='descripcion de la accion',
                color=0x0000FF
            )
    except:
        temp = yf.Ticker('AMD').info
        embed = discord.Embed(
            title='NO ENCONTRADO',
            description='TICKER NO ENCONTRADO',
            color=0x0000FF
        )

    embed.add_field(name='Promedio de 200 Dias', value=temp['twoHundredDayAverage'], inline=True)
    embed.add_field(name='Promedio de 50 Dias', value=temp['fiftyDayAverage'], inline=True)
    embed.add_field(name='52 Semanas Maximo', value=temp['fiftyTwoWeekHigh'], inline=True)
    embed.add_field(name='52 Semanas Minimo', value=temp['fiftyTwoWeekLow'], inline=True)
    embed.add_field(name='Cierre Anterior', value=temp['previousClose'], inline=True)
    embed.add_field(name='-----------------------------------', value='-', inline=False)
    embed.add_field(name='Precio de apertura', value=temp['regularMarketOpen'], inline=True)
    embed.add_field(name='Precio de cierre anterior', value=temp['regularMarketPreviousClose'], inline=True)
    embed.add_field(name='Mayor Precio anterior', value=temp['regularMarketDayHigh'], inline=True)
    embed.add_field(name='Menor Precio Anterior', value=temp['regularMarketDayLow'], inline=True)
    embed.add_field(name='Volumen', value=temp['regularMarketVolume'], inline=True)
    embed.add_field(name='Minimo del Dia (precio de hoy)', value=temp['dayLow'], inline=True)
    return embed

#------------------------------------------perdedores top-------------------------------------------------------------------------
@client.command()
async def perdedores(ctx):
    await ctx.send("espera.. OwO")
    temp = si.get_day_losers().head(10).drop(["Market Cap", "Volume", "Avg Vol (3 month)"], axis=1)
    await ctx.send(embed=crearEmbed(ctx,
               temp,
               'Perdedores',
               'Lista de top 10 perdedores',
               'https://pbs.twimg.com/media/ES9L6NIXQAAFlnO.jpg',
               0xFF0000))

#------------------------------------------GANADORES top-------------------------------------------------------------------------
@client.command()
async def ganadores(ctx):
    await ctx.send("espera.. OwO")
    temp = si.get_day_gainers().head(10).drop(["Market Cap", "Volume", "Avg Vol (3 month)"], axis=1)
    await ctx.send(embed=crearEmbed(ctx,
                                    temp,
                                    'Ganadores',
                                    'Lista de top 10 Ganadores',
                                    'https://wompampsupport.azureedge.net/fetchimage?siteId=7575&v=2&jpgQuality=100&width=700&url=https%3A%2F%2Fi.kym-cdn.com%2Fentries%2Ficons%2Ffacebook%2F000%2F029%2F959%2FScreen_Shot_2019-06-05_at_1.26.32_PM.jpg',
                                    0x00FF00))

#----------------------------------------------INFO---------------------------------------------------------------------
@client.command()
async def info(ctx,ticker):
    await ctx.send("espera.. OwO")
    # try:
    await ctx.send(embed=crearEmbedInfo(ctx,ticker,1))
    # except:
    #     await ctx.send("Ticker no encontrado >w<")

#----------------------------------------------INFOCOMPLETA---------------------------------------------------------------------
@client.command()
async def informacion(ctx,ticker):
    await ctx.send("espera.. OwO")
    try:
        await ctx.send(embed=crearEmbedInfo(ctx,ticker,0))
    except:
        await ctx.send("Ticker no encontrado >w<")
#------------------------------------------PRECIO DE ACCION-------------------------------------------------------------------------
@client.command()
async def accion(ctx, stock):
    await ctx.send("espera.. OwO")
    try:
        temp=stock+' esta en = '+ str(si.get_live_price(stock))+' USD'
        await ctx.send(temp)
    except:
        await ctx.send("Ticker no encontrado >w<")


#------------------------------------------OTROS-------------------------------------------------------------------------
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
    print('CORRIENDO V2')
    await client.change_presence(status=discord.Status.online, activity=discord.Game(os.environ.get("BOT_STATUS")))
client.run(os.environ.get("BOT_TOKEN_UWU"))
