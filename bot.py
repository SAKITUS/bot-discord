import discord
 
# La variable intenta almacenar los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios
client = discord.Client(intents=intents)
 
@client.event
async def on_ready():
    print(f'Hemos iniciado sesión como {client.user}')
 
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send("Hi!")
    elif message.content.startswith('$bye'):
        await message.channel.send("\U0001f642")
    elif message.content.startswith('how are you?'):
        await message.channel.send('good, and you?')
    elif message.content.startswith('queres cafe?'):
        await message.channel.send('si')
        await message.channel.send('y vos?')
    elif message.content.startswith('hiciste la tarea?'):
        await message.channel.send('sis, vos la hiciste?')
    elif message.content.startswith('me olvide, me la pasas?'):
        await message.channel.send('jajaj no jodete')
    elif message.content.startswith('jugas al formula 1?'):
        await message.channel.send('\U0001F923')
        await message.channel.send('si, me gusta el f1 2012')
    elif message.content.startswith('este año alonso gana la 33?'):
        await message.channel.send('si no es este año sera el proximo')


    else:
        await message.channel.send(message.content)
 
client.run("escribe tu token aqui")
