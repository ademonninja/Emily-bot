# Header bullshit
import hikari
import lightbulb
import dotenv
import os
import asyncio
from dotenv import load_dotenv

load_dotenv()

# Keeps my code sanitized for people looking at it to keep my token secret.
KEY = os.getenv('DISCORD_TOKEN')

bot = lightbulb.BotApp(token=KEY, prefix='$')

@bot.command
@lightbulb.command("ping", "checks that the bot is alive.")
@lightbulb.implements(lightbulb.SlashCommand)
async def ping(ctx: lightbulb.Context) -> None:
    await ctx.respond("Pong.")

bot.run()
