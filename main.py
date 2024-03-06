import Config.Settings as settings
import discord
from discord.ext import commands

logger = settings.logging.getLogger("bot")

# def run():
#     # Define your intents
#     intents = discord.Intents.default()
#     intents.messages = True

#     # Create a bot instance
#     bot = commands.Bot(command_prefix='!', intents=intents)
#     bot.run(settings.DISCORD_API_SECRET, root_logger=True)

#     @bot.event
#     async def on_ready():
#         logger.info(f"User: {bot.user} (ID: {bot.user.id})")


if __name__ == '__main__':
    # run()
    pass
