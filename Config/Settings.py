import os
import logging
from logging.config import dictConfig
from dotenv import load_dotenv
from Config.Singleton import Singleton
from Folder import Folder

load_dotenv()

DISCORD_API_SECRET = os.getenv("DISCORD_API_TOKEN")

LOGGING_CONFIG = {
    "version": 1,
    "disabled_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "%(levelname)-10s - %(asctime)s - %(module)-15s : %(message)s"
        },
        "standard": {
            "format": "%(levelname)-10s - %(name)-15s : %(message)s"
        }
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "standard"
        },
        "console2": {
            "level": "WARNING",
            "class": "logging.StreamHandler",
            "formatter": "standard"
        },
        "file": {
            "level": "INFO",
            "class": "logging.FileHandler",
            "filename": "Logs/infos.log",
            "mode": "w",
            "formatter": "verbose"
        }
    },
    "loggers": {
        "bot": {
            "handlers": ['console'],
            "level": "INFO",
            "propagate": False
        },
        "discord": {
            "handlers": ['console2', 'file'],
            "level": "INFO",
            "propagate": False
        }
    }
}
dictConfig(LOGGING_CONFIG)

class BConfigs(Singleton):
    def __init__(self) -> None:
        if not super().is_created:
            self.BOT_TOKEN = os.getenv('BOT_TOKEN')
            if self.BOT_TOKEN is None:
                raise ValueError('No TOKEN was given!')

            self.BOT_PREFIX = os.getenv('BOT_PREFIX')
            if self.BOT_PREFIX == 'Prefix_For_BeatBudy':
                self.BOT_PREFIX = '!'

            self.SPOTIFY_ID = os.getenv('SPOTIFY_ID')
            self.SPOTIFY_SECRET_KEY = os.getenv('SPOTIFY_SECRET_KEY')
            
            if self.SPOTIFY_ID == "Your_Account_Spotify_ID":
                self.SPOTIFY_ID = None
            
            if self.SPOTIFY_SECRET_KEY == "Your_Own_SPOTIFY_SECRET_KEY":
                self.SPOTIFY_SECRET_KEY = None
            
            if self.SPOTIFY_ID is None or self.SPOTIFY_SECRET_KEY is None:
                print('Spotify not enabled!')
            
            # Determines whether the bot should automatically disconnect when the server is empty.
            # If the environment variable is not set, defaults to 'True'.
            self.AUTO_DISCONNECT_WHEN_ALONE = os.getenv('SHOULD_AUTO_DISCONNECT_WHEN_ALONE', 'True')

            self.SONG_PLAYBACK_IN_SEPARATE_PROCESS = os.getenv('SONG_PLAYBACK_IN_SEPARATE_PROCESS', 'True')
            
            # Determines the maximum number of songs to download simultaneously. 
            # Increasing this number speeds up song availability but slows down other Bot commands, such as playback quality adjustments.
            # If the environment variable is not set, defaults to 5.
            self.MAX_DOWNLOAD_SONGS_AT_A_TIME = int(os.getenv('MAX_DOWNLOAD_SONGS_AT_A_TIME', 5))

            self.CLEANER_MESSAGES_QUANT = int(os.getenv('CLEANER_MESSAGES_QUANT', 5))
            self.ACQUIRE_LOCK_TIMEOUT = int(os.getenv('ACQUIRE_LOCK_TIMEOUT', 10))
            self.QUEUE_VIEW_TIMEOUT = int(os.getenv('QUEUE_VIEW_TIMEOUT', 120))

            self.COMMANDS_FOLDER_NAME = os.getenv('COMMANDS_FOLDER_NAME', 'DiscordCogs')
            self.COMMANDS_PATH = f'{Folder().root_folder}{self.COMMANDS_FOLDER_NAME}'
            self.VC_TIMEOUT = int(os.getenv('VC_TIMEOUT', 300))

            #TODO: Modify this part of the code
            self.CHANCE_SHOW_PROJECT = int(os.getenv('CHANCE_SHOW_PROJECT', 15))
            self.PROJECT_URL = os.getenv('PROJECT_URL', 'https://github.com/RafaelSolVargas/Vulkan')
            self.SUPPORTING_ICON = os.getenv('SUPPORTING_ICON', 'https://i.pinimg.com/originals/d6/05/b4/d605b4f8c5d1c6ae20dc353ef9f091bd.png')

            self.MAX_PLAYLIST_LENGTH = int(os.getenv('MAX_PLAYLIST_LENGTH', 50))
            self.MAX_PLAYLIST_FORCED_LENGTH = int(os.getenv('MAX_PLAYLIST_FORCED_LENGTH', 5))
            self.MAX_SONGS_IN_PAGE = int(os.getenv('MAX_SONGS_IN_PAGE', 10))
            self.MAX_PRELOAD_SONGS = int(os.getenv('MAX_PRELOAD_SONGS', 15))
            self.MAX_SONGS_HISTORY = int(os.getenv('MAX_SONGS_HISTORY', 15))

            self.INVITE_MESSAGE = os.getenv('INVITE_MESSAGE', """To invite BeatBuddy to your own server, click [here]({}). 
            Or use this direct URL: {}""")

            self.MY_ERROR_BAD_COMMAND = os.getenv('MY_ERROR_BAD_COMMAND', 'This string serves to verify if some error was raised by myself on purpose')
            self.INVITE_URL = os.getenv('INVITE_URL', 'https://discordapp.com/oauth2/authorize?client_id={}&scope=bot')

    def getPlayerManager(self):
        return self.__manager
    
    def setPlayersManager(self, new_manager):
        self.__manager = new_manager
            