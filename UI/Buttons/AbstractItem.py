from abc import ABC, abstractmethod
from discord.ui import Item, View

class AbstractItem(ABC):
    @abstractmethod
    def self_view(self, view: View):
        pass

    @abstractmethod
    def get_view(self) -> View:
        pass