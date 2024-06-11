# Header bullshit
import discord
import os
from dotenv import load_dotenv

load_dotenv()

# Keeps my code sanitized for people looking at it to keep my token secret.
KEY = os.getenv('DISCORD_TOKEN')
