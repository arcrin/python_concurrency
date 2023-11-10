from abc import ABC, abstractmethod
from typing import Coroutine, Any

class ExecutorEngineInterface(ABC):
    @abstractmethod
    async def run_script(self) -> Coroutine[Any, Any, str]:
        pass

    @abstractmethod
    async def stop_script(self):
        pass