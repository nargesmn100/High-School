#This program makes a list of the first 10 cubes (that is, the cube of each integer from 1 through 10), and then prints out the value of each cube.



cubes_list = [ ]

for number in range (1, 11):
  cube = number ** 3
  cubes_list.append(cube)
print(cubes_list)
