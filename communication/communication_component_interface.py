from abc import ABC, abstractmethod

class CommunicationComponentInterface(ABC):
    @abstractmethod
    async def send_message(self, client, message):
        pass

    @abstractmethod
    async def receive_message(self):
        pass

    @abstractmethod
    async def start(self):
        pass