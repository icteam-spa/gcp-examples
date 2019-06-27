import json

NAC = ""
BLUE = "B"
RED = "R"
GREEN = "G"
YELLOW = "Y"
ORANGE = "O"
WHITE = "W"


class Cube:

    def __init__(self):
        self.faces = [
            [NAC, NAC, NAC, NAC, BLUE, NAC, NAC, NAC, NAC],
            [NAC, NAC, NAC, NAC, RED, NAC, NAC, NAC, NAC],
            [NAC, NAC, NAC, NAC, GREEN, NAC, NAC, NAC, NAC],
            [NAC, NAC, NAC, NAC, YELLOW, NAC, NAC, NAC, NAC],
            [NAC, NAC, NAC, NAC, ORANGE, NAC, NAC, NAC, NAC],
            [NAC, NAC, NAC, NAC, WHITE, NAC, NAC, NAC, NAC]
        ]

    def to_json(self):
        return json.dumps({'faces': self.faces})


def random_cube():
    cube = Cube()
    return cube

