from Config.Singleton import Singleton

class Colors(Singleton):
    def __init__(self) -> None:
        if not super().is_created:
            self.__red = 0xF95738
            self.__green = 0x1F8B4C
            self.__grey = 0xE4DFDA
            self.__blue = 0x5762D5
            self.__black = 0x23272A

    @property
    def red(self) -> str:
        return self.__red

    @property
    def green(self) -> str:
        return self.__green

    @property
    def grey(self) -> str:
        return self.__grey

    @property
    def blue(self) -> str:
        return self.__blue

    @property
    def black(self) -> str:
        return self.__black