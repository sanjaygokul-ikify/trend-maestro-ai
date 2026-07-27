import unittest
from packages.core.engine import Engine, Agent, Task
from packages.services.orchestrator import OrchestratorService

class TestPipeline(unittest.TestCase):
    def test_pipeline(self):
        agents = [Agent('agent1'), Agent('agent2')]
        tasks = [Task('task1'), Task('task2')]
        engine = Engine(agents, tasks)
        service = OrchestratorService(agents, tasks)

        service.start()
        engine.update_task_status(tasks[0], 'running')
        self.assertEqual(tasks[0].status, 'running')

        engine.stop()
        service.stop()

if __name__ == '__main__':
    unittest.main()