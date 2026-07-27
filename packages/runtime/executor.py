import logging
from typing import List
from ..core.engine import Engine
from ..core.types import Agent, Task


class Executor:
    def __init__(self, engine: Engine):
        self.engine = engine
        self.logger = logging.getLogger(__name__)

    def execute(self):
        self.logger.info("Executor started")
        self.engine.start()
        while True:
            for agent in self.engine.agents:
                if agent.status == "running":
                    for task in agent.tasks:
                        if task.status == "pending":
                            task.status = "running"
                            self.logger.info(f"Task {task.id} started")
                            # task execution logic here
                            task.status = "completed"
                            self.logger.info(f"Task {task.id} completed")
            self.engine.stop()
            self.logger.info("Executor stopped")
            break

    def stop(self):
        self.engine.stop()
        self.logger.info("Executor stopped")


logging.basicConfig(level=logging.INFO)