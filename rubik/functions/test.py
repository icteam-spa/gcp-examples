from rubik import random_cube, validate_cube, Cube

cube = random_cube()
jv = cube.to_json()
print(jv)

ok = validate_cube(cube)
print(ok)

ok = validate_cube(Cube())
print(ok)



