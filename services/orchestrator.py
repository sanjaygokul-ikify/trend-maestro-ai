from packages.core.engine import Engine
from typing import List

class OrchestratorService:
    def __init__(self, agents: List, tasks: List):
        self.engine = Engine(agents, tasks)

    def start(self):
        self.engine.start()

    def stop(self):
        self.engine.stop()