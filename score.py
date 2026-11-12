class Score:
    """Ұпай: жиналған ұпай санын сақтайды."""

    def __init__(self, goal):
        self.points = 0
        self.goal = goal

    def add(self, amount):
        self.points += amount

    def reset(self):
        self.points = 0

    def reached_goal(self):
        return self.points >= self.goal
