import discord
from discord.ext import commands
import openai
import configparser
#PLEASE EDIT THE CONFIG.INI FILE.

config = configparser.ConfigParser()
config.read('config.ini') #Config.ini (Please specify the file path)

# config.ini (Discord Token)
discord_token = config.get('DEFAULT', 'discord_token')

# config.ini (Open AI Api key)
openai.api_key = config.get('DEFAULT', 'openai_api_key')

prefix = "!" # !commands

intents = discord.Intents.default()
intents.typing = True
intents.presences = True
intents.message_content = True

bot = commands.Bot(command_prefix=prefix, intents=intents)

@bot.event
async def on_ready():
    print(f"Bot olarak giriş yapıldı: {bot.user.name}")

# "ask" commands
@bot.command()
async def ask(ctx, *, question=None): #!ask command
    if question is None:
        await ctx.send("!ask <soru> şeklinde sorunuzu belirtin.")
        return

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=question,
        max_tokens=1000,
        temperature=0.6,
        n=1,
        stop=None,
    )
    answer = response.choices[0].text.strip()

    await ctx.send(answer)

bot.run(discord_token)
