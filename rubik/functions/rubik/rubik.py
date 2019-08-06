import json, random, uuid
from google.cloud import pubsub_v1

NAC = ""
BLUE = "B"
RED = "R"
GREEN = "G"
YELLOW = "Y"
ORANGE = "O"
WHITE = "W"


def parse_cube(dct):
    if 'faces' in dct:
        return dct['faces']
    else:
        return [
            [NAC, NAC, NAC, NAC, BLUE, NAC, NAC, NAC, NAC],
            [NAC, NAC, NAC, NAC, RED, NAC, NAC, NAC, NAC],
            [NAC, NAC, NAC, NAC, GREEN, NAC, NAC, NAC, NAC],
            [NAC, NAC, NAC, NAC, YELLOW, NAC, NAC, NAC, NAC],
            [NAC, NAC, NAC, NAC, ORANGE, NAC, NAC, NAC, NAC],
            [NAC, NAC, NAC, NAC, WHITE, NAC, NAC, NAC, NAC]
        ]


class Cube:
    def __init__(self, text=''):
        if text == '':
            self.faces = [
                [NAC, NAC, NAC, NAC, BLUE, NAC, NAC, NAC, NAC],
                [NAC, NAC, NAC, NAC, RED, NAC, NAC, NAC, NAC],
                [NAC, NAC, NAC, NAC, GREEN, NAC, NAC, NAC, NAC],
                [NAC, NAC, NAC, NAC, YELLOW, NAC, NAC, NAC, NAC],
                [NAC, NAC, NAC, NAC, ORANGE, NAC, NAC, NAC, NAC],
                [NAC, NAC, NAC, NAC, WHITE, NAC, NAC, NAC, NAC]
            ]
        else:
            self.faces = json.loads(text, object_hook=parse_cube)

    def to_json(self):
        return json.dumps({'faces': self.faces})


def random_cube():
    """
    Create a random Rubik cube
    :return: a cube
    """
    cube = Cube()
    for j in range(9):
        if j is not 4:
            colors = [BLUE, RED, GREEN, YELLOW, ORANGE, WHITE]
            random.shuffle(colors)
            for i in range(6):
                cube.faces[i][j] = colors[i]
    return cube


def validate_cube(cube):
    """
    Validate a rubik cube
    :param
        cube (rubik.Cube): a cube to be validate
    :return (boolean): true if the cube is valid, false otherwise
    """
    ok = True
    for j in range(9):
        if ok:
            colors = {BLUE, RED, GREEN, YELLOW, ORANGE, WHITE}
            for i in range(6):
                colors.discard(cube.faces[i][j])
            ok = (ok and (len(colors) is 0))
    return ok


def score_cube(cube):
    '''
    Score a cube
    :param cube: a cube to be scored
    :return: the value of the score
    '''
    score = 0
    for f in range(6):
        fc = cube.faces[f][4]
        for j in range(9):
            if fc == cube.faces[f][j]:
                score += 1
    return score


def submit_cube(cube):
    """
    :param
        cube(Cube):
    :return:
    """
    # TODO project_id = "Your Google Cloud Project ID"
    # TODO topic_name = "Your Pub/Sub topic name"

    # publisher = pubsub_v1.PublisherClient()
    # topic = publisher.topic_path(project_id, topic_name)

    result = dict()
    if validate_cube(cube):
        score = score_cube(cube)
        request_id = str(uuid.uuid4())
        result['status'] = "ok"
        result['message'] = "Cube submitted"
        result['request_id'] = request_id
        result['initial_score'] = score
    else:
        result['status'] = "ko"
        result['message'] = "Invalid cube"

    return result

