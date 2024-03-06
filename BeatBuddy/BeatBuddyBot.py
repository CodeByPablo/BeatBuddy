from asyncio import AbstractEventLoop
from discord import Guild, Status, Game, Message
from discord.ext.commands import Bot, Context
from discord.ext.commands.errors import MissingRequiredArgument, CommandNotFound
from Config.Settings import BConfigs
from Config.Messages import Messages
from Config.Embeds import BEmbeds

class BeatBuddyBot(Bot):
    def __init__(self, listing_slash: bool = False, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__listing_slash = listing_slash
        self.__config = BConfigs()
        self.__messages = Messages()
        self.__embeds = BEmbeds()
        self.remove_command('help')
    
    @property
    def listing_slash(self) -> bool:
        return self.__listing_slash
    
    def start_bot(self) -> None:
        if self.__config.BOT_TOKEN == '':
            print('Debugging Note: missing BOT_TOKEN')
            exit()
        
        super().run(self.__config.BOT_TOKEN, reconnect=True)
    
    async def start_bot_coroutine(self, loop: AbstractEventLoop) -> None:
        """Start a bot coroutine without waiting for server connection"""
        task = loop.create_task(self.__login())
        await task
        loop.create_task(self.__connect())

    async def __login(self):
        await self.login(token=self.__config.BOT_TOKEN)

    async def __connect(self):
        await self.connect(reconnect=True)

    async def on_ready(self):
        if self.__listing_slash:
            print(self.__messages.STARTUP_MESSAGE)
        await self.change_presence(status=Status.online, activity=Game(name=f'BeatBuddy | {self.__config.BOT_PREFIX}help'))
        if self.__listing_slash:
            print(self.__messages.STARTUP_COMPLETE_MESSAGE)
    
    async def on_command_error(self, ctx, error):
        if isinstance(error, MissingRequiredArgument):
            embed = self.__embeds.MISSING_ARGUMENTS()
            await ctx.send(embed=embed)
        if isinstance(error, CommandNotFound):
            embed = self.__embeds.COMMAND_NOT_FOUND()
            await ctx.send(embed=embed)
        else:
            print(f'Debugging Note: Command Error - {error}')
            embed = self.__embeds.UNKNOWN_ERROR()
            await ctx.send(embed=embed)

    async def process_commands(self, message: Message) -> None:
        if message.author.bot:
            return
        
        ctx = await self.get_context(message, cls=Context)

        if ctx.valid and not message.guild:
            return
        
        await self.invoke(ctx)

class Context(Context):
    bot: BeatBuddyBot
    guild: Guild




