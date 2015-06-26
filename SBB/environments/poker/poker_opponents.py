import random
import numpy
from ..default_opponent import DefaultOpponent
from ...config import Config

class PokerRandomOpponent(DefaultOpponent):
    def __init__(self):
        super(PokerRandomOpponent, self).__init__("random")
        self.seed_ = random.randint(0, Config.RESTRICTIONS['max_seed'])

    def initialize(self):
        self.random_generator_ = numpy.random.RandomState(seed=self.seed_)

    def execute(self, point_id, inputs, valid_actions, is_training):
        return self.random_generator_.choice(valid_actions)

    def __str__(self):
        return self.opponent_id +":"+str(self.seed_)

    def __repr__(self):
        return self.opponent_id +":"+str(self.seed_)

class PokerAlwaysFoldOpponent(DefaultOpponent):
    def __init__(self):
        super(PokerAlwaysFoldOpponent, self).__init__("always_fold")

    def initialize(self):
        pass

    def execute(self, point_id, inputs, valid_actions, is_training):
        return 0

class PokerAlwaysCallOpponent(DefaultOpponent):
    def __init__(self):
        super(PokerAlwaysCallOpponent, self).__init__("always_call")

    def initialize(self):
        pass

    def execute(self, point_id, inputs, valid_actions, is_training):
        return 1

class PokerAlwaysRaiseOpponent(DefaultOpponent):
    def __init__(self):
        super(PokerAlwaysRaiseOpponent, self).__init__("always_raise")

    def initialize(self):
        pass

    def execute(self, point_id, inputs, valid_actions, is_training):
        return 2