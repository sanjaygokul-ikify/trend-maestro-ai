import unittest
from packages.core.engine import Engine, Agent, Task
from packages.services.orchestrator import OrchestratorService

class TestRuntime(unittest.TestCase):
    def test_orchestrator(self):
        agents = [Agent('agent1'), Agent('agent2')]
        tasks = [Task('task1'), Task('task2')]
        service = OrchestratorService(agents, tasks)
        service.start()
        service.stop()

if __name__ == '__main__':
    unittest.main()