import json, random

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
    for j in range(9):
        if j is not 4:
            colors = [BLUE, RED, GREEN, YELLOW, ORANGE, WHITE]
            random.shuffle(colors)
            for i in range(6):
                cube.faces[i][j] = colors[i]
    return cube


def validate_cube(cube):
    ok = True
    for j in range(9):
        if ok:
            colors = {BLUE, RED, GREEN, YELLOW, ORANGE, WHITE}
            for i in range(6):
                colors.discard(cube.faces[i][j])
            ok = (ok and (len(colors) is 0))
    return ok
