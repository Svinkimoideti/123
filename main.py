import discord
from bot_logic import gen_pass
# Переменная intents - хранит привилегии бота
intents = discord.Intents.default()
# Включаем привелегию на чтение сообщений
intents.message_content = True
# Создаем бота в переменной client и передаем все привелегии
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('Привет'):
        await message.channel.send("Добрый день")
    if message.content.startswith('1'):
        await message.channel.send(":heart:")
    if message.content.startswith('Пока'):
        await message.channel.send(":regional_indicator_g: :regional_indicator_o: :o2: :regional_indicator_d:  :regional_indicator_b: :regional_indicator_y: :regional_indicator_e: !")
    if message.content.startswith('Пароль генерация'):
        await message.channel.send(gen_pass(10))
    else:
        await message.channel.send(message.content)

client.run("")
