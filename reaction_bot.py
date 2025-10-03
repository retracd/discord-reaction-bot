import discord
import os

### CONFIGURATION ###
TARGET_CHANNEL_NAME = "newer-general" # Change this to your target channel name
REACTION_EMOJI = "💀" # Change this to your target emoticon reaction

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

class ReactionBot(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user.name} (ID: {self.user.id})')
        print('Bot is ready to add reactions!')
        print('------')

    async def on_message(self, message):
        if message.author.id == self.user.id:
            return
        if message.channel.name == TARGET_CHANNEL_NAME:
            try:
                await message.add_reaction(REACTION_EMOJI)
                print(f"Added reaction to message ID {message.id} in channel {TARGET_CHANNEL_NAME}")
            except discord.Forbidden:
                print(f"Failed to add reaction to message ID {message.id}: Missing Permissions")
            except discord.HTTPException as e:
                print(f"Failed to add reaction to message ID {message.id}: {e}")

def main():
    intents = discord.Intents.default()
    intents.messages = True
    intents.guilds = True

    client = ReactionBot(intents=intents)
    client.run(BOT_TOKEN)

if __name__ == '__main__':
    main()
