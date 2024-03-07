from discord import Embed
from discord.ext.commands import Cog, command
from Config.Settings import BConfigs
from Config.Helper import Helper
from Config.Colors import Colors
from BeatBuddy.BeatBuddyBot import BeatBuddyBot

helper = Helper()

class ControlCog(Cog):
    def __init__(self, bot: BeatBuddyBot):
        self.__bot = bot
        self.__config = BConfigs()
        self.__colors = Colors()
        self.__commands = {
            'MUSIC': ['resume', 'pause', 'loop', 'stop',
                      'skip', 'play', 'queue', 'clear',
                      'np', 'shuffle', 'move', 'remove',
                      'reset', 'prev', 'history', 'volume'],
            'RANDOM': ['choose', 'flip-a-coin', 'random']
        }

    @command(name='help', help=helper.HELP_HELP, description= helper.HELP_HELP_LONG, aliases=['h', 'H'])
    async def help_msg(self, ctx, command_help=''):
        if command_help != '':
            for command in self.__bot.commands:
                if command.name == command_help:
                    txt = command.description if command.description else command.help
                    embed_help = Embed(
                        title=f'**Description of {command_help}** help',
                        description=txt,
                        color = self.__colors.blue
                    )
                    await ctx.send(embed=embed_help)
            embed_help = Embed(
                title='Help',
                description=f"Command {command_help} doesn't exist, type {self.__config.BOT_PREFIX}help to display commands!",
                color = self.__colors.black
            )
            await ctx.send(embed=embed_help)
        else:
            help_txt = ''
            help_music = '🎧 `MUSIC`\n'
            help_random = '🎲 `RANDOM`\n'
            help_help = '👾 `HELP`\n'

            for command in self.__bot.commands:
                if command.name in self.__commands['MUSIC']:
                    help_music += f'**{command}** - {command.help}\n'
                elif command.name in self.__commands['RANDOM']:
                    help_random += f'**{command}** - {command.help}\n'
                else:
                    help_help = f'**{command}** - {command.help}\n'
            help_txt = f'\n{help_music}\n{help_random}\n{help_help}'
            help_txt += f'\n\nType {self.__config.BOT_PREFIX}help "command" for more information about the command chosen!'
            embed_help = Embed(
                title=f'**Available commands for {self.__bot.user.name}**',
                description=help_txt,
                color = self.__colors.blue
            )
            if self.__bot.user.avatar != None:
                embed_help.set_thumbnail(url=self.__bot.user.avatar)
            await ctx.send(embed=embed_help)
    
    @command(name='invite', help=helper.HELP_INVITE, description=helper.HELP_INVITE_LONG, aliases= ['inv'])
    async def invite_bot(self, ctx):
        invite_url = self.__config.INVITE_URL.format(self.__bot.user.id)
        txt = self.__config.INVITE_MESSAGE.format(invite_url, invite_url)
        embed = Embed(
            title="Invite BeatBuddy",
            description=txt,
            color=self.__colors.BLUE
        )
        await ctx.send(embed=embed)