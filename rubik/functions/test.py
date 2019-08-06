import json
from rubik.rubik import random_cube, validate_cube, score_cube, submit_cube, Cube

cube = random_cube()
jv = cube.to_json()
print(jv)
cube2 = Cube(jv)
print(cube2.to_json() == jv)

ok = validate_cube(cube)
print(ok)

ok = validate_cube(Cube())
print(ok)

score = score_cube(cube)
print(score)

jv2 = '''{"faces":[
    ["G","G","G","G","G","G","G","G","G"],
    ["B","B","B","B","B","B","B","B","B"],
    ["O","O","O","O","O","O","O","O","O"],
    ["R","R","R","R","R","R","R","R","R"],
    ["Y","Y","Y","Y","Y","Y","Y","Y","Y"],
    ["W","W","W","W","W","W","W","W","W"]
]}'''
cube3 = Cube(jv2)
ok = validate_cube(cube3)
print(ok)

score = score_cube(cube3)
print(score)

submitted = submit_cube(random_cube())
print(submitted)

dct = {"faces": [
    ["G", "G", "G", "G", "G", "G", "G", "G", "G"],
    ["B", "B", "B", "B", "B", "B", "B", "B", "B"],
    ["O", "O", "O", "O", "O", "O", "O", "O", "O"],
    ["R", "R", "R", "R", "R", "R", "R", "R", "R"],
    ["Y", "Y", "Y", "Y", "Y", "Y", "Y", "Y", "Y"],
    ["W", "W", "W", "W", "W", "W", "W", "W", "W"]
]}

cfj = Cube(json.dumps(dct))
print(cfj.to_json())


