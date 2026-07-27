import logging
from typing import List, Dict
from .types import Agent, Task
from .exceptions import EngineException


class Engine:
    def __init__(self, agents: List[Agent], tasks: List[Task]):
        self.agents = agents
        self.tasks = tasks
        self.logger = logging.getLogger(__name__)

    def register_agent(self, agent: Agent):
        self.agents.append(agent)
        self.logger.info(f"Agent {agent.id} registered")

    def assign_task(self, task: Task, agent: Agent):
        if agent in self.agents:
            agent.tasks.append(task)
            self.tasks.append(task)
            self.logger.info(f"Task {task.id} assigned to agent {agent.id}")
        else:
            self.logger.error(f"Agent {agent.id} not found")
            raise EngineException(f"Agent {agent.id} not found")

    def update_task_status(self, task: Task, status: str):
        for agent in self.agents:
            if task in agent.tasks:
                task.status = status
                self.logger.info(f"Task {task.id} status updated to {status}")
                return
        self.logger.error(f"Task {task.id} not found")
        raise EngineException(f"Task {task.id} not found")

    def get_agent_status(self, agent: Agent):
        return agent.status

    def get_task_status(self, task: Task):
        return task.status

    def start(self):
        self.logger.info("Engine started")
        for agent in self.agents:
            agent.start()

    def stop(self):
        self.logger.info("Engine stopped")
        for agent in self.agents:
            agent.stop()

    def get_agents(self) -> List[Agent]:
        return self.agents

    def get_tasks(self) -> List[Task]:
        return self.tasks


class Agent:
    def __init__(self, id: str):
        self.id = id
        self.tasks = []
        self.status = "idle"
        self.logger = logging.getLogger(__name__)

    def start(self):
        self.logger.info(f"Agent {self.id} started")
        self.status = "running"

    def stop(self):
        self.logger.info(f"Agent {self.id} stopped")
        self.status = "idle"


class Task:
    def __init__(self, id: str):
        self.id = id
        self.status = "pending"
        self.logger = logging.getLogger(__name__)


logging.basicConfig(level=logging.INFO)