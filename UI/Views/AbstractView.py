from abc import ABC, abstractmethod

class AbstractView(ABC):
    @abstractmethod
    async def update(self) -> None:
        pass

    def set_message(self, message):
        pass
    
    @abstractmethod
    def stop_view(self) -> None:
        pass