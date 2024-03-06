from random import random
from datetime import timedelta
from discord import Embed
from Config.Settings import BConfigs
from Config.Exceptions import BeatBuddyError
from Config.Messages import Messages
from Config.Colors import Colors

class BEmbeds:
    def __init__(self) -> None:
        self.__config = BConfigs()
        self.__messages = Messages()
        self.__colors = Colors()
    
    def __will_show_project(self) -> bool:
        return (random() * 100 < self.__config.CHANCE_SHOW_PROJECT)
    
    def __add_footer_content(self, embed: Embed) -> Embed:
        footerText = f'\u200b Please support this project by leaving a star: {self.__config.PROJECT_URL}'
        return embed.set_footer(text=footerText, icon_url=self.__config.SUPPORTING_ICON)

    def ONE_SONG_LOOPING(self, info: dict) -> Embed:
        title = self.__messages.ONE_SONG_LOOPING
        return self.SONG_INFO(info, title)

    def EMPTY_QUEUE(self) -> Embed:
        title = self.__messages.SONG_PLAYER
        text = self.__messages.EMPTY_QUEUE
        embed = Embed(
            title=title,
            description=text,
            color=self.__colors.BLUE
        )
        return embed

    def MISSING_ARGUMENTS(self) -> Embed:
        embed = Embed(
            title=self.__messages.ERROR_TITLE,
            description=self.__messages.ERROR_MISSING_ARGUMENTS,
            color=self.__colors.BLACK
        )
        return embed

    def INVALID_INDEX(self) -> Embed:
        embed = Embed(
            title=self.__messages.BAD_COMMAND_TITLE,
            description=self.__messages.INVALID_INDEX,
            color=self.__colors.BLACK
        )
        return embed

    def SONG_ADDED_TWO(self, info: dict, pos: int) -> Embed:
        embed = self.SONG_INFO(info, self.__messages.SONG_ADDED_TWO, pos)
        return embed

    def INVALID_INPUT(self) -> Embed:
        embed = Embed(
            title=self.__messages.ERROR_TITLE,
            description=self.__messages.INVALID_INPUT,
            color=self.__colors.BLACK)
        return embed

    def UNAVAILABLE_VIDEO(self) -> Embed:
        embed = Embed(
            title=self.__messages.ERROR_TITLE,
            description=self.__messages.VIDEO_UNAVAILABLE,
            color=self.__colors.BLACK)
        return embed

    def DOWNLOADING_ERROR(self) -> Embed:
        embed = Embed(
            title=self.__messages.ERROR_TITLE,
            description=self.__messages.DOWNLOADING_ERROR,
            color=self.__colors.BLACK)
        return embed

    def SONG_ADDED(self, title: str) -> Embed:
        embed = Embed(
            title=self.__messages.SONG_PLAYER,
            description=self.__messages.SONG_ADDED.format(title),
            color=self.__colors.BLUE)
        return embed

    def SONGS_ADDED(self, quant: int) -> Embed:
        embed = Embed(
            title=self.__messages.SONG_PLAYER,
            description=self.__messages.SONGS_ADDED.format(quant),
            color=self.__colors.BLUE)
        return embed

    def SONG_INFO(self, info: dict, title: str, position='Playing Now') -> Embed:
        embed_bb = Embed(
            title=title,
            description=f"[{info['title']}]({info['original_url']})",
            color=self.__colors.BLUE
        )

        embed_bb.add_field(name=self.__messages.SONGINFO_UPLOADER,
                          value=info['uploader'],
                          inline=False)

        embed_bb.add_field(name=self.__messages.SONGINFO_REQUESTER,
                          value=info['requester'],
                          inline=True)

        if 'thumbnail' in info.keys():
            embed_bb.set_thumbnail(url=info['thumbnail'])

        if 'duration' in info.keys():
            duration = str(timedelta(seconds=info['duration']))
            embed_bb.add_field(name=self.__messages.SONGINFO_DURATION,
                              value=f"{duration}",
                              inline=True)
        else:
            embed_bb.add_field(name=self.__messages.SONGINFO_DURATION,
                              value=self.__messages.SONGINFO_UNKNOWN_DURATION,
                              inline=True)

        embed_bb.add_field(name=self.__messages.SONGINFO_POSITION,
                          value=position,
                          inline=True)

        if self.__will_show_project():
            embed_bb = self.__add_footer_content(embed_bb)
        return embed_bb

    def SONG_MOVED(self, song_name: str, pos1: int, pos2: int) -> Embed:
        embed = Embed(
            title=self.__messages.SONG_PLAYER,
            description=self.__messages.SONG_MOVED_SUCCESSFULLY.format(song_name, pos1, pos2),
            color=self.__colors.BLUE
        )
        return embed

    def ERROR_MOVING(self) -> Embed:
        embed = Embed(
            title=self.__messages.UNKNOWN_ERROR,
            description=self.__messages.ERROR_MOVING,
            color=self.__colors.BLACK
        )
        return embed

    def ERROR_EMBED(self, description: str) -> Embed:
        embed = Embed(
            description=description,
            color=self.__colors.BLACK
        )
        return embed

    def CUSTOM_ERROR(self, error: BeatBuddyError) -> Embed:
        embed = Embed(
            title=error.title,
            description=error.message,
            color=self.__colors.BLACK
        )
        return embed

    def WRONG_LENGTH_INPUT(self) -> Embed:
        embed = Embed(
            title=self.__messages.BAD_COMMAND_TITLE,
            description=self.__messages.LENGTH_ERROR,
            color=self.__colors.BLACK
        )
        return embed

    def BAD_LOOP_USE(self) -> Embed:
        embed = Embed(
            title=self.__messages.BAD_COMMAND_TITLE,
            description=self.__messages.BAD_USE_OF_LOOP,
            color=self.__colors.BLACK
        )
        return embed

    def COMMAND_ERROR(self):
        embed = Embed(
            title=self.__messages.ERROR_TITLE,
            description=self.__messages.ERROR_MISSING_ARGUMENTS,
            color=self.__colors.BLACK
        )
        return embed

    def INVALID_ARGUMENTS(self):
        embed = Embed(
            title=self.__messages.BAD_COMMAND_TITLE,
            description=self.__messages.INVALID_ARGUMENTS,
            color=self.__colors.BLACK
        )
        return embed

    def COMMAND_NOT_FOUND(self) -> Embed:
        embed = Embed(
            title=self.__messages.COMMAND_NOT_FOUND_TITLE,
            description=self.__messages.COMMAND_NOT_FOUND,
            color=self.__colors.BLACK
        )
        return embed

    def MY_ERROR_BAD_COMMAND(self) -> Embed:
        embed = Embed(
            title=self.__messages.BAD_COMMAND_TITLE,
            description=self.__messages.BAD_COMMAND,
            color=self.__colors.BLACK
        )
        return embed

    def UNKNOWN_ERROR(self) -> Embed:
        embed = Embed(
            title=self.__messages.ERROR_TITLE,
            description=self.__messages.UNKNOWN_ERROR,
            color=self.__colors.RED
        )
        return embed

    def FAIL_DUE_TO_LOOP_ON(self) -> Embed:
        embed = Embed(
            title=self.__messages.SONG_PLAYER,
            description=self.__messages.LOOP_ON,
            color=self.__colors.BLACK
        )
        return embed

    def ERROR_SHUFFLING(self) -> Embed:
        embed = Embed(
            title=self.__messages.SONG_PLAYER,
            description=self.__messages.ERROR_SHUFFLING,
            color=self.__colors.BLACK
        )
        return embed

    def SONGS_SHUFFLED(self) -> Embed:
        embed = Embed(
            title=self.__messages.SONG_PLAYER,
            description=self.__messages.SONGS_SHUFFLED,
            color=self.__colors.BLUE
        )
        return embed

    def LOOP_ONE_ACTIVATED(self) -> Embed:
        embed = Embed(
            title=self.__messages.LOOP_ONE_ACTIVATE,
            color=self.__colors.BLUE
        )
        return embed

    def LOOP_ALL_ACTIVATED(self) -> Embed:
        embed = Embed(
            title=self.__messages.LOOP_ALL_ACTIVATE,
            color=self.__colors.BLUE
        )
        return embed

    def SONG_PROBLEMATIC(self) -> Embed:
        embed = Embed(
            title=self.__messages.ERROR_TITLE,
            description=self.__messages.DOWNLOADING_ERROR,
            color=self.__colors.BLACK)
        return embed

    def PLAYER_RESTARTED(self) -> Embed:
        embed = Embed(
            title=self.__messages.ERROR_TITLE,
            description=self.__messages.ERROR_IN_PROCESS,
            color=self.__colors.BLACK)
        return embed

    def NO_CHANNEL(self) -> Embed:
        embed = Embed(
            title=self.__messages.IMPOSSIBLE_MOVE,
            description=self.__messages.NO_CHANNEL,
            color=self.__colors.BLACK
        )
        return embed

    def ERROR_DUE_LOOP_ONE_ON(self) -> Embed:
        embed = Embed(
            title=self.__messages.BAD_COMMAND_TITLE,
            description=self.__messages.ERROR_DUE_LOOP_ONE_ON,
            color=self.__colors.BLACK
        )
        return embed

    def LOOP_DISABLE(self) -> Embed:
        embed = Embed(
            title=self.__messages.LOOP_DISABLE,
            color=self.__colors.BLUE
        )
        return embed

    def PLAYER_RESUMED(self) -> Embed:
        embed = Embed(
            title=self.__messages.SONG_RESUMED,
            color=self.__colors.BLUE
        )
        return embed

    def SKIPPING_SONG(self) -> Embed:
        embed = Embed(
            title=self.__messages.SONG_SKIPPED,
            color=self.__colors.BLUE
        )
        return embed

    def STOPPING_PLAYER(self) -> Embed:
        embed = Embed(
            title=self.__messages.STOPPING,
            color=self.__colors.BLUE
        )
        return embed

    def RETURNING_SONG(self) -> Embed:
        embed = Embed(
            title=self.__messages.RETURNING_SONG,
            color=self.__colors.BLUE
        )
        return embed

    def PLAYER_PAUSED(self) -> Embed:
        embed = Embed(
            title=self.__messages.SONG_PAUSED,
            color=self.__colors.BLUE
        )
        return embed

    def NOT_PREVIOUS_SONG(self) -> Embed:
        embed = Embed(
            title=self.__messages.SONG_PLAYER,
            description=self.__messages.NOT_PREVIOUS,
            color=self.__colors.BLUE
        )
        return embed

    def HISTORY(self, description: str) -> Embed:
        embed = Embed(
            title=self.__messages.HISTORY_TITLE,
            description=description,
            color=self.__colors.BLUE)
        return embed

    def NOT_PLAYING(self) -> Embed:
        embed = Embed(
            title=self.__messages.SONG_PLAYER,
            description=self.__messages.PLAYER_NOT_PLAYING,
            color=self.__colors.BLUE)
        return embed
    
    def VOLUME_CHANGED(self, volume: float) -> Embed:
        embed = Embed(
            title=self.__messages.SONG_PLAYER,
            description=self.__messages.VOLUME_CHANGED.format(volume),
            color=self.__colors.BLUE)
        return embed

    def QUEUE(self, title: str, description: str) -> Embed:
        embed = Embed(
            title=title,
            description=description,
            color=self.__colors.BLUE
        )

        if self.__will_show_project():
            embed = self.__add_footer_content(embed)
        return embed

    def INVITE(self, bot_id: str) -> Embed:
        link = self.__messages.INVITE_URL
        link.format(bot_id)
        text = self.__messages.INVITE_MESSAGE.format(link, link)

        embed = Embed(
            title="Invite Vulkan",
            description=text,
            color=self.__colors.BLUE
        )
        return embed

    def ERROR_NUMBER(self) -> Embed:
        embed = Embed(
            description=self.__messages.ERROR_NUMBER,
            color=self.__colors.BLACK
        )
        return embed

    def RANDOM_NUMBER(self, a: int, b: int, x: int) -> Embed:
        embed = Embed(
            title=f'Random number between [{a}, {b}]',
            description=x,
            color=self.__colors.GREEN
        )
        return embed

    def SONG_REMOVED(self, song_name: str) -> Embed:
        embed = Embed(
            description=self.__messages.SONG_REMOVED_SUCCESSFULLY.format(song_name),
            color=self.__colors.BLUE
        )
        return embed

    def PLAYLIST_RANGE_ERROR(self) -> Embed:
        embed = Embed(
            description=self.__messages.LENGTH_ERROR,
            color=self.__colors.BLACK
        )
        return embed

    def PLAYLIST_CLEAR(self) -> Embed:
        return Embed(
            description=self.__messages.PLAYLIST_CLEAR
        )

    def FAC(self, result: str) -> Embed:
        embed = Embed(
            title='Flip a Coin',
            description=f'Result: {result}',
            color=self.__colors.GREEN
        )
        return embed

    def CHOSEN_THING(self, thing: str) -> Embed:
        embed = Embed(
            title='Choose something',
            description=f'Chosen: {thing}',
            color=self.__colors.GREEN
        )
        return embed

    def BAD_CHOOSE_USE(self) -> Embed:
        embed = Embed(
            title='Choose something',
            description=f'Error: Use {self.__config.BOT_PREFIX}help choose to understand this command.',
            color=self.__colors.RED
        )
        return embed

