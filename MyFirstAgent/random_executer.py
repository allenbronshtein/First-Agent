# Details : Allen Bronshtein ID 206228751
import random
class RandomExecutor(object):

    def __init__(self):
        self.successor = None

    def initialize(self, services):
        self.services = services

    def next_action(self):
        if self.services.goal_tracking.reached_all_goals():
            return None
        options = self.services.valid_actions.get()
        if len(options) == 0: return None
        if len(options) == 1: return options[0]
        return self.pick_from_many(options)

    def pick_from_many(self, options):
        chosen = random.choice(options)
        return chosen

from pddlsim.local_simulator import LocalSimulator
domain_path = "domain.pddl"
problem_path = "problem.pddl"
print LocalSimulator().run(domain_path, problem_path, RandomExecutor())
