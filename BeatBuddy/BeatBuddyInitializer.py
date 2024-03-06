
import string
from random import choices
from os import listdir
from discord import Intents
from discord.ext.commands import Bot
from Config.Settings import BConfigs
from Config.Exceptions import BeatBuddyError
from BeatBuddy import BeatBuddyBot

class BeatBuddyInitializer:
    def __init__(self, will_listen: bool) -> None:
        self.__config = BConfigs()
        self.__intents = Intents.default()
        self.__intents.message_content = True
        self.__intents.members = True
        self.__bot = self.__create_bot(will_listen)
        self.__add_cogs(self.__bot)
    
    def getBot(self) -> BeatBuddyBot:
        return self.__bot

    def __create_bot(self, will_listen: bool) -> BeatBuddyBot:
        if will_listen:
            prefix = self.__config.BOT_PREFIX
            bot = BeatBuddyBot(listing_slash=True,
                               command_prefix=prefix,
                               pm_help=True,
                               case_insensitive=True,
                               intents=self.__intents)
        else:
            prefix = ''.join(choices(string.ascii_uppercase + string.digits,k=4))
            bot = BeatBuddyBot(listing_slash=True,
                               command_prefix=prefix,
                               pm_help=True,
                               case_insensitive=True,
                               intents=self.__intents)
        return bot
    
    def __add_cogs(self, bot:Bot) -> None:
        try:
            cogs_status = []
            for file_name in listdir(self.__config.COMMANDS_PATH):
                if file_name.endswith('.py'):
                    cog_path = f'{self.__config.COMMANDS_FOLDER_NAME}.{file_name[:-3]}'
                    cogs_status.append(bot.load_extension(cog_path, store=True))

            if len(bot.cogs.keys()) != self.__get_total_cogs():
                print(cogs_status)
                raise BeatBuddyError(message='Failed to load some Cog')
        except BeatBuddyError as e:
            print('ERROR LOADING BOT!')
            print(e)

    def __get_total_cogs(self) -> int:
        qty = 0
        for filename in listdir(self.__config.COMMANDS_PATH):
            if filename.endswith('.py'):
                qty += 1
        return qty

