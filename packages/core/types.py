from typing import List

class Agent:
    def __init__(self, id: str):
        self.id = id
        self.tasks = []
        self.status = "idle"


class Task:
    def __init__(self, id: str):
        self.id = id
        self.status = "pending"
