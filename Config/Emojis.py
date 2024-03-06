from Config.Singleton import Singleton

class BEmojis(Singleton):
    def __init__(self) -> None:
        if not super().is_created:
            self.SKIP = "⏩"
            self.BACK = "⏪"
            self.PAUSE = "⏸️"
            self.PLAY = "▶️"
            self.STOP = "⏹️"
            self.LOOP_ONE = "🔂"
            self.LOOP_OFF = "➡️"
            self.LOOP_ALL = "🔁"
            self.SHUFFLE = "🔀"
            self.QUEUE = "📜"
            self.MUSIC = "♫"
            self.ERROR = "❗"
            self.DOWNLOADING = "📥"
            self.SUCCESS = "✅"