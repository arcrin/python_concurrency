from abc import ABC, abstractmethod

class ExecutorEngineInterface(ABC):
    @abstractmethod
    async def run_script(self, script):
        pass

    @abstractmethod
    async def stop_script(self):
        pass