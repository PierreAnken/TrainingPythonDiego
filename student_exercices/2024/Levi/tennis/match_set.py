from match import Match


class MatchSet:

    def __init__(self, match: Match):
        self.match_points = []
        self.match = match

    # 6 with 2 difference
    def get_set_winner(self) -> str:

        points = self.get_points()

        # At least a player has 6 points?
        if points[0] >= 6 or points[1] >= 6:
            # Is there at least a difference from 2?
            if abs(points[0] - points[1]) > 1:
                return 'A' if points[0] > points[1] else 'B'

    def get_points(self) -> list[int]:
        # Sum points by player
        points = [0, 0]  # A - B
        for point in self.match_points:
            if point.winner == 'A':
                points[0] += 1
            else:
                points[1] += 1
        return points

    def is_finished(self):
        return bool(self.get_set_winner())

    def play_set(self):

        from match_point import MatchPoint

        # Until the set is finished we play points
        while not self.is_finished():
            match_point = MatchPoint(self)
            match_point.play_point()
            self.match_points.append(match_point)

    def __str__(self):
        # Set result: [A:3, B:6]
        points = self.get_points()
        return f'Set result: [A:{points[0]}, B:{points[1]}]'
