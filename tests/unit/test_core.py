import unittest
from packages.core.engine import Engine, Agent, Task

class TestCore(unittest.TestCase):
    def test_agent(self):
        agent = Agent('agent1')
        self.assertEqual(agent.id, 'agent1')
        self.assertEqual(agent.status, 'idle')

    def test_task(self):
        task = Task('task1')
        self.assertEqual(task.id, 'task1')
        self.assertEqual(task.status, 'pending')

    def test_engine(self):
        agents = [Agent('agent1'), Agent('agent2')]
        tasks = [Task('task1'), Task('task2')]
        engine = Engine(agents, tasks)
        self.assertEqual(len(engine.agents), 2)
        self.assertEqual(len(engine.tasks), 2)

if __name__ == '__main__':
    unittest.main()