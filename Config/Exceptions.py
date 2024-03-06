from Config.Messages import Messages

class BeatBuddyError(Exception):
    def __init__(self, message='',title='', *args: object) -> None:
        self.__message = message
        self.__title = title
        super().__init__(*args)

    @property
    def message(self) -> str:
        return self.__message
    
    @property
    def title(self) -> str:
        return self.__title

class ImpossibleMove(BeatBuddyError):
    def __init__(self, message='', title='', *args: object) -> None:
        message = Messages()
        if title == '':
            title = message.IMPOSSIBLE_MOVE
        super().__init__(message, title, *args)

class MusicUnavailable(BeatBuddyError):
    def __init__(self, message='', title='', *args: object) -> None:
        super().__init__(message, title, *args)

class YoutubeError(BeatBuddyError):
    def __init__(self, message='', title='', *args: object) -> None:
        super().__init__(message, title, *args)

class BadCommandUsage(BeatBuddyError):
    def __init__(self, message='', title='', *args: object) -> None:
        super().__init__(message, title, *args)

class DownloadingError(BeatBuddyError):
    def __init__(self, message='', title='', *args: object) -> None:
        super().__init__(message, title, *args)

class SpotifyError(BeatBuddyError):
    def __init__(self, message='', title='', *args: object) -> None:
        super().__init__(message, title, *args)

class UnknownError(BeatBuddyError):
    def __init__(self, message='', title='', *args: object) -> None:
        super().__init__(message, title, *args)

class InvalidInput(BeatBuddyError):
    def __init__(self, message='', title='', *args: object) -> None:
        super().__init__(message, title, *args)

class WrongLength(BeatBuddyError):
    def __init__(self, message='', title='', *args: object) -> None:
        super().__init__(message, title, *args)

class ErrorMoving(BeatBuddyError):
    def __init__(self, message='', title='', *args: object) -> None:
        super().__init__(message, title, *args)

class ErrorRemoving(BeatBuddyError):
    def __init__(self, message='', title='', *args: object) -> None:
        super().__init__(message, title, *args)

class InvalidIndex(BeatBuddyError):
    def __init__(self, message='', title='', *args: object) -> None:
        super().__init__(message, title, *args)

class NumberRequired(BeatBuddyError):
    def __init__(self, message='', title='', *args: object) -> None:
        super().__init__(message, title, *args)