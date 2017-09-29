from __future__ import print_function

print('Welcome to PyMaze')

# Setup an x by y 2D array full of walls (+)
col = 5
row = 4
mz = [["#"] * col for i in range(row)]
print("mz = %r" % mz)

# set the open path
mz[0][1] = " "
mz[1][1] = " "
mz[1][2] = " "
mz[2][2] = " "
mz[2][3] = " "
mz[3][3] = " "

# print the maze
for y in reversed(range(row)):
  for x in range(col):
  	print(mz[y][x], end=' ')
  print("")

print("")
print("Goodbye")