import argparse
from packages.services.orchestrator import OrchestratorService
from packages.core.engine import Engine, Agent, Task


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--start', action='store_true')
    parser.add_argument('--stop', action='store_true')
    args = parser.parse_args()

    agents = [Agent('agent1'), Agent('agent2')]
    tasks = [Task('task1'), Task('task2')]
    service = OrchestratorService(agents, tasks)

    if args.start:
        service.start()
    elif args.stop:
        service.stop()

if __name__ == '__main__':
    main()