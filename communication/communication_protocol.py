from typing import Protocol, Any

class CommClientProtocol(Protocol):
    async def send(self, message: Any):
        ...

class CommunicationProtocol(Protocol):
    async def send_message(self, client: CommClientProtocol, message: str):
        ...

    async def start(self):
        ...