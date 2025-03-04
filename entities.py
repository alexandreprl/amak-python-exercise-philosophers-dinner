from amak import Agent


class Fork:
    def __init__(self):
        self.available = True
        self.holder = None

    def take(self, agent):
        self.available = False
        self.holder = agent

    def put(self):
        self.available = True
        self.holder = None

    def is_taken_by(self, agent):
        return self.holder == agent


class PhilosopherAgent(Agent):
    def __init__(self, id, amas, left_fork, right_fork):
        super().__init__(amas)
        self.id = id
        self.ate_pasta = 0
        self.left_fork = left_fork
        self.right_fork = right_fork
        self.left_neighbor = None
        self.right_neighbor = None

    def on_perceive(self):
        pass

    def on_decide(self):
        pass

    def on_act(self):
        pass
