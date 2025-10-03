import discord
import os

#
# CONFIGURATION
TARGET_CHANNEL_NAME = "newer-general"
REACTION_EMOJI = "💀"

# I reccomend to store your bot token in an environment variable for security reasons
#  You can do this by creating a .env file and adding the line
#  DISCORD_TOKEN="your_token_here"
# If you don't want to create a .env file, you can replace os.getenv("DISCORD_TOKEN")
#  below with your actual token string, but be aware that this is less secure.
try:
    from dotenv import load_dotenv
    load_dotenv()
    BOT_TOKEN = os.getenv("DISCORD_TOKEN")
    if BOT_TOKEN is None:
        raise ImportError
except ImportError:
    print("WARNING: dotenv library not found or DISCORD_TOKEN not set.")
    print("Please create a .env with DISCORD_TOKEN='' set or set it as an environment variable.")

