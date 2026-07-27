class Metrics:
    def __init__(self):
        self.metrics = {}

    def add_metric(self, name: str, value: float):
        self.metrics[name] = value

    def get_metric(self, name: str) -> float:
        return self.metrics.get(name, 0.0)