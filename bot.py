import discord
import responses

async def sendMessage(message,user_message,isPrivate):
    try:
        response = responses.handleResponse(user_message)
        await message.author.send(response) if isPrivate else await message.channel.send(response)
    except Exception as e:
        print(e)


def runDiscordBot():
    TOKEN = 'MTE0OTc0OTg3NTYyMjI5MzUzNQ.GLhwyy.s8cgayzuCA-LNh4s6z2g-kLNgVvYKTOOuUXemw'
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is now running')

    @client.event
    async def on_message(message):
        if message.author != client.user:  # Check if the message author is not the bot
            username = str(message.author)
            user_message = str(message.content)
            channel = str(message.channel)
            print(f"{username} said: '{user_message}' ({channel})")
            await sendMessage(message, user_message, isPrivate=False)

    client.run(TOKEN)